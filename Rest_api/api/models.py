from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class external_books(models.Model):
    name = models.CharField(max_length=250)
    isbn = models.TextField()
    authors = models.CharField(max_length=250)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    release_date = models.DateField()

    def __str__(self):
        return self.name + ' ' + self.authors
    


    
