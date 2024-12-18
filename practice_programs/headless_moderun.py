import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome()
driver.implicitly_wait(5)


driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

openWindows = driver.window_handles

driver.switch_to.window(openWindows[1])
email_id = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
print("Email Id is ", email_id)
print(f"{email_id=}")

driver.switch_to.window(openWindows[0])
driver.find_element(By.ID, "username").send_keys(email_id)
driver.find_element(By.ID, "password").send_keys("learning")

driver.find_element(By.XPATH, "//div/label[2]/span[1]").click()
time.sleep(2)
driver.find_element(By.ID, "okayBtn").click()
driver.find_element(By.NAME, "terms").click()
driver.find_element(By.ID, "signInBtn").click()
time.sleep(2)
error_msg = driver.find_element(By.XPATH, "//form/div[1]").text
print("Error Message is ", error_msg)

print("Successful run.. !!")
