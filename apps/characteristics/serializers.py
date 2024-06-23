from rest_framework import serializers
from .models import Characteric, CharacteristicItem


class CharacteristicItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacteristicItem
        fields = ['id', 'name', 'value']


class CharactericSerializer(serializers.ModelSerializer):
    items = CharacteristicItemSerializer(many=True)

    class Meta:
        model = Characteric
        fields = ['id', 'product', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        characteric = Characteric.objects.create(**validated_data)
        for item_data in items_data:
            CharacteristicItem.objects.create(characteristic=characteric, **item_data)
        return characteric

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.product = validated_data.get('product', instance.product)
        instance.save()

        # Удалить старые характеристики
        instance.items.all().delete()

        # Создать новые характеристики
        for item_data in items_data:
            CharacteristicItem.objects.create(characteristic=instance, **item_data)

        return instance
