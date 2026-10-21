from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models.functions import Lower
from video_collection.forms import VideoForm, SearchForm
from .models import Video


def home(request):
    app_name = 'Otter Videos Collection'
    return render(request, 'video_collection/home.html', {'app_name': app_name})


def add(request):
    if request.method == 'POST': #create a new video object
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            try:
                new_video_form.save()
                return redirect('video_list')
                #messages.info(request, 'Video added.')
                #todo show success message or redirect to list of videos
            except ValidationError:
                messages.warning(request, 'Invalid Youtube video')
            except IntegrityError: # not unique url error
                messages.warning(request, 'Video already exists')

        messages.warning(request, 'Please correct the data entered.')
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})


def video_list(request):

    search_form = SearchForm(request.GET) # Search query built by data sent by the user

    if search_form.is_valid():
        search_term = search_form.cleaned_data['search_term'] #e.g: 'river'
        videos = Video.objects.filter(name__icontains=search_term).order_by(Lower('name'))
    else: #not valid search
        search_form = SearchForm()
        videos = Video.objects.order_by(Lower('name'))

    return render(request, 'video_collection/video_list.html', {'videos': videos, 'search_form': search_form})