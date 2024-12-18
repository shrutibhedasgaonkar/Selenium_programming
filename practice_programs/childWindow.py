from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
tag_text = driver.find_element(By.TAG_NAME, "h3").text
print(tag_text)

driver.switch_to.window(windowsOpened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)


input("Press Enter to exit..!!")