"""
File to do tests and note some drafts

Author: Lincoln Wallace
date: 21/03/2021
"""

import json
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
print("Tudo Okay")
driver =  webdriver.Chrome(executable_path=r"..\Finances_project\Web_Scraping_For_Finances\chromedriver.exe")
driver.get(url1)
time.sleep(6)
path = "//div[@id='Lead-4-QuoteNav-Proxy']//section//div//ul//li[class='IbBox Fw(500) fin-tab-item H(44px) desktop_Bgc($hoverBgColor):h desktop-lite_Bgc($hoverBgColor):h  selected']//a[@class='Lh(44px) Ta(c) Bdbw(3px) Bdbs(s) Px(12px) C($linkColor) Bdbc($seperatorColor) D(b) Td(n) selected_Bdbc($linkColor) selected_C($primaryColor) selected_Fw(b)']//span"
driver.find_element_by_xpath(path).click()
driver.quit()
'''

'''
# Search in Google.com:
PATH = "..\Finances_project\chromedriver.exe" 
driver =  webdriver.Chrome(PATH)
driver.get('http://www.google.com/')
search_box.send_keys('We Are The Champions')
search_box.submit()
time.sleep(4) # Let the user actually see something!  
driver.quit()
'''

fiis =  ['mxrf11',
         'hglg11',
         'visc11',
         '',
         '',
        ]

PATH = "..\Finances_project\chromedriver.exe" 
driver =  webdriver.Chrome(PATH)

url = 'https://fiis.com.br/'

driver.get(url)


time.sleep(8)


try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"popup-x"))
    )
    element.click()
    element2 = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"header--search-btn"))
    )
    element2.click()
except:
    driver.quit()

search = driver.find_element_by_xpath("/html/body/div[1]")
search = driver.find_element_by_xpath("//div[1]")
search = driver.find_element_by_xpath("//div[@id='main-search']")



'''
<input type="text" name="search_keyword" id="main-search--keyword" autocomplete="off">
'''

'''
click1 = driver.find_element_by_id(id)
click1.click()
time.sleep(2)
driver.quit()
'''

