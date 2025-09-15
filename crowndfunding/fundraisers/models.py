from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# We inherited our class from the built-in models.Model class that comes with Django. This means that our new model has a bunch of incredibly useful functionality right out of the box. Django will even create a database table for us based on this model!
# Our model has a bunch of attributes: title, description, etc. Each of these is itself an instance of one of the classes that comes bundled with Django. These attributes tell Django what types of fields we want in our database table





class Fundraiser(models.Model):
    title = models.CharField(max_length=200)   # Title field cannnot be longer than 200 characters
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        related_name='owned_fundraisers',
        on_delete=models.CASCADE #if fundraiser is deleted, delete all related pledges  
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)  
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser',
        related_name='pledges',
        on_delete=models.CASCADE #if fundraiser is deleted, delete all related pledges
    )  
    supporter = models.ForeignKey(
        get_user_model(),
        related_name='pledges',
        on_delete=models.CASCADE #if fundraiser is deleted, delete all related pledges
    )
    
