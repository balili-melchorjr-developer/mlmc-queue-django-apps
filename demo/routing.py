from django.urls import re_path

from .consumers import PostConsumer, RoomConsumer, ChatRoomConsumer

websocket_urlpatterns = [
    re_path(r'^ws/posts/$', PostConsumer.as_asgi()),
    re_path(r'ws/chat/room/$', RoomConsumer.as_asgi())
]