import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

'''
element_radio = driver.find_element(By.XPATH, "//input[@value='radio1']")
print(element_radio.is_displayed())  # Returns True if the element is visible
print(element_radio.is_enabled())  # Returns True if the element is clickable

driver.find_element(By.XPATH, "//input[@value='radio1']").click()

select = Select(driver.find_element(By.ID, "dropdown-class-example"))
select.select_by_visible_text("Option3")
select.select_by_value("option2")

# driver.find_element(By.XPATH, "//input[@id ='checkBoxOption2']").click()

boxes = driver.find_elements(By.XPATH, "//input[@type= 'checkbox']")
for checkboxes in boxes:
    if checkboxes.get_attribute("value") == "option2":
        checkboxes.click()

driver.find_element(By.ID, "autocomplete").send_keys("In")
time.sleep(3)
list_1 = driver.find_elements(By.XPATH, "//li[@class= 'ui-menu-item']/div")
for elements in list_1:
    if elements.text == "India":
        print(elements.text)
        elements.click()

print(driver.find_element(By.ID, "autocomplete").get_attribute("value"))

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[value= 'Hide']").click()
textbox = driver.find_element(By.CSS_SELECTOR, "input[name = 'show-hide']")
assert not textbox.is_displayed()

driver.find_element(By.CSS_SELECTOR, "input[value= 'Show']").click()
assert driver.find_element(By.CSS_SELECTOR, "input[name = 'show-hide']")

'''
name = "Test"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
time.sleep(2)

alert = driver.switch_to.alert
alert_message = alert.text
expected_word = "Test"
assert expected_word in alert_message
print(alert_message)
alert.accept()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
alert_message1 = alert.text
time.sleep(2)
text = "you want to confirm?"
print(alert_message1)
assert text in alert_message1
# alert.accept()
alert.dismiss()






