"""This script automates playing the Cookie Clicker game using Selenium WebDriver.
Features:
- Automatically clicks the main cookie at regular intervals.
- Monitors the current number of cookies and available upgrades (Cursor, Grandma, Factory).
- Purchases the most expensive affordable upgrade in priority order: Factory > Grandma > Cursor.
Functions:
- update_elements(): Retrieves the current cookie count, upgrade buttons, and their prices.
- click_cookie(): Clicks the main cookie button.
Execution:
- Continuously clicks the cookie and attempts to purchase upgrades as soon as enough cookies are available.
- Prints the current cookie count and logs purchases to the console.
Requirements:
- Selenium WebDriver for Firefox must be installed and configured.
- Internet connection to access the Cookie Clicker game.
Note:
- The script is intended for educational and automation practice purposes."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# Navigate to the Cookie Clicker website
driver.get("https://orteil.dashnet.org/experiments/cookie/")


def update_elements():
    """
    Updates and retrieves the current game elements and their prices from the Cookie Clicker game using Selenium.

    Returns:
        tuple: A tuple containing:
            - cursor_1_price (int): The price of the Cursor upgrade.
            - grandma_2_price (int): The price of the Grandma upgrade.
            - factory_3_price (int): The price of the Factory upgrade.
            - cursor_1 (WebElement): The WebElement for the Cursor upgrade button.
            - grandma_2 (WebElement): The WebElement for the Grandma upgrade button.
            - factory_3 (WebElement): The WebElement for the Factory upgrade button.
            - cookie_count (int): The current number of cookies available.
    """
    cookie_count = driver.find_element(By.ID, "money").text
    # Remove the commas from the cookie count
    cookie_count = cookie_count.replace(",", "")
    # Convert the cookie count to an integer
    cookie_count = int(cookie_count)
    # Find the elements for the Cursor, Grandma, and Factory buttons
    cursor_1 = driver.find_element(By.ID, "buyCursor")
    grandma_2 = driver.find_element(By.ID, "buyGrandma")
    factory_3 = driver.find_element(By.ID, "buyFactory")
    # Get the prices of the Cursor, Grandma, and Factory buttons
    cursor_1_price = int(cursor_1.find_element(By.XPATH, '/html/body/div[3]/div[5]/div/div[1]/b').text.split(" ")[-1])
    grandma_2_price = int(grandma_2.find_element(By.XPATH, '/html/body/div[3]/div[5]/div/div[2]/b').text.split(" ")[-1])
    factory_3_price = int(factory_3.find_element(By.XPATH, '/html/body/div[3]/div[5]/div/div[3]/b').text.split(" ")[-1])
    # print(cursor_1_price, grandma_2_price, factory_3_price)
    return cursor_1_price, grandma_2_price, factory_3_price,cursor_1, grandma_2, factory_3,cookie_count


# make the most click per second

def click_cookie():
    # Find the cookie button
    cookie_button = driver.find_element(By.ID, "cookie")
    # Click the cookie button
    cookie_button.click()
    # Wait for 0.5 seconds
    time.sleep(0.5)

if __name__ == "__main__":
    # Click the cookie button every 0.5 seconds
    while True:
        click_cookie()
        # Get the current prices
        cursor_1_price, grandma_2_price, factory_3_price, cursor_1, grandma_2, factory_3, cookie_count = update_elements()

        print(cookie_count)
        # Check if the cookie count is greater than the price of the Factory
        if cookie_count > factory_3_price:
            # Click the Factory button
            factory_3.click()
            print("Factory bought")
        # Check if the cookie count is greater than the price of the Grandma
        elif cookie_count > grandma_2_price:
            # Click the Grandma button
            grandma_2.click()
            print("Grandma bought")
        # Check if the cookie count is greater than the price of the Cursor
        elif cookie_count > cursor_1_price:
            # Click the Cursor button
            cursor_1.click()
            print("Cursor bought")
       