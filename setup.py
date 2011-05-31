#!/usr/bin/env python

from distutils.core import setup

setup(name='Django Recaptcha',
      version='0.1',
      description='Recaptcha for Django Forms',
      author='Nathaniel Tucker',
      url='http://bitbucket.org/ntucker/django-recaptcha',
      packages=['recaptcha_form', 'recaptcha_form.registration_backend'],
     )