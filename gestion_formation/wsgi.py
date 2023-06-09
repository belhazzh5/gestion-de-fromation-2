"""
WSGI config for gestion_formation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import pathlib 
from django.core.wsgi import get_wsgi_application

CURRENT_DIR = pathlib.Path(__file__).parent


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_formation.settings')

application = get_wsgi_application()
