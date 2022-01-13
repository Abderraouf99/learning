from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = "/Users/abderraoufbenchoubane/chromedriver"

driver = webdriver.Chrome(driver_path)

driver.get("https://www.python.org/")

upcoming_events_html_data = driver.find_elements_by_css_selector(".event-widget li")
upcoming_events_dict = {}
for event in upcoming_events_html_data:
    formatted_event = event.text.split("\n")
    date = formatted_event[0]
    event_name = formatted_event[1]
    upcoming_events_dict[date] = event_name
print(upcoming_events_dict)
driver.quit()