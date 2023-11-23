from django.urls import path
from .views import BookDetailAPI,CreateListBookApiView,AuthorListAPI,AuthorDetailAPI

urlpatterns = [
      path('api/listbook',CreateListBookApiView.as_view()),
      path('api/listbook/<int:pk>',BookDetailAPI.as_view()),
    
      path('api/listauthor',AuthorListAPI.as_view()),
      path('api/listauthor/<int:pk>',AuthorDetailAPI.as_view()),
    
]