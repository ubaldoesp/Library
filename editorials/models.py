from django.db import models

# Create your models here.
class Editorial(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=50)
    web_page = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name