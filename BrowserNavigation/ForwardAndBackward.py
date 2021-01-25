from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
driver.implicitly_wait(5)
driver.maximize_window()

#
best_seller=driver.find_element(By.XPATH,"//a[@class='nav-a  ' and text()='Best Sellers']")
best_seller.click()

# backward direction
driver.back()

# forward direction
driver.forward()

print(driver.title)
driver.quit()