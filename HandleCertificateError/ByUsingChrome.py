from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver import DesiredCapabilities

desired_capabilities = DesiredCapabilities().CHROME.copy()
desired_capabilities['acceptInsecureCerts'] = True
driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=desired_capabilities)
driver.implicitly_wait(10)
driver.get("https://expired.badssl.com/")
driver.maximize_window()
time.sleep(5)
driver.quit()
