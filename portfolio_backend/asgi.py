"""
ASGI config for portfolio_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

# This what it look like before changes
# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_backend.settings')

# application = get_asgi_application()

# --------------------------------------------------------------------------

# This what it look like after changes
import os

from django.core.asgi import get_asgi_application

settings_module = 'portfolio_backend.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'portfolio_backend.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()

