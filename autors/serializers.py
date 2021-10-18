from django.db import models
from rest_framework.serializers import ModelSerializer
from autors.models import Autor

class AutorSerializer(ModelSerializer):
    
    class Meta:
        model = Autor
        fields = ('name','age','date_of_birth')