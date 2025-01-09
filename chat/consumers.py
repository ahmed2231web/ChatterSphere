import json
import base64
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.core.files.base import ContentFile
from .models import Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json.get('type', 'message')
        message = text_data_json.get('message', '')
        sender = text_data_json.get('sender', '')
        image_data = text_data_json.get('image', None)

        # Save message to database
        if message or image_data:
            await self.save_message(sender, message, image_data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
                'image': image_data
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        image = event.get('image', None)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'image': image
        }))

    @database_sync_to_async
    def save_message(self, username, message_text, image_data=None):
        sender = User.objects.get(username=username)
        message = Message(
            sender=sender,
            room=self.room_name,
            message=message_text
        )

        if image_data and image_data.startswith('data:image'):
            # Extract the base64 data
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            
            # Create a ContentFile from the base64 data
            image_content = ContentFile(base64.b64decode(imgstr), name=f'chat_image_{message.id}.{ext}')
            message.image = image_content

        message.save()
        return message