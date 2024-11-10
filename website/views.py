from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Coffeeshop, Rating, Event
from .forms import CoffeeshopForm, RatingForm
# Create your views here.

today = timezone.now().date()

def home(request):
    ratings = Rating.objects.all()
    coffeeshop_list = Coffeeshop.objects.annotate(average_rating=Avg('rating__rating'),
                                                  average_price=Avg('rating__price')).order_by('-average_rating')
    next_event = Event.objects.filter(event_date__gte=today).order_by('event_date').first()
    return render(request,'website/home.html',{
         'coffeeshop_list': coffeeshop_list,
         'next_event': next_event,
         })

def view_reviews(request, coffeeshop_id):
    coffeeshop = Coffeeshop.objects.get(pk=coffeeshop_id)
    reviews = coffeeshop.rating_set.all()

    return render(request,'website/reviews.html',{
         'reviews': reviews,
         'coffeeshop': coffeeshop,
         })

@login_required
def add_coffeeshop(request):
    if request.method == "POST":
        form = CoffeeshopForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.created_by = request.user # logged in user
            shop.coffeeshop_status = 'A'
            shop.save()
            messages.success(request, "New Coffee Shop added")
            return redirect('home')
    else:
        form = CoffeeshopForm
    return render(request,'website/add_coffeeshop.html', {'form': form})


@login_required
def add_rating(request):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.created_by = request.user # logged in user
            rating.save()
            messages.success(request, "Rating added")
            return redirect('home')
    else:
        form = RatingForm
    return render(request,'website/add_rating.html', {'form': form})

@login_required
def my_ratings(request):
    user = request.user
    rating_list = Rating.objects.filter(created_by=user).order_by('coffeeshop')
    return render(request,'website/my_ratings.html',{
         'rating_list': rating_list,
         })

@login_required
def edit_rating(request, rating_id):
    rating = Rating.objects.get(pk=rating_id)
    if request.user == rating.created_by:
        form = RatingForm(request.POST or None, instance=rating)
        if form.is_valid():
            form.save()
            messages.success(request, "Rating updated")
            return redirect('my_ratings')
        return render(request,'website/edit_rating.html', {
            'rating': rating,
            'form': form,})
    else:
        messages.success(request, "You can't edit that rating")
        return redirect('home')

@login_required
def delete_rating(request, rating_id):
    rating = Rating.objects.get(pk=rating_id)
    if request.user == rating.created_by:
        rating.delete()
        messages.success(request, "Review deleted")
        return redirect('my_ratings')
    else:
        messages.success(request, "You can't delete that rating")
        return redirect('home')
