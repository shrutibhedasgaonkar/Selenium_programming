import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(6)
driver.get("https://rahulshettyacademy.com/seleniumPractise")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("be")
time.sleep(2)

veg_list = driver.find_elements(By.XPATH, "//div[@class ='products']/div")
count_product = len(veg_list)
print(len(veg_list))

time.sleep(5)
for list_1 in veg_list:
    list_1.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//a[@class = 'cart-icon']").click()
driver.find_element(By.XPATH, "//div[@class = 'cart-preview active']/div/button").click()

# sum calculation
prices = driver.find_elements(By.XPATH,"//tbody/tr/td[5]/p")
Sum = 0
for price in prices:
    Sum = Sum + int(price.text)
print(Sum)

amount = driver.find_element(By.CLASS_NAME, "totAmt")
total_amt = float(amount.text)

assert Sum == total_amt

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

time.sleep(5)
promo_info = driver.find_element(By.CLASS_NAME, "promoInfo")
print(promo_info.text)
actual_message = "Code applied ..!"
assert promo_info.text == "Code applied ..!", (f"\nExpected promo code message is {actual_message} and actual promo code"
                                               f" message is {promo_info.text}")

# assert discount amount
dis_amt = driver.find_element(By.CLASS_NAME, "discountAmt")
discount_amt = float(dis_amt.text)
print(discount_amt)

discount = total_amt * (10/100)
final_price = total_amt - discount
print(final_price)

assert final_price == discount_amt


input("Press Enter to exit...")









