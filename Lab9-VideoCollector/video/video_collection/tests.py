from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from .models import Video
from video_collection.models import Video
from django.db import IntegrityError
from django.core.exceptions import ValidationError


class TestHomePageMessage(TestCase):

    def test_app_tittle_message_shown_on_home_page(self):
        url = reverse('home')
        response = self.client.get(url) # mimic a user get request to the url
        self.assertContains(response, "Otter Videos Collection")

class TestAddVideos(TestCase):

    def test_add_video(self):
        valid_video = {
            'name': 'California Sea Otters',
            'url': 'https://www.youtube.com/watch?v=94NJ6ckrKEg',
            'notes': 'PBS documentary'
        }

        url = reverse('add_video')
        response = self.client.post(url, data=valid_video, follow=True)

        self.assertTemplateUsed('video_collection/video_list.html')

        # does the video list show the new video
        self.assertContains(response, 'California Sea Otters')
        self.assertContains(response, 'https://www.youtube.com/watch?v=94NJ6ckrKEg')
        self.assertContains(response, 'PBS documentary')

        #check the database
        video_count = Video.objects.count()
        self.assertEqual(1, video_count)
        #check if the attributes are the same
        video = Video.objects.first()
        self.assertEqual('California Sea Otters', video.name)
        self.assertEqual('https://www.youtube.com/watch?v=94NJ6ckrKEg', video.url)
        self.assertEqual('PBS documentary', video.notes)
        self.assertEqual('94NJ6ckrKEg', video.video_id)

    def test_add_video_invalid_url_not_added(self):
        invalid_video_url = {
            'https://www.youtube.com/',
            'https://www.youtube.com/watch',
            'https://www.youtube.com/watch?',
            'https://www.youtube.com/watch?abc=123',
            'https://www.youtube.com/watch?v=',
            'https://google.com',
            'https://google.com/watch?v=yuio23kk'
        }

        for invalid_url in invalid_video_url:

            new_video = {
                'name': 'example',
                'url': invalid_url,
                'notes': 'example notes'
            }

            url = reverse('add_video')
            response = self.client.post(url, data=new_video)

            self.assertTemplateNotUsed('video_collection/add.html')

            messages = response.context['messages'] # this call the warning message in the view
            message_text = [ message.message for message in messages ]

            self.assertIn('Invalid Youtube video', message_text)
            self.assertIn('Please correct the data entered.', message_text)

            # check the database
            video_count = Video.objects.count()
            self.assertEqual(0, video_count)

class TestVideoList(TestCase):

    def test_all_videos_display_ordered(self):
        # these are going to be forced created in the database, no checking url validation just pattern filter
        v1 = Video.objects.create(name='abc', notes='abc', url='https://www.youtube.com/watch?v=123')
        v2 = Video.objects.create(name='zyc', notes='abc', url='https://www.youtube.com/watch?v=124')
        v3 = Video.objects.create(name='AAA', notes='abc', url='https://www.youtube.com/watch?v=125')
        v4 = Video.objects.create(name='lmn', notes='abc', url='https://www.youtube.com/watch?v=126')

        # expected order
        expected_video_order = [v3, v1, v4, v2]

        url = reverse('video_list')
        response = self.client.get(url)

        videos_in_template = list(response.context['videos']) #convert the response in a list, by default is query type

        self.assertEqual(expected_video_order, videos_in_template)

    # 'no video' message is display when no videos in db
    def test_no_video_message(self):
        url = reverse('video_list')
        response = self.client.get(url)
        self.assertContains(response, 'No videos')
        self.assertEqual(0, len(response.context['videos']))

    def test_singular_video_message(self):
        v1 = Video.objects.create(name='abc', notes='abc', url='https://www.youtube.com/watch?v=123')
        url = reverse('video_list')
        response = self.client.get(url)

        self.assertContains(response, '1 video')
        self.assertNotContains(response, '1 videos')


    def test_video_number_message(self):
        v1 = Video.objects.create(name='abc', notes='abc', url='https://www.youtube.com/watch?v=123')
        v2 = Video.objects.create(name='zyc', notes='abc', url='https://www.youtube.com/watch?v=124')
        url = reverse('video_list')
        response = self.client.get(url)

        self.assertContains(response, '2 videos')


class TestVideoSearch(TestCase):
    def test_video_search_match(self):
        v1 = Video.objects.create(name='abc', notes='abc', url='https://www.youtube.com/watch?v=123')
        v2 = Video.objects.create(name='not me', notes='abc', url='https://www.youtube.com/watch?v=124')
        v3 = Video.objects.create(name='AbC', notes='abc', url='https://www.youtube.com/watch?v=125')
        v4 = Video.objects.create(name='hello ABC', notes='abc', url='https://www.youtube.com/watch?v=126')

        expected_video_order = [v1, v3, v4] #expected order
        response = self.client.get(reverse('video_list') + '?search_term=abc')
        videos_in_template = list(response.context['videos'])
        self.assertEqual(expected_video_order, videos_in_template)

    def test_video_search_no_matches(self):
        v1 = Video.objects.create(name='abc', notes='abc', url='https://www.youtube.com/watch?v=123')
        v2 = Video.objects.create(name='not me', notes='abc', url='https://www.youtube.com/watch?v=124')
        v3 = Video.objects.create(name='AbC', notes='abc', url='https://www.youtube.com/watch?v=125')
        v4 = Video.objects.create(name='hello ABC', notes='abc', url='https://www.youtube.com/watch?v=126')

        expected_video_order = [] #expect empty list
        response = self.client.get(reverse('video_list') + '?search_term=kittens')
        videos_in_template = list(response.context['videos'])
        self.assertEqual(expected_video_order, videos_in_template)
        self.assertContains(response, 'No videos')

class TestVideoModel(TestCase):

    def test_invalid_url_raises_validation_error(self):
        invalid_video_url = {
            'https://www.youtube.com/',
            'https://www.youtube.com/watch',
            'https://www.youtube.com/watch?',
            'https://www.youtube.com/watch/somethingelse',
            'https://www.youtube.com/watch/somethingelse?v=wer123',
            'https://www.youtube.com/watch?abc=123',
            'https://www.youtube.com/watch?v=',
            'https://google.com',
            'https://google.com/watch?v=yuio23kk'
        }

        for invalid_url in invalid_video_url:
            with self.assertRaises(ValidationError):
                Video.objects.create(name='example', notes='abc', url=invalid_url)

        #nothing should be added to the db
        self.assertEqual(0, len(Video.objects.all()))


    def test_duplicate_video_raises_integrity_error(self):
        v1 = Video.objects.create(name='abc', notes='abc', url='https://www.youtube.com/watch?v=123')
        with self.assertRaises(IntegrityError):
            Video.objects.create(name='abc', notes='abc', url='https://www.youtube.com/watch?v=123')