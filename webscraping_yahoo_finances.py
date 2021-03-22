"""
Webscraping from yahoo finances

Author: Lincoln Wallace
date: 07/03/2021
file: webscraping_yahoo_finances.py
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

#option = options()
#option.headless = True
# Tests section: Testing Selenium functions

url =   ['http://www.google.com/',
         'https://fiis.com.br/',
         'https://finance.yahoo.com/',
         '',
         ''
        ]

urlfiis = 'https://fiis.com.br/'

fiis =  ['XPLG11',
         'MXRF11',
         'HGLG11',
         'XPML11',
         'BCFF11',
         'RECT11',
         'HFOF11',
         'HSML11',
         'HTMX11',
         'KNIP11',
        ]

# Location off Chrome driver
PATH = "..\Finances_project\chromedriver.exe"


# open fiis pages
for i in range(len(fiis)):

        # open a new window
        driver =  webdriver.Chrome(PATH)
        driver.get(urlfiis+fiis[i])
        driver.implicitly_wait(10) # seconds # Stop to user see something!
        try:
                # Close adds about ebook
                element = WebDriverWait(driver,20).until(
                        EC.presence_of_element_located((By.ID,"popup-x"))
                        )
                element.click()
        except:
                print("Deu ruim em fechar o anuncio")
        time.sleep(3)
        driver.close()

# search_icon = driver.find_element_by_id(id) 
# search_icon.click()

# search.send_keys(fiis[0])
# search_box.submit()


"""
# OBS:
To access elements in a HTML code we normaly have: ID -> NAME -> CLASS_NAME

<input type="text" name="search_keyword" id="main-search--keyword" autocomplete="off">
"""



