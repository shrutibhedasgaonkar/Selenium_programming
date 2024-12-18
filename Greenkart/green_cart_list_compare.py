import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(8)

driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("b")

time.sleep(3)
# verify list for the searched character
exp_veg_list = ['Brocolli - 1 Kg', 'Cucumber - 1 Kg', 'Beetroot - 1 Kg', 'Beans - 1 Kg', 'Brinjal - 1 Kg', 'Banana - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg', '', '']

search_list = driver.find_elements(By.CSS_SELECTOR, ".product-name")
actual_list = []

for items in search_list:
    actual_list.append(items.text)

print("Actual List = ", actual_list)
assert actual_list == exp_veg_list, f"\nExpected list: {exp_veg_list}\nActual list: {actual_list}"

input("Press enter to exist...")
