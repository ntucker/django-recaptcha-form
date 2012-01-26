
from django.conf.urls.defaults import patterns, url

from pinax.account.urls import *
from .forms import RecaptchaSignupForm

urlpatterns = urlpatterns
urlpatterns.insert(0, url(r"^signup/$", signup_view, {"form_class":RecaptchaSignupForm}, name="acct_signup"))