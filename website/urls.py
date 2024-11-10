from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_coffeeshop', views.add_coffeeshop, name="add_coffeeshop"),
    path('add_rating', views.add_rating, name="add_rating"),
    path('my_ratings', views.my_ratings, name="my_ratings"),
    path('edit_rating/<rating_id>', views.edit_rating, name="edit_rating"),
    path('delete_rating/<rating_id>', views.delete_rating, name="delete_rating"),
    path('view_reviews/<coffeeshop_id>', views.view_reviews, name="view_reviews")
]
