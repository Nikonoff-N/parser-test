from rest_framework import routers, serializers, viewsets
from .models import *

class ArticleSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSource
        fields = ['name',]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['text',]

# Serializers define the API representation.
class ArticleSerializer(serializers.ModelSerializer):
    # source = serializers.HyperlinkedRelatedField(view_name='sourceApi',format='html',read_only=True)
    # tags = serializers.HyperlinkedRelatedField(many=True,view_name='tagApi',format='html',read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    source = ArticleSourceSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ['title', 'content', 'source', 'pub_date','tags',"url"]



