from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=500)
    description=models.TextField()
    content=models.TextField()
    date_posted=models.DateField(default=timezone.now)
    category=models.CharField(max_length=100, default="Education")
