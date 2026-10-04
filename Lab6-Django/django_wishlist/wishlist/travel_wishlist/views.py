from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
# Create your views here.

def place_list(request):

    if request.method == 'POST':
        #create a new place
        form = NewPlaceForm(request.POST)
        places = form.save() #creating a model object from forms
        if form.is_valid(): # check point
            places.save() #saves in the database
            return redirect('place_list') # reload the home page

    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request,
                  'travel_wishlist/wishlist.html',
                  {'places': places,
                   'new_place_form': new_place_form})

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request,
                  'travel_wishlist/visited.html',
                  {'visited': visited}
    )

def about(request):
    author = "Andres"
    about = 'A website to keep your wishlist of place to travel'
    return render(request, 'travel_wishlist/about.html',
                  {'author': author, 'about': about})

def place_was_visited(request, place_pk):
    if request.method == 'POST':
        #place = Place.objects.get(pk=place_pk) # Database query
        # recommended way to avoid the website to crash
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True # change status
        place.save()
    return redirect('place_list')
    # It can be redirected to another location like the visited places
    #return redirect('places_visited')