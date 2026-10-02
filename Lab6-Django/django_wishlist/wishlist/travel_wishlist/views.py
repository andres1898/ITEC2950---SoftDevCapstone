from django.shortcuts import render, redirect
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