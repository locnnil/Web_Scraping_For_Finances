"""
Webscraping from yahoo finances

Author: Lincoln Wallace
date: 07/03/2021
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

url = []

url =   ['http://www.google.com/',
         'https://fiis.com.br/',
         'https://finance.yahoo.com/',
         '',
         ''
        ]

fiis =  ['MXRF11',
         'HLGL11',
         '',
         '',
         '',
         ''
        ]

# Location off Chrome driver
PATH = "..\Finances_project\chromedriver.exe" 
driver =  webdriver.Chrome(PATH)

driver.get(url[1])
time.sleep(2) # Stop to user see something!


id = "main-search"

search_icon = driver.find_element_by_id(id)
search_icon.click()


search.send_keys(fiis[0])
search_box.submit()

time.sleep(3)
driver.quit()


"""
# OBS:
To access elements in a HTML code we normaly have: ID -> NAME -> CLASS_NAME

<input type="text" name="search_keyword" id="main-search--keyword" autocomplete="off">
"""



