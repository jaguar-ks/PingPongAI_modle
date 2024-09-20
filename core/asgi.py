"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import game.routing  # Ensure this is the correct import for your routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Initialize Django
# django.setup()

# This is where you define how to route different types of protocols
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            game.routing.websocket_urlpatterns  # This should match your WebSocket URL patterns
        )
    ),
})
