from datetime import datetime
from .models import *

def addSource(name:str)->ArticleSource:
    try:
        s = ArticleSource.objects.get(name = name)
        print("source alredy exists")
    except:
        s = ArticleSource(name = name)
        s.save()
        print(f"source {name} created")
        return s

def addTag(name:str,source:ArticleSource)->Tag:
    try:
        s = Tag.objects.get(name = name,source = source)
        print(f"Tag {name} alredy exists")    
    except:
        t = Tag(name = name,source = source)
        t.save()
        print(f"Tag {name} created")
        return t

def addArticle(title:str,source:ArticleSource,content:str,pub_date:datetime,tags:list[Tag])->None:
    try:
        a = Article.objects.get(title = title,source = source)
        print(f"Article {title} alredy exists")  
    except:
        a = Article(title = title,source = source,content= content,pub_date=pub_date)
        a.save()
        a.tags.add(*tags)
        a.save()
        print(f"Article {title} created")
