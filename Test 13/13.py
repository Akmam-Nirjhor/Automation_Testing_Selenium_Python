import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.get("https://google.com")
driver.find_element("name","q").send_keys("https://www.bdbooking.com/")
driver.find_element(By.NAME,"btnK").submit()
driver.get("https://www.bdbooking.com/")
driver.get("https://www.bdbooking.com/Spot/Bangladesh/Kuakata")









