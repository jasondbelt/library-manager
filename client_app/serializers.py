#CLIENT_APP.SERIALIZERS
from .models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ["id", "email"]