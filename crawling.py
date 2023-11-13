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
from selenium.webdriver.support.relative_locator import locate_with

from patentNotice.models import PatentNotice, PatentNoticeDate
import logging
from datetime import datetime

# from patentAttorneys.models import TestNotice  # Django 모델 임포트

# logger = logging.getLogger("crawler")


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
    # date_element = driver.find_element(By.XPATH, '//*[@class="bbs_tit"]/a')
    # date_text = date_element.get_attribute("title")
    # date_element = driver.find_element(By.XPATH, '//h3[@id="popTitle"]')
    # date_text = date_element.text


    # title 링크 클릭
    # title_elements = driver.find_element(By.XPATH, '//*[@class="bbs_tit"]/a')
    
    while True:
        for i in range(1, 11):
            # 공지 제목 가져오기
            try:
                driver.find_element(By.XPATH, '//*[@id="content"]/article/div[3]/table/tbody/tr[' + str(i) + ']/td[2]/a').click()
            except:
                return
            
            # 공지 내용 가져오기
            title = driver.find_element(By.XPATH, '//*[@id="popTitle"]').text
        
            # 데이터베이스에 저장
            PatentNoticeDate(title=title).save()
            
            title_date = PatentNoticeDate.objects.latest('id') # 가장 나중에 저장된 인덱스 가져오기

            # 이미지 jpg 크롤링
            # image = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[2]/td/a/img').get_attribute('src')
            
            # 이미지 url 크롤링
            # image_url = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[2]/td/a').get_attribute('href')
        
            # image = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[3]/td[1]/a/img').get_attribute('src')

            try:
                for i in (2, 7):
                    # 이미지 jpg 크롤링
                    image = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[' + str(i) + ']/td/a/img').get_attribute('src')
                    
                    # 이미지 url 크롤링
                    image_url = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[' + str(i) + ']/td/a').get_attribute('href')
                
                    # 데이터베이스에 저장
                    # date = PatentNoticeDate(title=title).save()
                    PatentNotice(title=title_date, image=image, image_url=image_url).save()
            
                for i in range(1, 3):
                    image = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[3]/td[' + str(i) + ']/a/img').get_attribute('src')
                    image_url = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[3]/td[' + str(i) + ']/a').get_attribute('href')
            
                    # 데이터베이스에 저장
                    # date = PatentNoticeDate(title=title).save()
                    PatentNotice(title=title_date, image=image, image_url=image_url).save()
            
                # image = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[7]/td/a/img').get_attribute('src')
                # image_url = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[7]/td/a').get_attribute('href')

                image = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[8]/td/table/tbody/tr/td/a/img').get_attribute('src')
                image_url = driver.find_element(By.XPATH, '//*[@id="htmlCont"]/table/tbody/tr[8]/td/table/tbody/tr/td/a').get_attribute('href')
                                                                                                                                        
                PatentNotice(title=title_date, image=image, image_url=image_url).save()
            except:
                pass
            
            # x 눌러서 공지 화면 돌아가기
            driver.find_element(By.XPATH, '//*[@id="content"]/article/div[4]/div[2]/div[1]/a').click()

        try:
            driver.find_element(locate_with(By.TAG_NAME, 'a').to_right_of({By.XPATH: '//*[@id="content"]/article/div[5]/strong'})).click()

        except:
            break
    return

    # print(title_date)
    # print(news)
    # news = PatentNotice(title=title_date, image=image, image_url=image_url)
    # news.save()
    # 새 탭으로 전환
    # driver.switch_to.window(driver.window_handles[-1])
    
    
    # 이전 탭으로 전환
    # driver.switch_to.window(driver.window_handles[0])
    
    # 다음 목록으로 이동하기
    # try:
    #     driver.find_element(
    #         locate_with(By.TAG_NAME, "a").to_right_of(
    #             {By.XPATH: '//*[@id="content"]/article/div[4]/div[2]/div[1]/a'}
    #         )
    #     ).click()
    # except:
    #     break

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
