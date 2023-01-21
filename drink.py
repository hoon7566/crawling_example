import datetime

import selenium
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver  # 셀레니움을 활성화
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from time import sleep
import openpyxl

import requests

url = "http://dailydrink.co.kr/search"

def crawling_dailydrink():
    dr = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    dr.implicitly_wait(10)  # second
    dr.get(url)  # 드라이버를 통해 url의 웹 페이지를 오픈
    a = dr.find_element(By.CLASS_NAME, 'list_more_btn').find_element(By.TAG_NAME, 'span')
    try:
        for i in range(100):
            a.click()
            sleep(1)
    except selenium.common.exceptions.StaleElementReferenceException:
        print('get end')

    html = BeautifulSoup(dr.page_source, 'html.parser')
    drink_list = html.select('div.search__list_div li.tb_body')
    print(len(drink_list))
    drink_data = []
    drink_index = []
    drink_header = ['날짜', '제품명', '발매', '종류', '도수', '캐스크번호', '판매 상점/온라인', '결제', '가격', ]
    for i in range(len(drink_list)):
        date = drink_list[i].select_one('li.date span').text
        name = drink_list[i].select_one('li.name span').text
        made_year = drink_list[i].select_one('li.made_year span').text
        type = drink_list[i].select_one('li.type span').text
        percentage = drink_list[i].select_one('li.percentage span').text
        cask_number = drink_list[i].select_one('li.cask_number span').text
        shop = drink_list[i].select_one('li.shop span').text
        p_type = drink_list[i].select_one('li.p_type span').text
        price = drink_list[i].select_one('li.price span').text
        drink_index.append(date)
        drink_data.append([date, name, made_year, type, percentage, cask_number, shop, p_type, price])

    pd.DataFrame(drink_data, columns=drink_header).to_csv('./test.csv', index=False)


if __name__ == '__main__':
    crawling_dailydrink()
