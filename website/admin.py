from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Coffeeshop, Rating, Event

admin.site.unregister(Group)

@admin.register(Coffeeshop)
class CoffeeshopAdmin(admin.ModelAdmin):
    list_display = ('coffeeshop_name', 'coffeeshop_tag', 'created_by', 'coffeeshop_status')
    ordering = ('coffeeshop_name','coffeeshop_status')
    search_fields = ('coffeeshop_name',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('coffeeshop', 'created_by', 'rating')
    ordering = ('coffeeshop','created_by', 'rating')
    search_fields = ('coffeeshop','created_by',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('coffeeshop', 'event_date', 'details')
    ordering = ('coffeeshop','event_date',)
    search_fields = ('coffeeshop','event_date',)
