from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
# Create your models here.

class Coffeeshop(models.Model):
    STATUS = (
        ('A', 'Active'),
        ('C', 'Closed'),
        )
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, limit_choices_to={'is_active': True}, null = True, on_delete=models.SET_NULL)
    coffeeshop_name = models.CharField('Coffee Shop Name', max_length = 100)
    coffeeshop_tag = models.CharField('Known for', max_length = 200, blank=True, null = True)
    coffeeshop_address = models.CharField('Address', max_length = 100, blank=True, null = True)
    coffeeshop_status = models.CharField('Still in business?', choices=STATUS, max_length = 1)

    def __str__(self):
        return (f'{self.coffeeshop_name}')

class Rating(models.Model):
    SIZE = (
        ('S', 'Small'),
        ('L', 'Large'),
        ('W', 'Weird Milk'),        
        )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, limit_choices_to={'is_active': True}, null = True, on_delete=models.SET_NULL)
    coffeeshop = models.ForeignKey(Coffeeshop, limit_choices_to={'coffeeshop_status': 'A'}, on_delete=models.CASCADE)
    size = models.CharField('Cup Size', choices=SIZE, max_length = 1, blank=True, null = True)
    price = models.DecimalField(
        'Price $',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0)],
        help_text="Enter the price in dollars"
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Enter a rating between 1 and 10")
    description = models.TextField('What did you think??',blank=True)

    def get_size_display(self):
        return dict(self.SIZE).get(self.size, self.size)

    def __str__(self):
        return f'{self.coffeeshop} - Drinker: {self.created_by} - Rating: {self.rating}'

class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, limit_choices_to={'is_active': True}, null = True, on_delete=models.SET_NULL)
    coffeeshop = models.ForeignKey(Coffeeshop, limit_choices_to={'coffeeshop_status': 'A'}, on_delete=models.CASCADE)
    event_date = models.DateField()
    details = models.CharField('Any details',max_length = 100, blank=True, null = True)
    def __str__(self):
        return f'{self.coffeeshop} - On: {self.event_date}'
