from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

USER_NAME = "ithakidev"
PASSWORD = "C0n547udr7"
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

    def scroll_followers_popup(self, scrolls=5):
        # Locate the scrollable followers list inside the dialog
        dialog = self.driver.find_element(By.XPATH, "//div[@role='dialog']//ul")
        for _ in range(scrolls):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            sleep(2)

    def find_followers(self):
        # Go to the similar account's followers page
        self.driver.get(f"https://www.instagram.com/{self.similar_account}/")
        sleep(5)

        # Click on the followers link
        followers_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span")
        followers_link.click()
        sleep(5)
        # Scroll in the popup to load more followers
        self.scroll_followers_popup(scrolls=5)

    
    # def follow_users(self):
    #     #  Click on the first 10 followers
    #     followers = self.driver.find_elements(By.XPATH, "//div[@role='dialog']//li")[:10]
    #     for follower in followers:
    #         follow_button = follower.find_element(By.XPATH, ".//button[contains(text(), 'Follow')]")
    #         if follow_button:
    #             follow_button.click()
    #             sleep(2)

  
    
if __name__ == "__main__":
    bot = InstagramFollowerBot(SIMILAR_ACCOUNT)
    bot.driver.get("https://www.instagram.com/accounts/login/")
    sleep(5)
    bot.login()
    bot.find_followers()
    # bot.follow_users()