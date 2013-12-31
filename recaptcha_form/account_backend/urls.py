
from django.conf.urls import patterns, url

from account.urls import *
from .forms import RecaptchaSignupForm

urlpatterns = urlpatterns
urlpatterns.insert(0, url(r"^signup/$", SignupView.as_view(form_class=RecaptchaSignupForm), name="account_signup"))