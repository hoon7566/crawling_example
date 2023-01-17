import datetime
from bs4 import BeautifulSoup
import urllib.request


def print_weather():
    print('#오늘의 #날씨 #요약 \n')
    webpage = urllib.request.urlopen(
        'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')
    soup = BeautifulSoup(webpage, 'html.parser')
    temps = soup.find('p', "summary")
    cast = soup.find('span')
    print('오늘 날씨 : ', temps.get_text(), '℃', cast.get_text())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_weather()

