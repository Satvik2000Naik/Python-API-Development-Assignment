from django.contrib import admin

from api.models import external_books

# Register your models here.
from .models import external_books
admin.site.register(external_books)
