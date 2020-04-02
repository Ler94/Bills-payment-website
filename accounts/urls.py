from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    url(r'^profile/login/?$', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r'^userpage/$', views.UserView.as_view(), name="userpage"),
    url(r'^personal/$', views.PersonalInfoView.as_view(), name="personal"),
    url(r'^personal/edit/$', views.Info.as_view(), name="edit"),
    url(r'^profile/$', views.Info.as_view(), name="profile"),
    url(r'^sendmail/$', views.SendMail.as_view(), name="send_mail"),
    url(r'^userpage/creditcard$', views.PaymentView.as_view(), name="credit_card"),
    url(r'^userpage/nehasim/$', views.NehasimView.as_view(), name="nehasim"),

]
