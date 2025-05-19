# This is a bot for Tinder, a dating app. It automates the process of swiping right on profiles.
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


# Configura el perfil de Firefox para permitir la ubicación automáticamente
profile = FirefoxProfile()
profile.set_preference("geo.prompt.testing", True)
profile.set_preference("geo.prompt.testing.allow", True)
profile.set_preference("geo.enabled", True)

# Usa Options para asignar el perfil
options = Options()
options.profile = profile

# Crea una nueva instancia del driver de Firefox con el perfil configurado
# driver = webdriver.Firefox(firefox_profile=profile)
driver = webdriver.Firefox(options=options)

# Navigate to the Tinder website
driver.get("https://tinder.com")
# Wait for the page to load
sleep(3)
# Find the login button and click it
login_button = driver.find_element(By.LINK_TEXT, 'Log in')
login_button.click()
# Wait for the login page to load
sleep(3)
# Find the login with Facebook button and click it
try:
    fb_login_button = driver.find_element(By.LINK_TEXT, 'Log in with Facebook')
except:
    # If the 'Log in with Facebook' button is not found, try using a different selector
    # This is a fallback in case the button is not found by LINK_TEXT
    # Sometimes the 'Log in with Facebook' button may not be found by LINK_TEXT due to localization, dynamic content, or different page layouts.
    # Try using a more robust selector, such as partial link text or a CSS selector.
    fb_login_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Log in with Facebook"]')
    fb_login_button.click()
# Wait for the Facebook login page to load
sleep(3)
# Switch to the Facebook login window
driver.switch_to.window(driver.window_handles[1])
# Find the email and password fields and enter your credentials
email_field = driver.find_element(By.ID, 'email')
email_field.send_keys('your_email_here')
password_field = driver.find_element(By.ID, 'pass')
password_field.send_keys('your_password_here')  # Replace with your actual password
# Find the login button and click it
login_button = driver.find_element(By.ID, 'loginbutton')
login_button.click()
sleep(3)
# Click the "Continue" button if it appears
try:
    continue_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Continuar como Robert"]')
    continue_button.click()
except:
    print("Continue button not found")
# Switch back to the Tinder window
driver.switch_to.window(driver.window_handles[0])
# Wait for the Tinder page to load
sleep(3)
# Find the "Allow" button and click it
try:
    allow_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Allow"]')
    allow_button.click()
except:
    print("Allow button not found")
sleep(3)
# Click in i'll miss out
try:
    miss_out_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="I’ll miss out"]')
    miss_out_button.click()
except:
    print("Miss out button not found")

# Wait for the Tinder page to load
sleep(5)
# acept cookies
try:
    cookies_button = driver.find_element(
        By.CSS_SELECTOR,
        '[style="--tui-button-background: transparent; --tui-button-border: var(--color--border-button-secondary, inherit); --tui-button-foreground: var(--color--foreground-button-secondary, inherit); --tui-button-overlay: var(--color--interactive-button-secondary, inherit); --tui-button-focus: var(--color--border-focus-default, inherit);"]'
    )
    cookies_button.click()
except:
    print("Cookies button not found")
# Wait for the Tinder page to load
print("Waiting for Tinder to load...")
sleep(120)
# Start swiping
while True:
    try:
        # Find the "Like" button and click it
        like_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Nope"]')
        like_button.click()
        # Wait for a few seconds before swiping again
        sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
        break