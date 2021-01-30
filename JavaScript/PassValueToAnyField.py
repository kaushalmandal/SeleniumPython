from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5)
driver.maximize_window()
username = driver.find_element(By.XPATH, "//input[@name='email']")
driver.execute_script("document.getElement(username).value='kaushal.mandal000@gmail.com';")
time.sleep(5)
driver.quit()
