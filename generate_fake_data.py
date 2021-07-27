"""
Generating Fake Data for Statistics Linear Corelation

Author: Lincoln Wallace
date: 27/07/2021
file: generate_fake_data.py
"""

import json
import time
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://forms.gle/s9z9TuPMSW278hVP6"

# Location off Chrome driver
PATH = "..\Finances_project\chromedriver.exe"

# open a new window
# OBS: necessary to correct, for better optimization in this part of code
driver = webdriver.Chrome(PATH)
driver.get(url)
driver.implicitly_wait(3)  # seconds # Stop to user see something!



