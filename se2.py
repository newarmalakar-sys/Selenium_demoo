import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://youtube.com")

search = driver.find_element(By.NAME, "search_query")
search.send_keys("Xpath selenium tutorial")

#Absolute Xpath
# findd = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/div[1]/div/button/span/span/div")
# findd.click()

#relative Xpath
driver.find_element(By.XPATH, ""//div[@style='width:100%;height:100%']"").click()

time.sleep(5)
