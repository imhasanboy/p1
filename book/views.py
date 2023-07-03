from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import BookModel, AuthorModel
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer
# Create your views here.
from rest_framework import status


class BookView(APIView):

    def get(self, request, *args, **kwargs):
        book = BookModel.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)


class DetailBookView(APIView):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(BookModel, pk=kwargs['book_id'])
        serializer = BookSerializer(book)
        return Response(serializer.data)


class CreateBookView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UpdateBookView(APIView):
    def patch(self, request, *args, **kwargs):
        instance = get_object_or_404(BookModel, pk=kwargs['book_id'])
        serializer = BookSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteBookView(APIView):
    def delete(self, request, *args, **kwargs):
        deleter = get_object_or_404(BookModel, pk=kwargs['book_id'])
        deleter.delete()
        return Response({'massage': 'success'}, status=status.HTTP_204_NO_CONTENT)


class AuthorView(APIView):

    def get(self, request, *args, **kwargs):
        book = AuthorModel.objects.all()
        serializer = AuthorSerializer(book, many=True)
        return Response(serializer.data)


class DetailAuthorView(APIView):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(AuthorModel, pk=kwargs['author_id'])
        serializer = AuthorSerializer(book)
        return Response(serializer.data)


class CreateAuthorView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UpdateAuthorView(APIView):
    def patch(self, request, *args, **kwargs):
        instance = get_object_or_404(AuthorModel, pk=kwargs['author_id'])
        serializer = AuthorSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAuthorView(APIView):
    def delete(self, request, *args, **kwargs):
        deleter = get_object_or_404(AuthorModel, pk=kwargs['author_id'])
        deleter.delete()
        return Response({'massage': 'success'}, status=status.HTTP_204_NO_CONTENT)
