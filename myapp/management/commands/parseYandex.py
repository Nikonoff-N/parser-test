import httpx
from bs4 import BeautifulSoup
from datetime import datetime
#print(r.content)
#print(r.json())

BASE_URL = "https://market.yandex.ru"

def parseNews()->list:
    r = httpx.get('https://market.yandex.ru/partners/api/news-more/news')
    result = [{"url":BASE_URL+news['url'],
        "title":news['approvedTitle'].replace("&nbsp;"," "),
        "pub_date":datetime.strptime(news['date'],"%Y-%m-%dT%H:%M:%S%z"),
        "tags":[t['displayName'] for t in news['tags']],
        "content":parseNewsPage(BASE_URL+news['url'])
        } for news in r.json()]

    return result



def parseNewsPage(url)->str:
    r = httpx.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    result = soup.find("div",itemprop="articleBody")
    return result

if __name__ == "__main__":
    print("hello")
    results = parseNews()
    print(results)