# Selenium WebDriver
#* Selenium is a powerful tool for controlling web browsers through programs and performing browser automation.
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()  # Create a new instance of the Firefox driver
driver.get("https://www.python.org/")# Find the price using its class attribute value
upcoming_events = driver.find_element(By.CLASS_NAME, "event-widget")

print(f"Upcoming Events: {upcoming_events.text}")  # Print the upcoming events
# Save the upcoming events in to a dictionary
upcoming_events_dict = {}
for event in upcoming_events.find_elements(By.TAG_NAME, "li"):
    event_time = event.find_element(By.TAG_NAME, "time").text
    event_name = event.find_element(By.TAG_NAME, "a").text
    upcoming_events_dict[event_time] = event_name

print("Upcoming Events Dictionary:")
for time, name in upcoming_events_dict.items():
    print(f"  {time}: {name}")

# driver.quit()  # Close the browser