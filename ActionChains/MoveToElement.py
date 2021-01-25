from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.spicejet.com/")
driver.maximize_window()
login_ele = driver.find_element(By.XPATH, "//a[@id='ctl00_HyperLinkLogin']");
act_chain = ActionChains(driver)
act_chain.move_to_element(login_ele).perform()
spice_club_member = driver.find_element(By.LINK_TEXT, "SpiceClub Members")
act_chain.move_to_element(spice_club_member).perform()
member_login = driver.find_element(By.LINK_TEXT, "Member Login")
member_login.click()
time.sleep(5)
driver.quit()
