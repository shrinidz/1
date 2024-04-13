from selenium import webdriver
from behave import given, when, then

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the Demo Login Page')
def step_impl(context):

    context.driver.get("https://www.saucedemo.com")

@when('I fill the account information for account StandardUser into the Username field and the Password field')
def step_impl(context):
    username_input = context.driver.find_element(By.ID, "user-name")
    password_input = context.driver.find_element(By.ID, "password")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")

@when('I fill the account information for account LockedOutUser into the Username field and the Password field')
def step_impl(context):
    username_input = context.driver.find_element(By.ID, "user-name")
    password_input = context.driver.find_element(By.ID, "password")

    username_input.send_keys("locked_out_user")
    password_input.send_keys("secret_sauce")

@when('I click the Login Button')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()

@then('I am redirected to the Demo Main Page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("inventory.html")
    )

@then('I verify the App Logo exists')
def step_impl(context):
    app_logo = context.driver.find_element(By.CLASS_NAME, "app_logo")
    assert app_logo.is_displayed()


@then('I verify the Error Message contains the text "{error_message}"')
def step_impl(context, error_message):
    error_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert error_element.text  == "Epic sadface: Sorry, this user has been locked out."
