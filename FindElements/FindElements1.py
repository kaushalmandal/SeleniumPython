from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("E:\Software\driver\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.NAME, "q").send_keys("kaushal")
optionList = driver.find_elements(By.XPATH, "//div[@class='sbl1']")
for option in optionList:
    print(option.text)
    if (option.text == 'kaushalya'):
        option.click()
        break
#driver.quit()
