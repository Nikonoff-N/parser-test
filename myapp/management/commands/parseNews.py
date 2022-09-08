from . import parseYandex 
from . import ozonParser
from .dbManager import *

from django.core.management.base import BaseCommand

#command module allows ass to work with db in ORM only

YANDEX_SOURCE = "yandex"
OZON_SOURCE = "ozon"

def addNews(source,news):
    '''
        base command to add news to db
    '''
    source = addSource(source)
    tags = [addTag(tag,source) for tag in news['tags']]
    article = addArticle(title= news['title'],
    source=source,
    content=news["content"],
    pub_date=news["pub_date"],
    tags = tags,
    url = news["url"]
    )    

#comand code easy to modify and extend
class Command(BaseCommand):
    def handle(self, **options):
        yandexNews = parseYandex.parseNews()[:10:]
        for news in yandexNews:
            addNews(YANDEX_SOURCE,news)
        ozonNews = ozonParser.parseNews()[:10:]
        for news in ozonNews:
            addNews(OZON_SOURCE,news)

