# This is a bot for Tinder, a dating app. It automates the process of swiping right on profiles.
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# Navigate to the Tinder website
driver.get("https://tinder.com")
# Wait for the page to load
sleep(3)
# Find the login button and click it
login_button = driver.find_element(By.LINK_TEXT, 'Log in')
login_button.click()
# Wait for the login page to load
sleep(3)
# Find the login with Facebook button and click it
try:
    fb_login_button = driver.find_element(By.LINK_TEXT, 'Log in with Facebook')
except:
    # If the 'Log in with Facebook' button is not found, try using a different selector
    # This is a fallback in case the button is not found by LINK_TEXT
    # Sometimes the 'Log in with Facebook' button may not be found by LINK_TEXT due to localization, dynamic content, or different page layouts.
    # Try using a more robust selector, such as partial link text or a CSS selector.
    fb_login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'login-button') and contains(text(), 'Log in with Facebook')]")
fb_login_button.click()
# Wait for the Facebook login page to load
sleep(3)