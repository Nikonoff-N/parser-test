from . import parseYandex 
from . import ozonParser
from .dbManager import *
#from dbManager import *

from django.core.management.base import BaseCommand
YANDEX_SOURCE = "yandex"
OZON_SOURCE = "ozon"

def addNews(source,news):
    source = addSource(source)
    tags = [addTag(tag,source) for tag in news['tags']]
    print(tags)
    article = addArticle(title= news['title'],
    source=source,
    content=news["content"],
    pub_date=news["pub_date"],
    tags = tags,
    url = news["url"]
    )    


class Command(BaseCommand):
    def handle(self, **options):
        yandexNews = parseYandex.parseNews()[:10:]
        for news in yandexNews:
            addNews(YANDEX_SOURCE,news)
        ozonNews = ozonParser.parseNews()[:10:]
        for news in ozonNews:
            addNews(OZON_SOURCE,news)

