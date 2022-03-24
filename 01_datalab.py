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
            
            # Click start date btn

            # Click end date btn

            # Click inquiry btn

            
            
            # After all crawling, click the select location btn
            elm = chrome.find_element_by_css_selector('#area-select')
            elm.send_keys(Keys.ENTER)
            time.sleep(mid_lap)

    time.sleep(mid_lap)
    # elm.click()