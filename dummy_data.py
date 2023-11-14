import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from book.models import author,book,review
import random
from faker import Faker


def create_author(n):
    fake=Faker()
    for _ in range(n):
        author.objects.create(
            name=fake.name(),
            biography=fake.text(),
            birth_date=fake.date(),
        )
    print(f"{n} Authors was added successufully")
    
  
def create_book(n):
    fake=Faker()
    for _ in range(n):
        book.objects.create(
            title=fake.name(),
            price=random.randint(100,200),
            publish_date= fake.date(),
        )  
    print(f"{n} Books was added successufully")  
      

def create_review(n):
    fake=Faker()
    
    for _ in range(n):
        review.objects.create(
            name=book.objects.all().order_by('?')[0],
            reviewer_name=fake.name(),
            content=fake.text(),
            rating=random.randint(1,5),
        )        
    print(f"{n} Reviews was added successufully")     


  
        
        
#create_author(50)
#create_book(100)
create_review(50)
