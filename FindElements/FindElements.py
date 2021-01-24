from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("E:\Software\driver\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@name='q']").send_keys('kaushal')
time.sleep(5)
optionList = driver.find_elements(By.XPATH, "//div[@class='sbl1']")
print("length in optionList is :", optionList)
for option in optionList:
    print(option.text)
driver.quit()
