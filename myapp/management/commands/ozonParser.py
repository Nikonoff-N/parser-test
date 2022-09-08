import undetected_chromedriver
import httpx
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json
BASE_URL = "https://seller.ozon.ru/news/"



def getDataFromApi(driver):
    ''' knocks to api and fetches list of last ten news'''
    try:
        # open page
        driver.get("https://seller.ozon.ru/content-api/news/?_limit=10&_start=0")
        content = driver.page_source
        #get page content
        soup = BeautifulSoup(content,"html.parser")
        #remove fluff
        data = soup.find("pre")
        #shove into dict
        results = json.loads(str(data.contents[0]))
    except Exception as ex:
        print("error")
        print(ex)
        #catch errors
        results = ''
    finally:
        return results

def parseNewsPage(driver,url)->str:
    '''parses news using exiting driver'''
    results = ""
    try:
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content,"html.parser")
        #finds tag with news
        results = soup.find("section",class_="new-section html-content_Ol8P9")
        
    except Exception as ex:
        print("error")
        print(ex)
    finally:

        return results


def parseNews()->list:
    '''parses news from ozon'''

    #opens chrome
    driver = undetected_chromedriver.Chrome(use_subprocess=True)
    #fetch data from api
    data = getDataFromApi(driver)
    #stuct the data in list of hash tables 
    result = [{
        "url":BASE_URL+news['slug'],#url from slug field
        'title':news['title'],
        'pub_date':datetime.fromisoformat(news['date'][:-1] + '+00:00'),#parse time from iso
        "tags":[t['name'] for t in news['theme']],#list of tags
        "content":parseNewsPage(driver,BASE_URL+news['slug'])}#go to dedicated news page
        for news in data] # repeat for all news
    driver.close()#close driver
    driver.quit()# close browser
    return result
    
if __name__ == "__main__":
    #test it
    print(parseNews())

    
    