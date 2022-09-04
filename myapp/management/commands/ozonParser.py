import undetected_chromedriver
import httpx
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json
BASE_URL = "https://seller.ozon.ru/news/"



def getDataFromApi(driver):
    try:
        #driver = undetected_chromedriver.Chrome(use_subprocess=True)
        driver.get("https://seller.ozon.ru/content-api/news/?_limit=10&_start=0")
        content = driver.page_source
        #content = content.find_element_by_tag_name('pre').text
        #parsed_json = json.loads(content)
        #time.sleep(15)
    except Exception as ex:
        print("error")
        print(ex)
    finally:
        # driver.close()
        # driver.quit()
        soup = BeautifulSoup(content,"html.parser")
        data = soup.find("pre")
        results = json.loads(str(data.contents[0]))
        return results

def parseNewsPage(driver,url)->str:
    results = ""
    try:
        # driver = undetected_chromedriver.Chrome(use_subprocess=True)
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content,"html.parser")
        print("got it")
        #print(soup.prettify())
        results = soup.find("section",class_="new-section html-content_Ol8P9")
    except Exception as ex:
        print("error")
        print(ex)
    finally:
        # driver.close()
        # driver.quit()
        return results

# def parseNews()->list:
#     r = httpx.get('https://market.yandex.ru/partners/api/news-more/news')
#     result = [{"url":BASE_URL+news['url'],
#         "title":news['approvedTitle'].replace("&nbsp;"," "),
#         "pub_date":datetime.strptime(news['date'],"%Y-%m-%dT%H:%M:%S%z"),
#         "tags":[t['displayName'] for t in news['tags']],
#         "content":parseNewsPage(BASE_URL+news['url'])
#         } for news in r.json()]

#     return result

def parseNews()->list:
    driver = undetected_chromedriver.Chrome(use_subprocess=True)
    data = getDataFromApi(driver)
    result = [{
        "url":BASE_URL+news['slug'],
        'title':news['title'],
        #'pub_date':datetime.strptime(news['date'],"%Y-%m-%dT%H:%M:%S.%zZ"),
        'pub_date':datetime.fromisoformat(news['date'][:-1] + '+00:00'),
        "tags":[t['name'] for t in news['theme']],
        "content":parseNewsPage(driver,BASE_URL+news['slug'])}
        for news in data]
    driver.close()
    driver.quit()
    return result
    
if __name__ == "__main__":
    print(parseNews())

    
    