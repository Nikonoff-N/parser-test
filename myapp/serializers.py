from rest_framework import routers, serializers, viewsets
from .models import *

# Serializers define the API representation.
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    source = serializers.HyperlinkedRelatedField(view_name='sourceApi',format='html',read_only=True)
    tags = serializers.HyperlinkedRelatedField(many=True,view_name='tagApi',format='html',read_only=True)
    class Meta:
        model = Article
        fields = ['title', 'content', 'source', 'pub_date','tags',"url"]

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['source', 'text']

class ArticleSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSource
        fields = ['name',]