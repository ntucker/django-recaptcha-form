from registration.backends.default import DefaultBackend
from .forms import RecaptchaRegistrationForm


class RecaptchaBackend(DefaultBackend):
    def get_form_class(self, request):
        """
        Return the recaptcha form class used for user registration.
        
        """
        return RecaptchaRegistrationForm
