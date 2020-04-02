from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
import datetime
from django.utils.dates import MONTHS

from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField

from .models import User, PersonalInfo, NehasimModel, SendMailModel, Payment
User = get_user_model()



class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


class InfoForm(forms.ModelForm):
    first_name = forms.CharField()
    second_name = forms.CharField()
    phone_number = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    home_number = forms.IntegerField()

    class Meta:
        model = PersonalInfo
        fields = ('first_name', 'second_name', 'phone_number', 'city', 'street', 'home_number', )

class NehasimForm(forms.ModelForm):
        city = forms.CharField(required=False)
        street = forms.CharField(required=False)
        home_number = forms.IntegerField(required=False,)

        class Meta:
            model = NehasimModel
            fields = ('city', 'street', 'home_number',)

class SendMailForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = SendMailModel
        fields = ('name', 'email', 'message')


MONTH_CHOICE = list(MONTHS.items())
YEAR_DROPDOWN = []
for y in range(2020, (datetime.datetime.now().year + 5)):
    YEAR_DROPDOWN.append((y, y))


class PaymentForm(forms.ModelForm):
    CardholderName = forms.CharField(required=True)
    cc_number = CardNumberField(label='Card Number')
    cc_code = SecurityCodeField(label='CVV/CVC')
    Expiration_Date = forms.CharField(widget=forms.Select(choices=MONTH_CHOICE))
    Year = forms.IntegerField(widget=forms.Select(choices=YEAR_DROPDOWN))
    class Meta:
        model = Payment
        fields = ('cc_number', 'cc_code', 'Expiration_Date', 'Year', 'CardholderName')
