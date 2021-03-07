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

from selenium.webdriver.Chrome.options import options
import json

option = options()
option.headless = True

# Tests section: Testing Selenium functions

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()


url1 = "https://finance.yahoo.com/quote/MGLU3.SA/key-statistics?p=MGLU3.SA"



