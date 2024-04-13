from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path="C:/Users/Dell/OneDrive/Documents/driver/chromedriver-win64/chromedriver.exe")

driver.get("https://www.saucedemo.com")
driver.maximize_window()

username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )
#app_logo = driver.find_element(By.CLASS_NAME, "app_logo")
#assert app_logo.is_displayed()

#error_element = WebDriverWait(driver, 10).until(
        #EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    #)
#assert error_message in error_element.text
#assert error_element.text  == "Epic sadface: Sorry, this user has been locked out."

sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
sort_dropdown.click()
price_low_to_high = driver.find_element(By.XPATH, "//option[@value='lohi']")
price_low_to_high.click()

add_to_cart_buttons = driver.find_elements(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']")
lowest_price_button = add_to_cart_buttons[0]  # Assuming the first product is the lowest priced
lowest_price_button.click()

time.sleep(2)

cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()

time.sleep(2)

checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

first_name_field = driver.find_element(By.ID, "first-name")
first_name_field.send_keys("john")

last_name_field = driver.find_element(By.ID, "last-name")
last_name_field.send_keys("doe")

zip_code_field = driver.find_element(By.ID, "postal-code")
zip_code_field.send_keys("123")

continue_button = driver.find_element(By.XPATH, "//input[@type='submit']")
continue_button.click()

total_amount = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]")
Actual_total_amount = total_amount.text[7:]
Expected_total_amount = "$8.63"
assert  Actual_total_amount == Expected_total_amount

driver.execute_script("window.scrollTo(0, 100);")

finish_button = driver.find_element(By.ID, "finish")
finish_button.click()


thank_you_header = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='checkout_complete_container']/h2")))
assert thank_you_header.is_displayed(), "Thank You header not found on the Checkout Complete page"





