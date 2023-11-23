from django.contrib import admin
from .models import Author,Book,Review
# Register your models here.


class book_Admin(admin.ModelAdmin):
    list_display=['title','publish_date','price']
    search_fields=['title','price']
    list_filter=['publish_date','price']
    
    
class Review_Admin(admin.ModelAdmin):
    list_display=['reviewer_name','rating']
    search_fields=['rating']
    list_filter=['rating','reviewer_name']    
    
    

admin.site.register(Book,book_Admin)
admin.site.register(Author)
admin.site.register(Review,Review_Admin)