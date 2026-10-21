from django.test import TestCase
from django.urls import reverse
from .models import Video

from video_collection.models import Video


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


class TestVideoList(TestCase):
    pass

class TstVideoSearch(TestCase):
    pass

class TestVideoModel(TestCase):
    pass
