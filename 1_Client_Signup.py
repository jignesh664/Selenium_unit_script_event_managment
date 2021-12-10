import os
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
import time

options = webdriver.ChromeOptions()



driver = webdriver.Chrome(options=options)
driver.get("http://localhost/AD-event-management-main/HomePage/rishabh")
time.sleep(5)

signup_locator = By.LINK_TEXT, "SignUp"
signup_link = driver.find_element(*signup_locator)
signup_link.click()
time.sleep(3)


# for Client signup:
send_button = By.XPATH, "/html/body/div/div[3]/div/div[2]/button"
driver.find_element(*send_button).click()
time.sleep(3)

f_send_button = By.XPATH, "//button"
driver.find_element(*f_send_button).click()
time.sleep(3)


# enter name
name_locator= By.XPATH, "/html/body/form/div[1]/input"
name_field = driver.find_element(*name_locator)
name_field.send_keys("dilip")
time.sleep(3)

# enter username
user_name_locator= By.XPATH, "/html/body/form/div[2]/input"
user_name_field = driver.find_element(*user_name_locator)
user_name_field.send_keys("dilip")
time.sleep(3)

# enter email
email_locator= By.XPATH, "/html/body/form/div[3]/input"
email_field = driver.find_element(*email_locator)
email_field.send_keys("dilip@gmail.com")
time.sleep(3)

# enter password
password_locator= By.XPATH, "/html/body/form/div[4]/input"
password_field = driver.find_element(*password_locator)
password_field.send_keys("qwerty123")
time.sleep(3)

# enter confirm_password
c_password_locator= By.XPATH, "/html/body/form/div[5]/input"
c_password_field = driver.find_element(*c_password_locator)
c_password_field.send_keys("qwerty123")
time.sleep(3)

# enter mobile
mobile_locator= By.XPATH, "/html/body/form/div[6]/input"
mobile_field = driver.find_element(*mobile_locator)
mobile_field.send_keys("9898536464")
time.sleep(3)

#for scrolldown
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

c_send_button = By.XPATH, "/html/body/form/button[1]"
driver.find_element(*c_send_button).click()
time.sleep(5)

driver.quit()
