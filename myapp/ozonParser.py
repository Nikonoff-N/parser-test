import undetected_chromedriver
import time
import json
try:
    print(1)
    driver = undetected_chromedriver.Chrome(use_subprocess=True)
    #time.sleep(15)
    print(2)
    driver.get("https://seller.ozon.ru/content-api/news/?_limit=10&_start=0")
    content = driver.page_source
    #content = content.find_element_by_tag_name('pre').text
    #parsed_json = json.loads(content)
    print(content)
    time.sleep(15)
except Exception as ex:
    print("error")
    print(ex)
finally:
    driver.close()
    driver.quit()