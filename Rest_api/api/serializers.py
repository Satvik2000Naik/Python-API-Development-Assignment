from rest_framework import fields, serializers
from rest_framework.utils import model_meta
from .models import external_books

class bookSerializer(serializers.ModelSerializer):


    class Meta:
        model = external_books
        feilds = '__all__'