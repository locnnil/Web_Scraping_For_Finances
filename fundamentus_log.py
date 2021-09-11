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

# Location off Chrome driver
PATH = "..\Finances_project\chromedriver.exe"
# Email for fundamentei web-site
email = "leohendrik000@gmail.com"
# Password for fundamentei web-site
password = "ILovePythonAndFinances"

url_home = "https://fundamentei.com/"

acoes = ['ITSA4',
         'WEGE3',
         'PETR4',
         ]

driver = webdriver.Chrome(PATH)
driver.get(url_home)
driver.implicitly_wait(5)

try:
    # Close adds about ebook
    element = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-7dlv7o"))
    )
    element.click()
    print()
except:
    print("Erro em clicar para logar")

try:
    # Close adds about ebook
    element = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-zbgoky"))
    )
    element.send_keys(email)
except:
    print("Erro em clicar no email e digitar")

try:
    # Close adds about ebook
    element = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    element.send_keys(password)
except:
    print("Erro em clicar na senha e digitar")

try:
    # Close adds about ebook
    element = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-1dqkbbj"))
    )
    element.click()
except:
    print("Erro ao clicar em 'logar' ")

time.sleep(1)

for i in range(len(acoes)):
    print(acoes[i])
    time.sleep(2)
    driver.get(url_home+"/br/"+acoes[i])
    try:
        # Close adds about ebook
        element = driver.find_element_by_class_name("css-1b8yuao")
        html_content = element.get_attribute('outerHTML')
        print(html_content)
    except:
        print("Erro ao Carregar tabela")

driver.quit()
    # loop to be implemented
    # Get stonks indicators



