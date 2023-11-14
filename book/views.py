from django.shortcuts import render
from .models import book 
# Create your views here.


def book(request):
    all_books=book.objects.all()
    return render(request,'book.html',{'books':all_books})
