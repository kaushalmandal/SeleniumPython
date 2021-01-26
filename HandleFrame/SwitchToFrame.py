from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://londonfreelance.org/courses/frames/index.html")
driver.implicitly_wait(10)
driver.maximize_window()
driver.switch_to.frame(3)
driver.switch_to.frame('navbar')
frame_element = driver.find_element(By.XPATH, "//frame[@name='content']")
driver.switch_to.frame(frame_element)
time.sleep(5)
driver.quit()
