from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, ListView, UpdateView
from . import forms
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import InfoForm, NehasimForm, SendMailForm, PaymentForm
from accounts.models import PersonalInfo, NehasimModel, SendMailModel, Payment
from django.contrib.auth import get_user_model
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
User = get_user_model()




# Create your views here.
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class Info(CreateView):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = InfoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = InfoForm(request.POST)
        if form.is_valid():
            info_model = form.save(commit=False)
            info_model.user = request.user
            existing_personal_info = PersonalInfo.objects.filter(user_id=request.user)
            if len(existing_personal_info.values()) > 0:
                existing_personal_info.delete()
            info_model.save()
            return redirect('accounts:personal')

        return render(request, 'accounts/personal_info.html')

class UserView(TemplateView):
    template_name = 'accounts/userpage.html'

class PersonalInfoView(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/personal_info.html'

    def get_queryset(self, request):
        self.cities_user = PersonalInfo.objects.filter(user_id=request.user).values()
        return self.cities_user

    def get(self, request):
        my_infos = self.get_queryset(request)
        args = {}
        if len(my_infos) > 0:
            args = {
                'first_name': [info['first_name'] for info in my_infos][0],
                'second_name':[info['second_name'] for info in my_infos][0],
                'city': [info['city'] for info in my_infos][0],
                'street': [info['street'] for info in my_infos][0],
                'home_number': [info['home_number'] for info in my_infos][0],
                'phone_number': [info['phone_number'] for info in my_infos][0],
            }

        return render(request, 'accounts/personal_info.html', args)

class NehasimView(TemplateView):
    success_url = reverse_lazy('accounts:nehasim')
    template_name = 'accounts/nehasim.html'

    def get_queryset(self, request):
        self.cities = PersonalInfo.objects.filter(user_id=request.user).values('city', 'street', 'home_number')
        return self.cities

    def get(self, request):
        form = NehasimForm()
        my_infos = self.get_queryset(request)
        args = {}
        if len(my_infos) > 0:
            args = {
                'city': [info['city'] for info in my_infos][0],
                'street': [info['street'] for info in my_infos][0],
                'home_number': [info['home_number'] for info in my_infos][0],
            }
        form.fields['city'].initial = args['city']
        form.fields['street'].initial = args['street']
        form.fields['home_number'].initial = args['home_number']
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NehasimForm(request.POST)
        if form.is_valid():
            nehasim_model = form.save(commit=False)
            nehasim_model.user = request.user
            nehasim_model.save()
            return render(request, 'accounts/nehasim.html', {'text':'Nehasim updated', 'form':form})

class SendMail(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/send_mail.html'

    def get(self, request):
        form = SendMailForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = SendMailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(name, message, email, ['estrella4494@gmail.com'],)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return render(request, 'accounts/send_mail.html', {'form':form, 'text':'Thank you for the message!'})

class PaymentView(TemplateView):
    template_name = 'accounts/payment.html'

    def get(self, request):
        form = PaymentForm()
        return render(request, self.template_name, {'form': form})


    def get_queryset(self, request):
        self.credit_info = Payment.objects.filter(user_id=request.user).values()
        return self.credit_info

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            pay = form.save(commit=False)
            pay.user = request.user
            pay.save()
            return render(request, 'accounts/payment.html', {'text':'Credit card saved', 'form':form})

        return render(request, 'accounts/payment.html',{'form':form})
