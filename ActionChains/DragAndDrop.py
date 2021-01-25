from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.implicitly_wait(5)
driver.maximize_window()
source = driver.find_element(By.XPATH, "//div[@id='draggable']")
target = driver.find_element(By.XPATH, "//div[@id='droppable']")
act_chain = ActionChains(driver)
act_chain.drag_and_drop(source, target).perform()
time.sleep(5)
driver.quit()
