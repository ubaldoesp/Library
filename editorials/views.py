from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Editorial
from .serializers import EditorialSerializer
from Library.permissions import AllPermissions
# Create your views here.

class EditorialViewSet(ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    permission_classes = (AllPermissions,)
    

