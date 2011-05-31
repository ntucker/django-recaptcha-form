from recaptcha_form.forms import RecaptchaForm
from registration.forms import RegistrationForm


class RecaptchaRegistrationForm(RecaptchaForm, RegistrationForm):
    pass