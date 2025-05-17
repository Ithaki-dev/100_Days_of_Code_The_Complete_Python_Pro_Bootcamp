# This scrip automate aplication process on LinkedIn

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# Navigate to the LinkedIn jobs page
driver.get("https://www.linkedin.com/jobs/")

# Find the search input field and enter the job title
search_input = driver.find_element(By.ID, 'jobs-search-box-keyword-id-ember1936')
search_input.send_keys("Software Engineer")
search_input.send_keys(Keys.ENTER)


