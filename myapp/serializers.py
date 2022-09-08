from rest_framework import routers, serializers, viewsets
from .models import *

#data serializers for each model

class ArticleSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSource
        fields = ['name',]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['text',]

class ArticleSerializer(serializers.ModelSerializer):
    #this one refeerences othor models s it has some custom fields
    tags = TagSerializer(read_only=True, many=True)
    source = ArticleSourceSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ['title', 'content', 'source', 'pub_date','tags',"url"]



