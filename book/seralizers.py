from rest_framework import serializers
from .models import Book,Author,Review

#book serializers
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = '__all__' 

#author serializers
class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields= '__all__'
        
#review serializers      
class RewviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review 
        fields= '__all__'