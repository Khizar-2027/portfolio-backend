"""
WSGI config for portfolio_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""


# This is before changes
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_backend.settings')

# application = get_wsgi_application()


# This is after changes
import os

from django.core.wsgi import get_wsgi_application

settings_module = 'portfolio_backend.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'portfolio_backend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()