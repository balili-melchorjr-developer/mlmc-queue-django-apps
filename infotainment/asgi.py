"""
ASGI config for infotainment project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

import demo.routing
import admission.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infotainment.settings')

application = get_asgi_application()

application  = ProtocolTypeRouter({
    'http': application,
    # 'websocket': URLRouter([
    #     *demo.routing.websocket_urlpatterns,
    #     *admission.routing.websocket_urlpatterns
    # ]),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                # *demo.routing.websocket_urlpatterns,
                *admission.routing.websocket_urlpatterns,
            ])
        )
    )
})
