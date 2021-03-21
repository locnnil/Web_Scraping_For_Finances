"""
Webscraping from yahoo finances

Author: Lincoln Wallace
date: 07/03/2021
"""

# Begin Imports section

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import json

# End Import section

# Begin Testes Section

url = "https://fiis.com.br/mxrf11/"

option = Options()
option.headless = True
"""options=option"""

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=gecko+'.exe')

driver.get(url)

time.sleep(4)

driver.quit()




