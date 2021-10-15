from django.db import models

# Create your models here.
class Autor(models.Model):
    name= models.CharField(max_length=100)
    age= models.PositiveIntegerField(default=0)
    date_of_birth= models.DateField(null=True)
    date_creation= models.DateTimeField(auto_now=True)
    date_updated= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    