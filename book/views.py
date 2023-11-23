from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from .seralizers import BookSerializer,AuthorSerializers,RewviewSerializer
from .models import Book,Author,Review
from rest_framework import status
from rest_framework.response import Response


ERORR_404_NotFound = {
    "status": '404 not found',
    "message": "something went error, this page not found or the object you want has been deleted"
}




class CreateListBookApiView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['title','publish_date','price']
    search_fields =['title','price']
    ordering_fields =['price']
    
class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    lookup_field='pk'
    serializer_class=BookSerializer  
    
    def get(self, request, **kwargs):
        try:
            book=Book.objects.get(id=kwargs['pk'])
        except Author.DoesNotExist:
            return Response(ERORR_404_NotFound,status=status.HTTP_404_NOT_FOUND)
        book_serializer=BookSerializer(book)
        reviews=Review.objects.filter(book=book) 
        reviews_serializer=RewviewSerializer(reviews, many=True)
        return Response({
            'book':book_serializer.data,
            'reviews':reviews_serializer.data,
        },status=status.HTTP_200_OK)
        

class AuthorListAPI(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializers
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['name','birth_date','biography']
    search_fields =[]
    
    

class AuthorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    lookup_field = 'pk'
    serializer_class=AuthorSerializers 
    
    def get(self,request, **kwargs):
        try:
            author=Author.objects.get(id=kwargs['pk'])
        except Author.DoesNotExist:
            return Response(ERORR_404_NotFound,status=status.HTTP_404_NOT_FOUND)
        author_serializer=AuthorSerializers(author)
        books=Book.objects.filter(author=author)
        book_serializer=BookSerializer(books, many=True)
        return Response({
            'Author':author_serializer.data,
            'books':book_serializer.data,
        },status=status.HTTP_200_OK)
    
    



