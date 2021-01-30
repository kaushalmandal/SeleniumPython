from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
driver.implicitly_wait(5)
driver.maximize_window()
linktext = driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
driver.execute_script("arguments[0].click();", linktext)
title = driver.execute_script("return document.title;")
print("title is :", title)
driver.quit()
