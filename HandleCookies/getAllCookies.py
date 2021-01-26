from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.reddit.com/")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.get_cookies())
cookies = driver.get_cookies()
for cook in cookies:
    print(cook)
    break
driver.quit()
