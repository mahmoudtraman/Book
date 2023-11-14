from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import generics
from .seralizers import bookserializer,Authorsserializers
from .models import book,author




class booklistapi(generics.ListAPIView):
    queryset=book.objects.all()
    serializer_class=bookserializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['title','publish_date','price']
    search_fields =['title','price','name']
    ordering_fields =['price']
    permission_classes = [IsAuthenticated]
    

class bookdetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=book.objects.all()
    serializer_class=bookserializer  
    
    
    
    
class Authorlistapi(generics.ListAPIView):
    queryset=author.objects.all()
    serializer_class=Authorsserializers
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['name','birth_date','biography']
    search_fields =['name']
    permission_classes = [IsAuthenticated]
    

class Authordetailapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=author.objects.all()
    serializer_class=Authorsserializers  