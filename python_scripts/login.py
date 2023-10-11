from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time
from webdriver_manager.chrome import ChromeDriverManager

username = "4NI20EExyz"
password_date = DD
password_month = "MON"
password_year = YEAR

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://parents.nie.ac.in/")

username_field = browser.find_element("name", "username")
username_field.send_keys(username)

password_date_field = Select(browser.find_element("name", "dd"))
password_date_field.select_by_visible_text(str(password_date))

password_month_field = Select(browser.find_element("name", "mm"))
password_month_field.select_by_visible_text(password_month)

password_year_field = Select(browser.find_element("name", "yyyy"))
password_year_field.select_by_visible_text(str(password_year))

login_button = browser.find_element("xpath", "//input[@type='image']")
login_button.click()

while True:
    time.sleep(1)

browser.quit()
