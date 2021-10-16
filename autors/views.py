from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Autor
from .serializers import AutorSerializer
from Library.permissions import AllPermissions

# Create your views here.
# Create crud simple of autors

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (AllPermissions,)
    