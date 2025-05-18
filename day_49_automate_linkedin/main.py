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
email_input.send_keys("your_email_here")  # Replace with your email
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys("your_password_here")  # Replace with your password
password_input.send_keys(Keys.RETURN)
# Wait for the page to load
sleep(5)  # seconds
# Find the jobs tab and click it
# Sometimes the 'Jobs' tab may not be found by LINK_TEXT due to localization, dynamic content, or different page layouts.
# Try using a more robust selector, such as partial link text or a CSS selector.

try:
    jobs_tab = driver.find_element(By.LINK_TEXT, 'Jobs')
except:
    try:
        jobs_tab = driver.find_element(By.PARTIAL_LINK_TEXT, 'Job')
    except:
        # Fallback: use a CSS selector for the jobs tab in the top nav
        jobs_tab = driver.find_element(By.CSS_SELECTOR, "a[data-test-global-nav-link='jobs']")

jobs_tab.click()
# Wait for the jobs page to load
sleep(5)  # seconds
# Find the search input field and enter the job title
try:
    search_input = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search jobs']")
    search_input.send_keys("Python Developer")
    search_input.send_keys(Keys.ENTER)
except:
    try:
        search_input = driver.find_element(By.CLASS_NAME, 'basic-input')
        search_input.send_keys("Python Developer")
        search_input.send_keys(Keys.ENTER)
    except:
        print("Search input field not found")
# Wait for the search results page to load
sleep(5)  # seconds
# Select the easy apply filter
try:
    easy_apply_button = driver.find_element(By.ID, "searchFilter_applyWithLinkedin")
    easy_apply_button.click()
except:
    try:
        easy_apply_button = driver.find_element(By.CLASS_NAME, 'artdeco-pill')
        easy_apply_button.click()
    except:
        print("Easy Apply button not found")

# Wait for the Easy Apply page to load
sleep(3)  # seconds
# Find the easy apply button and click it
try:
    easy_apply_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Easy Apply']")
    easy_apply_button.click()
except:
    try:
        easy_apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
        easy_apply_button.click()
    except:
        print("Easy Apply button not found")

# Wait for the Easy Apply form to load
sleep(3)  # seconds

# Find the SUBMIT button and click it
try:
    submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button__text")
    submit_button.click()
except:
    try:
        next_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'submit')
        next_button.click()
    except:
        print("Next button not found")
