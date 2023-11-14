from rest_framework import serializers
from .models import book,author


class bookserializer(serializers.ModelSerializer):
    class Meta:
        model= book
        fields = '__all__' 



class Authorsserializers(serializers.ModelSerializer):
    class Meta:
        model=author
        fields= '__all__'