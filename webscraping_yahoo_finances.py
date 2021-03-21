"""
Webscraping from yahoo finances

Author: Lincoln Wallace
date: 07/03/2021
"""

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

import json

# option = options()
# option.headless = True

# Tests section: Testing Selenium functions
################################################################################################################

driver =  webdriver.Chrome(executable_path=r"..\Finances_project\Web_Scraping_For_Finances\chromedriver.exe")
driver.get('http://www.google.com/')
time.sleep(3) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('We Are The Champions')
search_box.submit()
time.sleep(10) # Let the user actually see something!  
driver.quit()

'''
###################################################################################################################

url1 = "https://finance.yahoo.com/quote/MGLU3.SA?p=MGLU3.SA&.tsrc=fin-srch"

print("Tudo Okay")

driver =  webdriver.Chrome(executable_path=r"..\Finances_project\Web_Scraping_For_Finances\chromedriver.exe")
driver.get(url1)
time.sleep(6)

path = "//div[@id='Lead-4-QuoteNav-Proxy']//section//div//ul//li[class='IbBox Fw(500) fin-tab-item H(44px) desktop_Bgc($hoverBgColor):h desktop-lite_Bgc($hoverBgColor):h  selected']//a[@class='Lh(44px) Ta(c) Bdbw(3px) Bdbs(s) Px(12px) C($linkColor) Bdbc($seperatorColor) D(b) Td(n) selected_Bdbc($linkColor) selected_C($primaryColor) selected_Fw(b)']//span"

driver.find_element_by_xpath(path).click()

driver.quit()

'''


