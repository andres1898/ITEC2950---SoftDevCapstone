from django.core.exceptions import ValidationError
from django.db import models
from urllib import parse

# a class that describe a video: name, url, notes
class Video(models.Model):
    # Describe the fields tha will be the columns in our database
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null=True) # optional field
    video_id = models.CharField(max_length=40, unique=True) #this make Django to check if the values are unique

    def save(self, *arg, **kwargs):

        # validation for a video from Youtube.com
        if not self.url.startswith('https://www.youtube.com/watch'):
            raise ValidationError('Video is not from Youtube.com')

        # extract the video ID form the url
        url_components = parse.urlsplit(self.url)
        query_string = url_components.query # this results in 'v=poj789da'

        if not query_string:
            raise ValidationError(f'Invalid Youtube URL {self.url}')
        parameters = parse.parse_qs(query_string, strict_parsing=True) # this will create a dictionary
        v_parameters_list = parameters.get('v') #return None if not found the 'v'

        if not v_parameters_list: # if it is an None
            raise ValidationError(f'Invalid Youtube URL {self.url}')
        self.video_id = v_parameters_list[0] # this will be the ID string

        super().save(*arg, **kwargs) # this will call the by-default save() method of Django and also safe the video


    def __str__(self):
        return (f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Video ID:{self.video_id}, Notes: {self.notes[:200]}')