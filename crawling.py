import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  # 설정 모듈 경로를 수정합니다.
django.setup()

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from patentNotice.models import PatentNotice
import logging
from datetime import datetime

# from patentAttorneys.models import TestNotice  # Django 모델 임포트

logger = logging.getLogger("crawler")


def crawlling():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument("--single-process")
    # options.add_argument("--disable-dev-shm-usage")
    # executable_path="/home/dfx/naroo/teamp/backend_0923/chromedriver"
    # driver = webdriver.Chrome(executable_path=executable_path, options=options)

    driver = webdriver.Chrome()  # selenium webdriver 설정
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)

    # 크롤링할 웹 페이지 url 설정 후 열기
    driver.get(
        "https://www.kipo.go.kr/ko/letter/kpoLetterPgmMgmt.do?menuCd=SCD0200656&parntMenuCd2=SCD0200050"
    )  # 크롤링할 웹 페이지의 URL

    # date
    date_element = driver.find_element(By.XPATH, '//*[@class="bbs_tit"]/a')
    date_text = date_element.get_attribute("title")

    # title 링크 클릭
    title_elements = driver.find_elements(By.XPATH, '//*[@class="bbs_tit"]/a')

    for title_element in title_elements:
        title_text = title_element.text  # title 텍스트 가져오기
        title_element.click()

        # 새 탭으로 전환
        driver.switch_to.window(driver.window_handles[-1])

        image = driver.find_element(By.TAG_NAME, "img")
        image_jpg = image.get_attribute("src")
        
        # 이미지 url 크롤링
        image_element = driver.find_element(By.TAG_NAME, "img")
        image_url = image_element.get_attribute("src")

        # 데이터베이스에 저장
        news = PatentNotice(title=title_text, image=image_jpg, image_url=image_url, date=date_text)
        news.save()

        # 이전 탭으로 전환
        driver.switch_to.window(driver.window_handles[0])

    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')

    # # 정책소식지 항목 추출
    # news_elements = soup.find_all('tr')
    # for news_element in news_elements:
    #     title_element = news_element.find('td', class_='bbs_tit')
    #     if title_element:
    #         title_link = title_element.find('a')
    #         title = title_link.text.strip()
    #         image_url = news_element.find('td', string='대변인').text.strip()
    #         date = news_element.find('td', class_='bbs_date').text.strip()

    #         # 데이터베이스에 저장
    #         TestNotice.objects.create(title=title, image_url=image_url, date=date)


if __name__ == "__main__":
    crawlling()
