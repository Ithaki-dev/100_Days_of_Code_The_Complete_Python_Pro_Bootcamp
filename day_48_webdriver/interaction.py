from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# Navigate to the Wikipedia website
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# Find the articlecount using its class attribute value
article_count = driver.find_element(By.XPATH,'//*[@id="articlecount"]/ul/li[2]/a[1]')
# Print the article count
print(f"Article Count: {article_count.text}")  # Print the article count
# article_count.click()  # Click on the article count link

all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()  # Click on the all portals link

search = driver.find_element(By.NAME, "search")
search.send_keys("Python (programming language)")  # Type in the search box
search.send_keys(Keys.ENTER)  # Press Enter