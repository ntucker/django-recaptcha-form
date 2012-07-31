from recaptcha_form.forms import RecaptchaForm
from account.forms import SignupForm


class RecaptchaSignupForm(RecaptchaForm, SignupForm):
    pass