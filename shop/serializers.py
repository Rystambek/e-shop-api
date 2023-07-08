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
    product = ProductSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model=Order
        fields =['id','product','user']
class CommentSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model=Comment
        fields =['id','text','product','user']
class LikeSerializer(serializers.ModelSerializer):
    product = ProductSerializer( read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model=Like
        fields =['id','like','product','user']

