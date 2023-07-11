from notifications.models import NotificationItem
from rest_framework import serializers

class NotificationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationItem
        fields = '__all__'