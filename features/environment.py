from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome(executable_path="C:/Users/Dell/OneDrive/Documents/driver/chromedriver-win64/chromedriver.exe")

def after_all(context):
    context.driver.quit()

