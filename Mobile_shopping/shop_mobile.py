import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(9)

driver.get("https://rahulshettyacademy.com/angularpractice/shop")

mobile_list_webElement = driver.find_elements(By.XPATH, "//div[@class= 'card h-100']")

for item in mobile_list_webElement:
    productName = item.find_element(By.XPATH, "div/h4/a").text
    if productName == "Samsung Note 8":
        print(productName)
        item.find_element(By.XPATH, "div/button").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout").click()

driver.find_element(By.CLASS_NAME, "btn.btn-success").click()
driver.find_element(By.ID, "country").send_keys("ind")

explicit_driver = WebDriverWait(driver, 15)
explicit_driver.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "India"))).click()

time.sleep(5)
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

print(driver.find_element(By.CLASS_NAME, "alert.alert-success.alert-dismissible").text)

assert "Success!" in driver.find_element(By.CLASS_NAME, "alert.alert-success.alert-dismissible").text, "Messages is not as expected"
print("Message is as expected.!")

input("press Enter to exit..!")
