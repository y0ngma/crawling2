import requests
import pyautogui
import pandas as pd
import datetime, time
import os, shutil, glob, sys
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver import generate_chrome
import re
import csv



if __name__=="__main__":
    DOWNLOAD_DIR = "C:/DOWNLOAD/crawling_data/datalab"
    PROJECT_DIR = str( os.path.dirname(os.path.abspath(__file__)) )
    driver_path = f'{PROJECT_DIR}/lib/webDriver/' # driver_path에 크롬드라이버를 넣어둔다
    start_time = datetime.datetime.today()

    platform = sys.platform
    if platform == 'win32': driver_path += 'chromedriverWindow'
    elif platform == 'darwin': driver_path += 'chromedriverMac'
    elif platform == 'linux': driver_path += 'chromedriverLinux'
    else: raise Exception()
    print('{:=<80}'.format(f'=== current sys info : {platform} '))
    print('{:=<80}'.format(f'=== chromedriver dir : {driver_path} '))
    print("{:=<80}".format(f'=== crawling csv dir : {DOWNLOAD_DIR} '))


    # 크롬 드라이버 인스턴스 생성
    chrome = generate_chrome( driver_path=driver_path, headless=False, download_path=DOWNLOAD_DIR )
    
    small_lap = 0.2
    mid_lap   = 0.5
    big_lap   = 4
    url = 'https://datalab.visitkorea.or.kr/datalab/portal/loc/getAreaDataForm.do'
    chrome.get(url)
    time.sleep(big_lap)

    # Click the select location btn
    elm = chrome.find_element_by_css_selector('#area-select')
    elm.send_keys(Keys.ENTER)
    time.sleep(mid_lap)

    # For loop of all sido btn
    sido_group = chrome.find_element_by_xpath('//*[@id="popup1"]/div[2]/div[1]/div')
    sidos = sido_group.find_elements_by_xpath('.//*/*')
    for sido in sidos[:-1]:
        sido.click()
        time.sleep(small_lap)
        # For loop of all sigungu btn
        sigungus = chrome.find_elements_by_xpath('//*[@id="popup1"]/div[2]/div[2]/div/*/*')
        for sigungu in sigungus:
            sigungu.click()
            time.sleep(small_lap)
            # Click inquiry btn and wait for loading
            elm = chrome.find_element_by_css_selector('#popup1 > div.modal-foot > div > a.button.bg-blue.modal-close')
            elm.click()
            time.sleep(big_lap)

            # # Click year btn at the top of the calandar(default is current year, 2022)
            # start_months = chrome.find_element_by_xpath('//*[@id="MonthPicker_monthStart"]/div[1]/table/tbody/tr/td[2]/a/span')
            # # Click year btn on the calandar (2016-2027, 3x4 number of buttons)
            # start_months = chrome.find_element_by_xpath('//*[@id="MonthPicker_monthStart"]/div[2]/table/tbody/tr[1]/td[3]/a/span')

            # Click month btn on the calandar (1-12, 3x4 number of buttons)
            # start_months = chrome.find_element_by_xpath('')
            # start_months = chrome.find_element_by_xpath('//*[@id="MonthPicker_monthStart"]/div[2]/table/tbody/tr[2]/td[1]/a')
            # start_months = chrome.find_element_by_xpath('//*[@id="MonthPicker_monthEnd"]/div[2]/table/tbody/tr[4]/td[3]/a')

            start_month_input = 1
            end_month_input   = 3
            start_months      = chrome.find_elements_by_xpath('//*[@id="MonthPicker_monthStart"]/div[2]/table/tbody/*/*')
            end_months        = chrome.find_elements_by_xpath('//*[@id="MonthPicker_monthEnd"]/div[2]/table/tbody/*/*')
            start_month_btn   = start_months[start_month_input-1]
            end_month_btn     = end_months[end_month_input-1]

            # Click start date input btn(drop down pop up window)
            set_start_date = chrome.find_element_by_xpath('//*[@id="monthStart"]')
            set_start_date.click()
            time.sleep(mid_lap)

            # Click previous/next year btn at the top of the calandar(default is current year, 2022)
            previous_year_btn = chrome.find_element_by_xpath('//*[@id="MonthPicker_monthStart"]/div[1]/table/tbody/tr/td[1]/a')
            previous_year_btn.click()
            time.sleep(mid_lap)

            # Click start month btn
            start_month_btn.click()
            time.sleep(mid_lap)
            print(f'시작일 설정 : {start_month_input}월')

            # Click end date input btn(drop down pop up window)
            set_end_date = chrome.find_element_by_xpath('//*[@id="monthEnd"]')
            set_end_date.click()
            time.sleep(mid_lap)
            
            # Click end month btn
            end_month_btn.click()
            time.sleep(mid_lap)
            print(f'종료일 설정 : {end_month_input}월')
            
            # Click inquiry btn
            inquiry_date = chrome.find_element_by_xpath('//*[@id="searchWrap"]/div[1]/input')
            inquiry_date.click()
            time.sleep(big_lap)

            
            # After all crawling, click the select location btn
            elm = chrome.find_element_by_css_selector('#area-select')
            elm.send_keys(Keys.ENTER)
            time.sleep(mid_lap)
            
            break
        break

    time.sleep(mid_lap)
    # elm.click()

    
    """
    (1,1), (1,2), (1,3)
    (2,1), (2,2), (2,3)
    (3,1), (3,2), (3,3)
    (4,1), (4,2), (4,3)
    """
    tmp = list()
    for i in range(1,5):
        for j in range(1,4):
            tmp.append([i,j])
        # print(tmp)
        # tmp = list()
    inputdate = 5
    print(tmp[inputdate-1])