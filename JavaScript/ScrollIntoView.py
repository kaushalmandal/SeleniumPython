from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
driver.implicitly_wait(5)
driver.maximize_window()
aboutus = driver.find_element(By.XPATH, "//a[text()='About Us']")
driver.execute_script("arguments[0].scrollIntoView(true);", aboutus)
time.sleep(5)
driver.quit()
