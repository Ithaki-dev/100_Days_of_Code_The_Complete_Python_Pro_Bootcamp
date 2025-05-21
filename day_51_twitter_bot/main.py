# Bot to tweet my internet usage stats to my ISP if they are not fulfilling my contract
"""
This script automates the process of checking internet speed and tweeting the results if the speed is below the contracted rate.
Workflow:
1. Uses Selenium WebDriver to open speedtest.net and perform a speed test.
2. Extracts the download and upload speeds from the results.
3. If the download speed is below the contracted threshold, logs into Twitter using provided credentials.
4. Composes and posts a tweet tagging the ISP about the subpar internet speed.
Variables:
- my_contract_download_speed (float): The contracted download speed in Mbps.
- my_contract_upload_speed (float): The contracted upload speed in Mbps.
Dependencies:
- selenium
- Firefox WebDriver
Note:
- User credentials are hardcoded for demonstration purposes; this is not secure for production use.
- The script uses sleep for waiting, which may be unreliable if page load times vary.
- Update the email, username, and password fields with actual credentials before use.
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
my_contract_download_speed = 70  # Mbps
my_contract_upload_speed = 70  # Mbps

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# Navigate to the speedtest website
driver.get("https://www.speedtest.net/")
# Wait for the page to load
sleep(3)
# Find the "Go" button and click it
go_button = driver.find_element(By.CLASS_NAME, "start-text")
go_button.click()
# Wait for the test to complete
sleep(60)
# Find the download and upload speeds
download_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text
download_speed = float(download_speed)
upload_speed = float(upload_speed)
print(f"Download speed: {download_speed} Mbps")
print(f"Upload speed: {upload_speed} Mbps")
# Close the browser
driver.quit()
# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
# Navigate to the Twitter website
driver.get("https://twitter.com/")
# Wait for the page to load
sleep(3)
# Find the login button and click it
login_button = driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
login_button.click()
# Wait for the login page to load
sleep(5)
# Find the email and password fields and enter your credentials
email_field = driver.find_element(By.NAME, 'text')
email_field.send_keys('your_email_here')
# Find the next button and click it
next_button = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
next_button.click()
# Wait for the next page to load
sleep(3)
#  Enter the username and click next
username_field = driver.find_element(By.NAME, 'text')
username_field.send_keys('your_username_here')
# Find the next button and click it
next_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="ocfEnterTextNextButton"]')
next_button.click()
# Wait for the password field to load
sleep(5)
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('your_password_here')
# Click the login button
login_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="LoginForm_Login_Button"]')
login_button.click()
# Wait for the Twitter page to load
sleep(7)
#  check if the download speed is less than 70 Mbps
if int(download_speed) < my_contract_download_speed:
    # Tweet the download speed
    tweet = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
    tweet.send_keys(f"Mi velocidad de descarga es {download_speed} Mbps, que es menos de mi velocidad contratada de {my_contract_download_speed} Mbps.")
    # Find the tweet button and click it
    tweet_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]')
    tweet_button.click()