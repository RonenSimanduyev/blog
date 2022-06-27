from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    imageUrl=models.CharField(max_length=400,blank=True)
    body=models.TextField()
    created=models.DateField(auto_now_add=True)