from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

USER_NAME = "username"
PASSWORD = "password"
SIMILAR_ACCOUNT = "chefsteps"


class InstagramFollowerBot:
    def __init__(self, similar_account):
        self.similar_account = similar_account
        self.driver = webdriver.Firefox()

    def login(self):
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")

        username_input.send_keys(USER_NAME)
        password_input.send_keys(PASSWORD)

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        sleep(5)

    def find_followers(self):
        # Go to the similar account's followers page
        self.driver.get(f"https://www.instagram.com/{self.similar_account}/")
        sleep(5)

        # Click on the followers link
        followers_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span")
        followers_link.click()
        sleep(5)
        # Switch to Pop-up follower frame
        scrollable_popup = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_popup)
            sleep(2)


    def follow_users(self):
        # Find all the follow buttons in the followers pop-up
        follow_buttons = self.driver.find_elements(By.XPATH, "//div[@role='dialog']//button[.//div[text()='Follow']]")
        if not follow_buttons:
            print("No follow buttons found.")
            return
        for button in follow_buttons:
            try:
                button.click()
                sleep(1)
            except Exception as e:
                print(f"Error clicking follow button: {e}")
                continue


if __name__ == "__main__":
    bot = InstagramFollowerBot(SIMILAR_ACCOUNT)
    bot.driver.get("https://www.instagram.com/accounts/login/")
    sleep(5)
    bot.login()
    bot.find_followers()
    bot.follow_users()