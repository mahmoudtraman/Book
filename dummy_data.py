import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from book.models import Author,Book,Review
import random
from faker import Faker


def create_author(n):
    fake=Faker()
    for _ in range(n):
        Author.objects.create(
            name=fake.name(),
            biography=fake.text(),
            birth_date=fake.date(),
        )
    print(f"{n} Authors was added successufully")
    
  
def create_book(n):
    fake=Faker()
    for _ in range(n):
        Book.objects.create(
            title=fake.name(),
            price=random.randint(100,200),
            publish_date= fake.date(),
        )  
    print(f"{n} Books was added successufully")  
      

def create_review(n):
    fake=Faker()
    
    for _ in range(n):
        Review.objects.create(
            book=Book.objects.all().order_by('?')[0],
            reviewer_name=fake.name(),
            content=fake.text(),
            rating=random.randint(1,5),
        )        
    print(f"{n} Reviews was added successufully")     


  
        
        
#create_author(50)
#create_book(100)
create_review(150)
