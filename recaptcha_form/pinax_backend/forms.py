from recaptcha_form.forms import RecaptchaForm
from pinax.apps.account.forms import SignupForm


class RecaptchaSignupForm(RecaptchaForm, SignupForm):
    pass