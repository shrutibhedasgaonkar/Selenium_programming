from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://autotest.how/demo/tinymce")

driver.switch_to.frame("tinymce_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Test this iFrame")

driver.switch_to.default_content()

test_text = driver.find_element(By.CSS_SELECTOR, "h1").text
assert test_text == "An iFrame contains the TinyMCE WYSIWYG Editor"


input("Press Enter to exit..!")
