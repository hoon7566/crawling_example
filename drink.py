import datetime
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver  # 셀레니움을 활성화
from selenium.webdriver.common.by import By

import requests

url = "http://dailydrink.co.kr/search"
driver_uri = '/opt/homebrew/bin/chromedriver'
def crawling_dailydrink():
    # response = requests.post(url,data='{"type":602,"likes":[],"startPosition":0,"count":100,"filters":[],"sorts":[{"key":"buy_date","value":2},{"key":"insert_time","value":2}]}')

    dr = webdriver.Chrome(driver_uri)  # 크롬 드라이버를 실행하는 명령어를 dr로 지정
    dr.implicitly_wait(5)  # second
    dr.get(url)  # 드라이버를 통해 url의 웹 페이지를 오픈
    list = dr.find_element(By.CLASS_NAME,'search__list_div')
    print(list.text)

    # print(response.text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    crawling_dailydrink()

