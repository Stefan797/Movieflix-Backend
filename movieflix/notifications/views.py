from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

from notifications.serializers import NotificationItemSerializer
from notifications.models import NotificationItem


# Create your views here.


class NotificationItemView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        notifications = NotificationItem.objects.all()
        serializer = NotificationItemSerializer(notifications, many=True)
        return Response(serializer.data)
