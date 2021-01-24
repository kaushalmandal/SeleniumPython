from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()
country = driver.find_element(By.ID, "Form_submitForm_Industry")
Select = Select(country)
Select.select_by_visible_text("Education")
time.sleep(5)
driver.quit()
