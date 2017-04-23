"""
Configuración WSGI de CIME-Core

Expone la aplicación en una variable a nivel de módulo llamada ``application``.

documentación:
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cime.settings")

application = get_wsgi_application()
