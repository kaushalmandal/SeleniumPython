from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.maximize_window()
Select = Select(driver.find_element(By.XPATH, "//select[@id='Form_submitForm_Country']")).select_by_visible_text(
    "India")
time.sleep(5)
driver.quit()
