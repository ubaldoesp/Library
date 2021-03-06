from django.db.models import fields
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from editorials.serializers import EditorialSerializer
from books.models import Book
from autors.models import Autor
class BookSerializer(ModelSerializer):
    editorial = EditorialSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'
    

class CreateBookSerializer(ModelSerializer):
    autor= PrimaryKeyRelatedField(queryset=Autor.objects.all(),many=True)
    
    class Meta:
        model = Book
        fields = '__all__'