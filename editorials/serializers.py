from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Editorial

class EditorialSerializer(ModelSerializer):
    
    class Meta:
        model = Editorial
        fields = ('name', 'web_page')
    
class CreateEditorialSerializer(ModelSerializer):
    
    class Meta:
        model = Editorial
        fields = ('name','mail','web_page')
        