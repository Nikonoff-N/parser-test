import httpx
from bs4 import BeautifulSoup
from datetime import datetime


BASE_URL = "https://market.yandex.ru"

def parseNews()->list:
    '''parses news from yandex'''
    r = httpx.get('https://market.yandex.ru/partners/api/news-more/news')
    result = [{"url":BASE_URL+news['url'],#url from slug field
        "title":news['approvedTitle'].replace("&nbsp;"," "),
        "pub_date":datetime.strptime(news['date'],"%Y-%m-%dT%H:%M:%S%z"),#parse time from iso
        "tags":[t['displayName'] for t in news['tags']],#list of tags
        "content":parseNewsPage(BASE_URL+news['url'])#go to dedicated news page
        } for news in r.json()]# repeat for all news

    return result



def parseNewsPage(url)->str:
    ''' go to page, parse it, simple'''
    r = httpx.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    result = soup.find("div",itemprop="articleBody")
    return result

if __name__ == "__main__":
    #test it
    print("hello")
    results = parseNews()
    print(results)