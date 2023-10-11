
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
import time

username = "abcd_a@xyz.ac.in"
password = "_________"

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://moodlegurukul.nie.ac.in/login/index.php")

email_input = browser.find_element(By.CSS_SELECTOR, 'input[id="username"]')
email_input.send_keys(username)

password_input = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
password_input.send_keys(password)

sign_in_button = browser.find_element(By.CSS_SELECTOR, 'button[id="loginbtn"]')
sign_in_button.click()


while True:
    time.sleep(1)

browser.quit()

