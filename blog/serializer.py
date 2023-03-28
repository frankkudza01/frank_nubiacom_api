from rest_framework import serializers
from bog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=["id","title","description","content","date_posted","category"]