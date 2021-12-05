from django.shortcuts import get_object_or_404
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import external_books
from .serializers import bookSerializer

class bookList(APIView):

    def get(self , request):
        books = external_books.objects.all()
        serializer = bookSerializer(books , many = True)
        return Response(serializer.data)
