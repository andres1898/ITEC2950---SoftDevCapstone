from django.test import TestCase
from django.urls import reverse

from .models import Place


class TestHomePage(TestCase):

    def test_home_page_shows_empty_list_message_for_empty_database(self):
        home_page_url = reverse('place_list')
        response = self.client.get(home_page_url)
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertContains(response, 'You have no places in your wishlist.')


class TestVisitedPage(TestCase):

    def test_visited_page_shows_empty_list_message_for_empty_database(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertContains(response, 'No places visited yet')


class TestWishList(TestCase):
    fixtures = ['test_places']

    def test_viewing_wishlist_contains_not_visited_places(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        self.assertContains(response, 'Tokyo')
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco')
        self.assertNotContains(response, 'Moab')


class TestVisitedList(TestCase):
    fixtures = ['test_places']

    def test_viewing_places_visited_shows_visited_places(self):
        response = self.client.get(reverse('places_visited'))

        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        self.assertContains(response, 'San Francisco')
        self.assertContains(response, 'Moab')
        self.assertNotContains(response, 'Tokyo')
        self.assertNotContains(response, 'New York')


class TestAddNewPlace(TestCase):

    def test_add_new_unvisited_place(self):
        add_place_url = reverse('place_list')
        new_place_data = {'name': 'Tokyo', 'visited': False}

        response = self.client.post(add_place_url, new_place_data, follow=True)
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        response_places = response.context['places']
        self.assertEqual(1, len(response_places))

        tokyo_response = response_places[0]
        tokyo_database = Place.objects.get(name='Tokyo', visited=False)
        self.assertEqual(tokyo_database, tokyo_response)

        # another place added
        response = self.client.post(reverse('place_list'), {'name': 'Yosemite', 'visited': False}, follow=True)
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        response_places = response.context['places']
        self.assertEqual(2, len(response_places))

    def test_add_new_visited_place_to_wishlist(self):
        response = self.client.post(reverse('place_list'), {'name': 'Tokyo', 'visited': True}, follow=True)

        # Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # What data was used to populate the template?
        response_places = response.context['places']

        # Should be 0 items - have not added any un-visited places
        self.assertEqual(0, len(response_places))

        # Expect this data to be in the database. Use get() to get data with
        # the values expected. Will throw an exception if no data, or more than
        # one row, matches. Remember throwing an exception will cause this test to fail
        place_in_database = Place.objects.get(name='Tokyo', visited=True)


class TestVisitPlace(TestCase):

    fixtures = ['test_places']

    def test_visit_place(self):
        visit_place_url = reverse('place_was_visited', args=(2,)) # 2 will act as the pk
        response = self.client.post(visit_place_url, follow=True)
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        # NY should be removed from the wishlist
        self.assertNotContains(response, 'New York')

        # Check if NY was added to the visited places
        new_york = Place.objects.get(pk=2)
        self.assertTrue(new_york.visited)

    def test_visit_non_existent_place(self):
        visit_nonexistent_place_url = reverse('place_was_visited', args=(900,))
        response = self.client.post(visit_place_url, follow=True)
        self.assertEqual(404, response.status_code)  # rise error with 'not found code'
