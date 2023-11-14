from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class author(models.Model):
    name=models.CharField(max_length=50)
    birth_date=models.DateField()
    biography=models.TextField(max_length=500)
    
    def __str__(self) -> str:
        return self.name
    
    
class book(models.Model):
    title=models.CharField(max_length=50)
    name=models.OneToOneField(author,on_delete=models.CASCADE,related_name='Book_Author',null=True,blank=True)
    publish_date=models.DateTimeField()
    price=models.IntegerField()
    slug=models.SlugField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.title    
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(book, self).save(*args, **kwargs) # Call the real save() method
    
    
    
class review(models.Model):
    name=models.ForeignKey(book,on_delete=models.CASCADE,related_name='Book_Review')
    reviewer_name=models.CharField(max_length=50)
    content=models.TextField(max_length=500)
    rating=models.IntegerField()
    
    def __str__(self) -> str:
        return self.reviewer_name