from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from rest_framework import viewsets

from .models import Post, Account, Room, Message
from .serializers import PostSerializer, AccountSerializer, RoomSerializer, MessageSerializer

class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_update(self, serializer):
        return super().perform_update(serializer)

def index(request):
    return render(request, 'demo/index.html')

def chatroom(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        if name:
            room = Room.objects.create(name=name, host=request.user)
            HttpResponseRedirect(reverse("room", args=[room.pk]))
    return render(request, 'chatroom/index.html')

def exact_room(request, pk):
    room: Room = get_object_or_404(Room, pk=pk)
    return render(request, 'chatroom/chatroom.html', {
        'room':room
    })

def chatty(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        if name:
            room = Room.objects.create(name=name, host=request.user)
            HttpResponseRedirect(reverse("room", args=[room.pk]))
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/chatroom.html', {
        "room_name":room_name,
    })
