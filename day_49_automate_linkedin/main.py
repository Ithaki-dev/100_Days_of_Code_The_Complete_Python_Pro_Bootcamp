# This scrip automate aplication process on LinkedIn
"""
Automates the LinkedIn job application process using Selenium WebDriver.
This script performs the following steps:
1. Launches a Firefox browser instance.
2. Navigates to the LinkedIn homepage.
3. Signs in using provided email and password credentials.
4. Navigates to the 'Jobs' section.
5. Searches for jobs with the title "Python Developer".
6. Applies the 'Easy Apply' filter to job search results.
7. Initiates the 'Easy Apply' process for a job listing.
8. Attempts to submit the application form.
Note:
- The script uses various selectors (link text, partial link text, CSS selectors, class names) to locate elements, with fallbacks for robustness.
- Replace `"your_email_here"` and `"your_password_here"` with your actual LinkedIn credentials.
- Includes basic error handling for missing elements.
- Uses `sleep` to wait for page loads; for production use, consider using Selenium's explicit waits for better reliability.
"""

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
email_input.send_keys("jincho1995@gmail.com")  # Replace with your email
password_input = driver.find_element(By.ID, 'password')
password_input.send_keys("c0n547udr7")  # Replace with your password
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
sleep(5)  # seconds

# Get the apply form
try:
    apply_form = driver.find_element(By.CLASS_NAME, 'artdeco-modal')
except:
    try:
        apply_form = driver.find_element(By.CSS_SELECTOR, "div[role='dialog']")
    except:
        print("Apply form not found")
# Find the submit button and click it
def next_button():
    try:
        submit_button = apply_form.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
        submit_button.click()
    except:
        try:
            submit_button = apply_form.find_element(By.CLASS_NAME, 'artdeco-button__text')
            submit_button.click()
        except:
            print("Submit button not found")

# Press again next
next_button()
next_button()

def close_form():
    try:
        close_button = apply_form.find_element(By.CSS_SELECTOR, "button[aria-label='Close']")
        close_button.click()
    except:
        try:
            close_button = apply_form.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
            close_button.click()
        except:
            print("Close button not found")
    sleep(3)  # seconds
    #  Find the discard button first get the form
    try:
        discard_button = driver.find_element(By.CLASS_NAME, "artdeco-button--secondary")
        discard_button.click()
    except:
        try:
            discard_button = driver.find_element(By.CLASS_NAME, 'artdeco-button')
            discard_button.click()
        except:
            print("Discard button not found")

# Check if there is a aditional question
try:
    additional_question = driver.find_element(By.CLASS_NAME, "ph5")
    additional_question.click()
    if additional_question:
        close_form()
except:
    try:
        additional_question = driver.find_element(By.CSS_SELECTOR, "div[role='dialog']")
        additional_question.click()
        if additional_question:
            close_form()
    except:
        print("Additional question not found")
