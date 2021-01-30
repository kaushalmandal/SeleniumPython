from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)
driver.quit()
