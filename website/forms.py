from django import forms
from django.forms import ModelForm
from django.core.validators import MaxValueValidator
from .models import Coffeeshop, Rating


# Create a venue form
class CoffeeshopForm(ModelForm):
    class Meta:
        model = Coffeeshop
        fields = ('coffeeshop_name', 'coffeeshop_tag', 'coffeeshop_address',)
        labels = {
            'coffeeshop_name': "",
            'coffeeshop_tag': "",
            'coffeeshop_address': "",
            }
        
        widgets = {
            'coffeeshop_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Coffee Shop Name'}),
            'coffeeshop_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Brief description'}),
            'coffeeshop_address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address / Location'}),
            }


class RatingForm(ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]
    
    class Meta:
        RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]
        model = Rating
        fields = ('coffeeshop', 'size', 'price', 'rating', 'description')
        labels = {
            'coffeeshop': "",
            'size': "",
            'price': "",
            'rating': "",
            'description': "",
            }
        
        widgets = {
            'coffeeshop': forms.Select(attrs={'class':'form-select', 'placeholder':'Coffee Shop Name'}),
            'size': forms.Select(attrs={'class':'form-select', 'placeholder':'Coffee Size / Type'}),
            'price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'How much?'}),
            'rating': forms.Select(choices=RATING_CHOICES, attrs={'class': 'form-select'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'What did you think?'}),
            }
