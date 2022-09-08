from datetime import datetime
from ...models import *

#this module used for db management
#prints are save as it is not supposed to be used in runtime
#only for one time use

def addSource(name:str)->ArticleSource:
    ''' adds source if doesnt exist, return source object for propper db managent'''
    try:
        s = ArticleSource.objects.get(name = name)
        print("source alredy exists")
        return s
    except:
        s = ArticleSource(name = name)
        s.save()
        print(f"source {name} created")
        return s

def addTag(text:str,source:ArticleSource)->Tag:
    ''' adds tag if doesnt exist, return tag object for propper db managent'''
    try:
        t = Tag.objects.get(text = text,source = source)
        print(f"Tag {text} alredy exists")   
        return t
    except:
        t = Tag(text = text,source = source)
        t.save()
        print(f"Tag {text} created")
        return t

def addArticle(title:str,source:ArticleSource,content:str,pub_date:datetime,tags:list[Tag],url:str)->None:
    ''' adds article if doesnt exist, return article object for propper db managent'''
    try:
        a = Article.objects.get(title = title,source = source)
        print(f"Article {title} alredy exists")
        return a
    except:
        print(f"Create new article {title}")
        #print(title,source,type(content),len(content),content,pub_date,url,sep ="\n")
        a = Article(title = title,source = source,content=str(content),pub_date=pub_date,url = url)
        a.save()
        a.tags.add(*tags)
        a.save()
        print(f"Article {title} created")
        return a
