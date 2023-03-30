from django.db import models

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return f'Tag[id: {self.id}, name: {self.name}]'
