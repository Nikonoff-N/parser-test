from datetime import datetime
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone
from datetime import datetime,timedelta
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
TZ = timezone.get_current_timezone()

# Create your views here.
def index(request):
    template = loader.get_template('myapp/index.html')
    articles = Article.objects.all()

    context = {"articles":articles}
    return HttpResponse(template.render(context, request))

def details(request,articleId):
    template = loader.get_template('myapp/details.html')
    article = Article.objects.get(pk = articleId)

    context = {"article":article}
    return HttpResponse(template.render(context, request))

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('index', args=()))


class ArticleList(APIView):
    """
    List all articles or get article by date
    """
    #@swagger_auto_schema(responses={200: ArticleSerializer(many=True)})

    def get(self, request, format=None):
        snippets = Article.objects.all()
        serializer = ArticleSerializer(snippets, many=True)
        return Response(serializer.data)

class ArticleByDate(APIView):

    def get(self, request,date = None, format=None):
        print(date)
        fixed_date = datetime.strptime(date,"%Y-%m-%d")
        fixed_date = fixed_date.replace(tzinfo=TZ)
        snippets = Article.objects.filter(pub_date__range=[fixed_date,fixed_date+timedelta(days=1)])
        print(snippets.count())
        serializer = ArticleSerializer(snippets, many=True)
        return Response(serializer.data)

class ArticleByTag(APIView):

    def get(self, request, tag = None, format=None):
        #tag = self.kwargs['tag']
        print(tag)
        tag = Tag.objects.get(text = tag)
        print(tag)
        snippets = Article.objects.filter(tags = tag)
        serializer = ArticleSerializer(snippets, many=True)
        return Response(serializer.data)

class TagList(APIView):
    """
    List all tags
    """
    @swagger_auto_schema()
    def get(self, request, format=None):
        snippets = Tag.objects.all()
        serializer = TagSerializer(snippets, many=True)
        return Response(serializer.data)

class SourceList(APIView):
    """
    List all tags
    """
    @swagger_auto_schema()
    def get(self, request, format=None):
        snippets = ArticleSource.objects.all()
        serializer = ArticleSourceSerializer(snippets, many=True)
        return Response(serializer.data)