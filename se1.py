import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://trytestingthis.netlify.app/index.html")

first_name= driver.find_element(By.ID, "fname")
first_name.send_keys("Sujan")

last_name= driver.find_element(By.ID, "lname")
last_name.send_keys("Malakar")
print(driver.title)

#for 5 sec delay
time.sleep(5)
