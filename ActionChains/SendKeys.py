from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://classic.freecrm.com/")
driver.implicitly_wait(5)
driver.maximize_window()
username = driver.find_element(By.XPATH, "//input[@name='username']")
password = driver.find_element(By.XPATH, "//input[@name='password']")
act_chain = ActionChains(driver)
act_chain.send_keys(username, 'batchautomation').perform()
act_chain.send_keys(password, 'Test@12345').perform()
driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(5)
print(driver.title)
