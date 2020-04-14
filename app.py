from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox 
browser = webdriver.Firefox(executable_path = '../../geckodriver.exe')
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")

# Get inputs from user ..

print("Please enter email id")
email = input()
print("Please enter password")
passwordIn = input()

username.send_keys(email)
password.send_keys(passwordIn)
# Step 4) Click Login
submit.click()