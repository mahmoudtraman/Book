from django.contrib import admin
from .models import author,book,review
# Register your models here.


class book_Admin(admin.ModelAdmin):
    list_display=['title','publish_date','price']
    search_fields=['title','price']
    list_filter=['publish_date','price']
    
    
class Review_Admin(admin.ModelAdmin):
    list_display=['reviewer_name','rating']
    search_fields=['rating','name']
    list_filter=['rating','reviewer_name']    
    
    

admin.site.register(book,book_Admin)
admin.site.register(author)
admin.site.register(review,Review_Admin)