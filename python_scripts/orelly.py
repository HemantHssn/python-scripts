
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
import time
import getpass

# print(f"its from orelley--------------->>>>{__name__}")

  
# Replace these values with your actual login credentials
username = "chethan.sk@nokia.com"
password = getpass.getpass("enter your password:\n")
# print(password)------->>>Omygod@123
# Create a new instance of the Chrome browser with the driver path managed by webdriver_manager
browser = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to the member login page
browser.get("https://www.oreilly.com/member/login/")

# Enter the username/email address
email_input = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
email_input.send_keys(username)


# Click on the 'Continue' button
continue_button = browser.find_element(By.CSS_SELECTOR, '[data-testid="EmailSubmit"]')
continue_button.click()

time.sleep(2) # Wait for the next page to load

# Find the password input element and send the password
password_input = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
password_input.send_keys(password)

# Find the Sign In button element
sign_in_button = browser.find_element(By.CSS_SELECTOR, 'button[data-testid="SignInBtn"]')
sign_in_button.click()

# Wait for the next page to load
while True:
    time.sleep(1)

# browser.quit()
