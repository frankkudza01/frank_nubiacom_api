from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.

# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Post(models.Model):
    title=models.CharField(max_length=500)
    description=models.TextField()
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    category=models.CharField(max_length=100, default="Education")
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    tags=TaggableManager()
    
    def __str__(self):
        return self.title

    def tag_list(self):
        tags=self.tags.split(',')
        return tags