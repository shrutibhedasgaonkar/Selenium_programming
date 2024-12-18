from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.LINK_TEXT, "Top Deals").click()

window_opened = driver.window_handles
driver.switch_to.window(window_opened[1])
driver.find_element(By.XPATH, "//thead/tr[1]/th[1]/span[1]").click()
items_sorted_list = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
expected_list = ['Almond', 'Apple', 'Banana', 'Beans', 'Brinjal']
sorted_list = []
for item in items_sorted_list:
    sorted_list.append(item.text)

print(sorted_list)

assert sorted_list == expected_list, f"The {sorted_list} is not same as {expected_list} "

print(f"The {sorted_list} is same as {expected_list}")

input("Press Enter to exit..!")


