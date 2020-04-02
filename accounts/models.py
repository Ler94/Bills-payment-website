from django.db import models
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
import misaka
from django import template
from django.contrib.auth import get_user_model

User = get_user_model()
register = template.Library()



class PersonalInfo(models.Model):
    user = models.OneToOneField(User, related_name="profile_infos",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    second_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    home_number = models.IntegerField(null=True, blank=True)
class NehasimModel(models.Model):
    city = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    home_number = models.IntegerField(null=True, blank=True)

class SendMailModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=300)

class Payment(models.Model):
    CardholderName = models.CharField(max_length=100, null=True,)
    cc_number = CardNumberField('card number')
    cc_code = SecurityCodeField('security code')
    Expiration_Date = models.CharField(max_length=100, null=True, blank=True)
    Year = models.IntegerField(max_length=100, null=True, blank=True)
