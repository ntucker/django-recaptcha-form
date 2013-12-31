
from django.conf.urls import patterns, url

from pinax.apps.account.urls import *
from .forms import RecaptchaSignupForm

urlpatterns = urlpatterns
urlpatterns.insert(0, url(r"^signup/$", signup_view, {"form_class":RecaptchaSignupForm}, name="acct_signup"))