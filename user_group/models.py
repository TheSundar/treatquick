from django.db import models

# Create your models here.
from django.contrib.auth.models import User, UserManager


class Address(models.Model):
    street_details = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)





class CustomUser(User):
    """User with app settings."""
    blood_group     = models.CharField(max_length=50,null=False)
    mobile_no       = models.CharField(max_length=15,primary_key=True)
    last_donated    = models.DateField()
    location        = models.ForeignKey(Address,related_name='address')
    timezone        = models.CharField(max_length=50, default='Europe/London')


    objects = UserManager()

    class Meta:
        unique_together = ('username', 'location')
        ordering = ['username']

class DonationHistory(models.Model):
    '''
    1)  Donee and Donor should not be same
    '''
    donee = models.ForeignKey(CustomUser,related_name='blood_takers')
    donor = models.ForeignKey(CustomUser,related_name='blood_givers')
    donated_on = models.DateTimeField()



class Group(models.Model):
    name = models.CharField(max_length=3000)
    url = models.URLField(max_length=3000)
    users = models.ManyToManyField(CustomUser,related_name='generalusers')
    admins = models.ManyToManyField(CustomUser,related_name='adminuser')
    is_approved = models.BooleanField(default=False)