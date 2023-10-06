# import calendar
# year = 2023
# month  = 3
# x = calendar.month(year,month)
# print(x)


import selenium
import time
import webdriver_manager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# To make it work on older versions
# of chrome we will use ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com')

# We can use any one of the ele to locate the element
ele = driver.find_element_by_xpath(
	'/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input').click()

ele = driver.find_element_by_css_selector(
	'#tsf > div:nth-child(2) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input').click()

ele = driver.find_element_by_name('q').click()
ele = driver.find_element_by_class_name('gLFyf gsfi').click()
