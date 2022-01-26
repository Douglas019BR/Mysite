"""
WSGI config for Mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import  sys
import os

import sys

from django.core.wsgi import get_wsgi_application
#Tip from stackoverflow
from django.conf import settings

#Tip from stackoverflow
sys.path.append('/home/user/Documents/douglas-repo/Mysite/Mysite')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mysite.settings')

application = get_wsgi_application()

