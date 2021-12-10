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

e_signup_locator = By.LINK_TEXT, "SignUp"
e_signup_link = driver.find_element(*e_signup_locator)
e_signup_link.click()
time.sleep(3)


# for Event_Manager signup:
e_send_button = By.XPATH, "/html/body/div/div[2]/form/button"
driver.find_element(*e_send_button).click()
time.sleep(3)

# f_send_button = By.XPATH, "//button"
# driver.find_element(*f_send_button).click()
# time.sleep(3)


# enter name
e_name_locator= By.XPATH, "/html/body/div/form/div[1]/input"
e_name_field = driver.find_element(*e_name_locator)
e_name_field.send_keys("shrey")
time.sleep(3)

# enter username
e_user_name_locator= By.XPATH, "/html/body/div/form/div[2]/input"
e_user_name_field = driver.find_element(*e_user_name_locator)
e_user_name_field.send_keys("shrey")
time.sleep(3)

#enter email
e_email_locator= By.XPATH, "/html/body/div/form/div[3]/input"
e_email_field = driver.find_element(*e_email_locator)
e_email_field.send_keys("shrey@gmail.com")
time.sleep(3)

# enter password
e_password_locator= By.XPATH, "/html/body/div/form/div[4]/input"
e_password_field = driver.find_element(*e_password_locator)
e_password_field.send_keys("qwerty12345")
time.sleep(3)

# enter confirm_password
ec_password_locator= By.XPATH, "/html/body/div/form/div[5]/input"
ec_password_field = driver.find_element(*ec_password_locator)
ec_password_field.send_keys("qwerty12345")
time.sleep(3)

# enter mobile
e_mobile_locator= By.XPATH, "/html/body/div/form/div[6]/input"
e_mobile_field = driver.find_element(*e_mobile_locator)
e_mobile_field.send_keys("9898735364")
time.sleep(3)

#for scrolldown
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

ec_send_button = By.XPATH, "/html/body/div/form/button[1]"
driver.find_element(*ec_send_button).click()
time.sleep(5)

driver.quit()
