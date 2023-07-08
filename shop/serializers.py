from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Order, Comment, Like



class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields ='__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=Order
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Comment
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Like
        fields = "__all__"

