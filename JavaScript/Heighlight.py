from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://facebook.com")
driver.maximize_window()
driver.implicitly_wait(10)
email = driver.find_element(By.XPATH, "//input[@id='email']")
driver.execute_script("arguments[0].style.border='3px solid red'", email)
driver.quit()