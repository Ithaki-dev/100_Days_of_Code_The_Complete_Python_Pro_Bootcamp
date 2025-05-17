from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# Navigate to the Wikipedia website
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# Find the articlecount using its class attribute value
article_count = driver.find_element(By.XPATH,'//*[@id="articlecount"]/ul/li[2]/a[1]')
# Print the article count
print(f"Article Count: {article_count.text}")  # Print the article count