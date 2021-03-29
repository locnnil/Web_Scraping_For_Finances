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

url = ['http://www.google.com/',
       'https://fiis.com.br/',
       'https://finance.yahoo.com/',
       'https://fundamentus.com.br/detalhes.php?papel=',
       ''
       ]

urlfiis = 'https://fiis.com.br/'

acoes = ['ITSA4',
         'WEGE3',
         'PETR4',
         '',
         '',
         '',
         '',
         '',
         '',
         '',
         ]

b3_completa = []

fiis = ['XPLG11',
        'MXRF11',
        'HGLG11',
        'XPML11',
        'BCFF11',
        'RECT11',
        'HFOF11',
        'HSML11',
        'HTMX11',
        'KNIP11',
        '',
        '',
        '',
        '',
        '',
        '',
        ]

# Location off Chrome driver
PATH = "..\Finances_project\chromedriver.exe"

# open fiis pages
for i in range(len(fiis)):

    # open a new window
    # OBS: necessary to correct, for better optimization in this part of code
    driver = webdriver.Chrome(PATH)
    driver.get(urlfiis + fiis[i])
    driver.implicitly_wait(10)  # seconds # Stop to user see something!
    try:
        # Close adds about ebook
        element = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.ID, "popup-x"))
        )
        element.click()
    except:
        print("Deu ruim em fechar o anuncio")
    # element = driver.find_element_by_id("informations--indexes")  # to be finished
    time.sleep(3)
    driver.close()

driver.quit()  # End of execution, closing browser

"""
# OBS:
To access elements in a HTML code we normaly have: ID -> NAME -> CLASS_NAME

<input type="text" name="search_keyword" id="main-search--keyword" autocomplete="off">
"""
