from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product,Order,Comment,Like



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields ='__all__'
class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    user = UserSerializer(many=True, read_only=True)
    class Meta:
        model=Order
        fields ='__all__'
class CommentSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    user = UserSerializer(many=True, read_only=True)
    class Meta:
        model=Comment
        fields ='__all__'
class LikeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    user = UserSerializer(many=True, read_only=True)
    class Meta:
        model=Comment
        fields ='__all__'

