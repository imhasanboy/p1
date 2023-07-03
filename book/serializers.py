from rest_framework import serializers
from .models import BookModel, AuthorModel
from django.shortcuts import get_object_or_404


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('id', 'name', 'fname', 'country')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id', 'author', 'name', 'page', 'price')
