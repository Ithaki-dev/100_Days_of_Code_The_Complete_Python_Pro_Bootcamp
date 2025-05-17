from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# Navigate to the Lab Report website
driver.get("https://secure-retreat-92358.herokuapp.com/")
# Find the first name input field using its name attribute value
first_name = driver.find_element(By.NAME, "fName")
# Find the last name input field using its name attribute value
last_name = driver.find_element(By.NAME, "lName")
# Find the email input field using its name attribute value
email = driver.find_element(By.NAME, "email")
# Find the sign up button using its class attribute value
sign_up_button = driver.find_element(By.CLASS_NAME, "btn")
# Fill in the first name input field
first_name.send_keys("Robert")
# Fill in the last name input field
last_name.send_keys("Quesada")
# Fill in the email input field
email.send_keys("robert.quesada@example.com")
# Click the sign up button
sign_up_button.click()