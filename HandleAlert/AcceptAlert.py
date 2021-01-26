from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.implicitly_wait(10)
driver.maximize_window()
signin = driver.find_element(By.XPATH, "//input[@name='proceed']");
signin.click()
time.sleep(5)
text = driver.switch_to.alert.text
print("text is :", text)
driver.switch_to.alert.accept()
driver.quit()
