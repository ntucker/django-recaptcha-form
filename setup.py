#!/usr/bin/env python

from distutils.core import setup
import os.path

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='django-recaptcha-form',
      version='0.1.2',
      description='Recaptcha for Django Forms',
      author='Nathaniel Tucker',
      author_email='me@ntucker.me',
      url='http://github.com/ntucker/django-recaptcha',
      packages=[
          'recaptcha_form',
          'recaptcha_form.registration_backend',
          'recaptcha_form.account_backend',
          'recaptcha_form.pinax_backend',
      ],
      install_requires=['django>=1.6', 'recaptcha-client>=1.0.6', ],
      long_description=read('README'),
      license='BSD',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
     )
