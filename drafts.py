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