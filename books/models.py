from django.db import models
from django.contrib.auth.models import User
from autors.models import Autor
from editorials.models import Editorial
# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField(null=True)
    published = models.BooleanField(default=True)
    publication_date = models.DateField(null=True)
    edition = models.IntegerField(null=True)
    editorial = models.ForeignKey(
        Editorial,
        on_delete= models.SET_NULL,
        null=True
    )
    autor = models.ManyToManyField(
        Autor,
        related_name='books'
    )
    user = models.ForeignKey(
        User, 
        on_delete= models.SET_NULL,
        null=True
    )
    date_creation= models.DateTimeField(auto_now=True)
    date_updated= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    