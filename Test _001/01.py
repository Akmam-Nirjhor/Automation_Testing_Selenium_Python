import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
driver.get("https://google.com")
driver.find_element("name","q").send_keys("https://www.bdbooking.com/")
driver.find_element(By.NAME,"btnK").submit()
driver.get("https://www.bdbooking.com/")

# driver.find_element_xpath_("//button[@class='btn btn-sm btn-primary header-top-btn login-button-press hide-on-extranet']").click()

# Sea Beach
# # driver.find_element_by_link_text("Sea Beach")
driver.get("https://www.bdbooking.com/Spot/Bangladesh/Sajek")









