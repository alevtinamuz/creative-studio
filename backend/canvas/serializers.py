from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Canvas


class CanvasSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Canvas
        fields = ('id', 'canvas_data', 'updated_at', 'last_user', 'name', 'avatar', 'created_at_formatted', 'created_by', 'users')