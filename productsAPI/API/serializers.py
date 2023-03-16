from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    size = serializers.CharField(max_length=5)
    manufac_id = serializers.IntegerField()
    cat_id = serializers.IntegerField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.manufac_id = validated_data.get('manufac_id', instance.manufac_id)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance