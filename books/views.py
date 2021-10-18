from django.db.models import query
from django.http import request
from django.shortcuts import render
from copy import copy
from rest_framework import  status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from books.serializers import BookSerializer, CreateBookSerializer, \
EditorialSerializer
from autors.serializers import AutorSerializer
from Library.permissions import AllPermissions
from books.models import Autor, Editorial, Book

# Create your views here.


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllPermissions,)
    
    def create(self, request, *args, **kwargs):
        request_data = copy(request.data)
        serializer = self.get_serializer_class()
        #print(f'Libro data: {request_data}')
        serialized = serializer(data=request_data)
        if not serialized.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serialized.errors)
        serialized.save()
        return Response(status=status.HTTP_201_CREATED,
                        data=serialized.data)
    
    def get_queryset(self):
        data ={}
        for k,v in self.request.query_params.items():
            if k in ['page','limit','offset']:
                continue
        return self.queryset.filter(**data)
    
    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return CreateBookSerializer
    #     if self.request.method == 'GET':
    #         return BookSerializer


    
    @action(methods=['GET','POST','PUT','PATCH','DELETE'],detail=True)
    def autors(self,request,pk):
        book = self.get_object()
        
        if request.method in 'GET':
            autors = book.autor.all()
            serializer = AutorSerializer(autors,many=True)
            return Response(status=status.HTTP_200_OK,data=serializer.data)   
        
        if request.method in  ['POST','PUT','PATCH']:
            autors_ids = request.data['autors'] 
            autors = Autor.objects.filter(id_in=autors_ids)
            print(autors)
            book.autor.set(autors) 
            return Response(status=status.HTTP_200_OK)
        
        if request.method == 'DELETE':
            autors_ids_delete = request.data['autors']
            for autor_id in autors_ids_delete :
                autor_get = Autor.objects.get(id=autor_id)
                book.autor.remove(autor_get)
            return Response(status=status.HTTP_200_OK)
    

    
    @action(methods=['GET','POST','DELETE','PUT','PATCH'],detail=True)
    def editorial(self,request,pk):
        book = self.get_object()
        
        if request.method == 'GET':
            serialized = EditorialSerializer(book.editorial)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            ) 
        if request.method in ['POST','PUT','PATCH']:
            editorial = Editorial.objects.get(id=request.data['editorial'])
            book.editorial = editorial
            book.save()
            return Response(status=status.HTTP_200_OK)
        
        if request.method == 'DELETE':
            book.editorial = None
            book.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        