from django.urls import path
from .api import booklistapi,bookdetailapi,Authorlistapi,Authordetailapi
from .views import  book

urlpatterns = [
    path('api/listbook',booklistapi.as_view()),
    path('api/listbook/<int:pk>',bookdetailapi.as_view()),
    path('api/listauthor',Authorlistapi.as_view()),
    path('api/listauthor/<int:pk>',Authordetailapi.as_view()),
]