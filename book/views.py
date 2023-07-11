from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import BookModel, AuthorModel
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer
# Create your views here.
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class BookView(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_class = (IsAuthenticated,)


class DetailBookView(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


class CreateBookView(generics.CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


class UpdateBookView(generics.RetrieveUpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


class DeleteBookView(generics.DestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer


class AuthorView(generics.ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class DetailAuthorView(generics.RetrieveAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class CreateAuthorView(generics.CreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class UpdateAuthorView(generics.RetrieveUpdateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class DeleteAuthorView(generics.DestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
