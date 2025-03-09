from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_path = "path/to/your/browser/driver"
browser = webdriver.Chrome(executable_path=driver_path)

url = "https://www.google.com"
browser.get(url)

search_box = browser.find_element_by_name("q")
search_box.send_keys("Python web automation")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

for i in range(3):
    next_page_button = browser.find_element_by_link_text("Next")
    next_page_button.click()
    time.sleep(5)

browser.quit()