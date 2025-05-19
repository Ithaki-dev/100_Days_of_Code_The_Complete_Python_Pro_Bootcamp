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
    fb_login_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Log in with Facebook"]')
    fb_login_button.click()
# Wait for the Facebook login page to load
sleep(3)
# Switch to the Facebook login window
driver.switch_to.window(driver.window_handles[1])
# Find the email and password fields and enter your credentials
email_field = driver.find_element(By.ID, 'email')
email_field.send_keys('ithakidev@gmail.com')
password_field = driver.find_element(By.ID, 'pass')
password_field.send_keys('caraculo123#')
# Find the login button and click it
login_button = driver.find_element(By.ID, 'loginbutton')
login_button.click()
# Click the "Continue" button if it appears
try:
    continue_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Continuar como Robert"]')
    continue_button.click()
except:
    print("Continue button not found")
# Switch back to the Tinder window
driver.switch_to.window(driver.window_handles[0])
# Wait for the Tinder page to load
sleep(3)
# Find the "Allow" button and click it
try:
    allow_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Allow"]')
    allow_button.click()
except:
    print("Allow button not found")
# Allow location access
try:
    location_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Allow"]')
    location_button.click()
except:
    print("Location button not found")

# Wait for the Tinder page to load
sleep(5)