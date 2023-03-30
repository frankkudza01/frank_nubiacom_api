from django.db import models
from django.utils import timezone

# Create your models here.

# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Post(models.Model):
    title=models.CharField(max_length=500)
    description=models.TextField()
    content=models.TextField()
    date_posted=models.DateField(default=timezone.now)
    category=models.CharField(max_length=100, default="Education")
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    
