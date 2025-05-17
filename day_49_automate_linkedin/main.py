# This scrip automate aplication process on LinkedIn

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# Navigate to the LinkedIn jobs page
driver.get("https://www.linkedin.com")
# Wait for the page to load
sleep(5)  # seconds
# Find the sign-in button and click it
sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign in with email')
sign_in_button.click()
# Wait for the sign-in page to load
sleep(5)  # seconds
# Find the email and password input fields and enter your credentials
email_input = driver.find_element(By.ID, 'username')
email_input.send_keys("your_email@example.com")
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys("your_password")
password_input.send_keys(Keys.RETURN)

# Wait for the page to load
sleep(5)  # seconds

# Find the search input field and enter the job title
# search_input = driver.find_element(By.ID, 'jobs-search-box-keyword-id-ember1936')
# search_input.send_keys("Software Engineer")
# search_input.send_keys(Keys.ENTER)


