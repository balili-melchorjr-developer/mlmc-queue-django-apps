from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('post', views.PostViewSet, basename='post')

urlpatterns = [
    path('chatty/', views.chatty, name='chatty'),
    path('chatty/<str:room_name>', views.room, name='room'),
    path('chatroom/', views.chatroom, name='chatroom'),
    path('chatroom/<int:pk>/', views.exact_room, name='exact_room')
]

urlpatterns += router.urls

