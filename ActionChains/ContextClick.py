from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://demoqa.com/buttons")
driver.maximize_window()
right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
act_chain = ActionChains(driver)
act_chain.context_click(right_click_button).perform()
right_click_msg = driver.find_element(By.XPATH, "//p[text()='You have done a right click']")
print(right_click_msg.text)
time.sleep(5)
driver.quit()
