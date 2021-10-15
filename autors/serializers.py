from django.db import models
from rest_framework.serializers import ModelSerializer
from .models import Autor

class AutorSerializer(ModelSerializer):
    
    class Meta:
        model = Autor
        fields = '__all__'