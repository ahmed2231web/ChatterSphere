import os
import django
from django.core.asgi import get_asgi_application

'''
. The os module is used to interact with the operating system.

. The django module is imported to set up the Django environment.

. get_asgi_application is a Django utility that returns an ASGI application callable.
'''
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')
django.setup()

'''
.This line sets the default settings module for the Django application. It tells Django to look for settings in the chatapp.settings module.

.django.setup() initializes the Django application, allowing you to use its features.
'''

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat.consumers import ChatConsumer

'''
Here, several components from Django Channels are imported:

    . ProtocolTypeRouter: This router allows you to route different types of protocols (like HTTP and WebSocket).
    
    . URLRouter: This router is used to route WebSocket connections based on URL patterns.
   
    . AuthMiddlewareStack: This middleware stack adds authentication capabilities to the WebSocket connections.
    
    . path: A utility for defining URL patterns.
    
    . ChatConsumer: A consumer class that handles WebSocket connections for chat functionality.
'''


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/chat/<str:room_name>/", ChatConsumer.as_asgi()),
        ])
    ),
})

'''
. The application variable is defined as a ProtocolTypeRouter instance.

. It routes HTTP requests to the Django ASGI application using get_asgi_application().

. WebSocket requests are routed through the AuthMiddlewareStack, which ensures that only authenticated users can access the WebSocket endpoints.

. The URL pattern for WebSocket connections is defined as ws/chat/<str:room_name>/, which allows for dynamic room names in the chat application. The ChatConsumer handles the WebSocket connections for these chat rooms.
'''