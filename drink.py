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
import sys, os
import openpyxl

import requests

drink_url = "http://dailydrink.co.kr/search"


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def get_exe_file_path():
    # print('bundle dir is', os.path.abspath(__file__))
    # print('sys.argv[0] is', sys.argv[0])
    # print('sys.executable is', sys.executable)
    # print('os.getcwd is', os.getcwd())

    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        # bundle_dir = sys._MEIPASS
        exe_dir = sys.argv[0]
    else:
        # we are running in a normal Python environment
        exe_dir = os.path.dirname(os.path.abspath(__file__))
    return exe_dir


def crawling_dailydrink():
    dr = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print('open chrome')

    drink_path = get_exe_file_path()
    dr.implicitly_wait(10)  # second
    dr.get(drink_url)  # 드라이버를 통해 url의 웹 페이지를 오픈
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

    create_folder(drink_path)
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
    print(get_exe_file_path())

    pd.DataFrame(drink_data, columns=drink_header).to_csv(drink_path + '/test.csv', index=False)


if __name__ == '__main__':
    crawling_dailydrink()
