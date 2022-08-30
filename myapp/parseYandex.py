import httpx

#print(r.content)
#print(r.json())


def parseNews()->list:
    r = httpx.get('https://market.yandex.ru/partners/api/news-more/news')
    for new in r.json():
        url = new['url']
        print(new.keys())
        print(new['approvedTitle'])
        print(new['approvedPreview'])
        for tag in new['tags']:
            print(tag['displayName'])