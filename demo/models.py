from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

from account.models import Account

STATUS = (
    ('Draft', 'Draft'),
    ('Publish', 'Publish'),
    ('Archive', 'Archive'),
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    status = models.CharField(choices=STATUS, default='Draft', max_length=200)

    author = models.ForeignKey(
        Account,
        related_name='blog_posts',
        on_delete=models.CASCADE,        
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Room(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True, unique=True)
    host = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='rooms')
    current_users = models.ManyToManyField(Account, related_name='current_rooms', blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey('demo.Room', on_delete=models.CASCADE, related_name='messages')
    text = models.TextField(max_length=500)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message({self.user} {self.room})"


