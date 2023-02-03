from rest_framework import serializers

from .models import Post, STATUS, Room, Message
from account.models import Account

class PostSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'status',
            'author'
        ]

    def get_author(self, obj):
        return obj.author.email

class AccountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        exclude = ['password']

class MessageSerializer(serializers.ModelSerializer):
    created_at_formatted = serializers.SerializerMethodField()
    user = AccountSerializer()

    class Meta:
        model = Message
        exclude = []
        depth = 1

    def gef_created_at_formatted(self, obj:Message):
        return obj.created_at.strftime('%d-%m-%Y %H:%M:%S')
        
class RoomSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()
    mesage = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['pk', 'name', 'host', 'message', 'current_users', 'last_message']
        depth = 1
        read_only_fields = ['messages', 'last_message']

    def get_last_message(self, obj:Room):
        return MessageSerializer(obj.messages.order_by('created_at').last()).data



