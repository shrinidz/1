from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'I am on the inventory page')
def step_impl(context):

    context.driver.get("https://www.saucedemo.com")
    username_input = context.driver.find_element(By.ID, "user-name")
    password_input = context.driver.find_element(By.ID, "password")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()


    WebDriverWait(context.driver, 10).until(
        EC.url_contains("inventory.html")
    )

@when('user sorts products from low price to high price')
def step_sort_products(context):
    # Code to sort products by price (assuming the UI allows this action)
    sort_dropdown = context.driver.find_element(By.CLASS_NAME, "product_sort_container")
    sort_dropdown.click()
    price_low_to_high = context.driver.find_element(By.XPATH, "//option[@value='lohi']")
    price_low_to_high.click()


@when('user adds lowest priced product')
def step_add_lowest_priced_product(context):
    # Code to add the lowest priced product to cart
    add_to_cart_buttons = context.driver.find_elements(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']")
    lowest_price_button = add_to_cart_buttons[0]  # Assuming the first product is the lowest priced
    lowest_price_button.click()

@when('user clicks on cart')
def step_click_cart(context):
    # Code to click on the cart icon or link
    cart_icon = context.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

@when('user clicks on checkout')
def step_click_checkout(context):
    # Code to click on the checkout button
    checkout_button = context.driver.find_element(By.ID, "checkout")
    checkout_button.click()

@when('user enters first name {first_name}')
def step_enter_first_name(context, first_name):
    # Code to enter first name in the checkout form
    first_name_field = context.driver.find_element(By.ID, "first-name")
    first_name_field.send_keys("john")

@when('user enters last name {last_name}')
def step_enter_last_name(context, last_name):
    # Code to enter last name in the checkout form
    last_name_field = context.driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("doe")

@when('user enters zip code {zip_code}')
def step_enter_zip_code(context, zip_code):
    # Code to enter zip code in the checkout form
    zip_code_field = context.driver.find_element(By.ID, "postal-code")
    zip_code_field.send_keys("123")

@when('user clicks Continue button')
def step_click_continue(context):
    # Code to click on the continue button in the checkout form
    continue_button = context.driver.find_element(By.XPATH, "//input[@type='submit']")
    continue_button.click()

@then('I verify in Checkout overview page if the total amount for the added item is ${total_amount}')
def step_verify_total_amount(context, total_amount):
    # Code to verify the total amount for the added item in the checkout overview page
    total_amount = context.driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]")
    Actual_total_amount = total_amount.text[7:]
    Expected_total_amount = "$8.63"
    assert Actual_total_amount == Expected_total_amount

@when('user clicks Finish button')
def step_click_finish(context):
    # Code to click on the finish button to complete the order
    context.driver.execute_script("window.scrollTo(0, 100);")
    finish_button = context.driver.find_element(By.ID, "finish")
    finish_button.click()

@then('Thank You header is shown in Checkout Complete page')
def step_verify_thank_you_header(context):
    # Code to verify the Thank You header in the checkout complete page
    thank_you_header = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='checkout_complete_container']/h2")))
    assert thank_you_header.is_displayed(), "Thank You header not found on the Checkout Complete page"

