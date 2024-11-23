from rest_framework import serializers
from .models import Characteric


class CharacteristicItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteric
        fields = ['name', 'value']

