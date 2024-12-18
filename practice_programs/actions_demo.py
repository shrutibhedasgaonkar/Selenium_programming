from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(5)
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

input("Press Enter to exit..!!")
