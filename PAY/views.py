from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required





class HomePage(TemplateView):
    template_name='base.html'
