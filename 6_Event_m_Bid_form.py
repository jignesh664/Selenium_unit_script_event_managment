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

login_locator = By.LINK_TEXT, "Login"
login_link = driver.find_element(*login_locator)
login_link.click()
time.sleep(3)

# for Event Manager login:
send_button = By.XPATH, "/html/body/div/div[2]/form/button"
driver.find_element(*send_button).click()
time.sleep(3)

# f_send_button = By.XPATH, "//button"
# driver.find_element(*f_send_button).click()
# time.sleep(3)

# enter username
e_name_locator= By.XPATH, "/html/body/div/form/div[1]/input"
e_name_field = driver.find_element(*e_name_locator)
e_name_field.send_keys("shrey")
time.sleep(3)

# enter password
e_password_locator= By.XPATH, "/html/body/div/form/div[2]/input"
e_password_field = driver.find_element(*e_password_locator)
e_password_field.send_keys("qwerty12345")
time.sleep(3)

#submit 
submit_button = By.XPATH, "/html/body/div/form/button"
driver.find_element(*submit_button).click()
time.sleep(5)

# Bid Form
# enter click on bid
bid_locator= By.XPATH, "/html/body/div/div/div/table/tbody/tr/td[10]/button"
bid_field = driver.find_element(*bid_locator)
bid_field.click()
time.sleep(3)

# Price
price_locator= By.XPATH, "/html/body/div/form/div[1]/input"
price_field = driver.find_element(*price_locator)
price_field.send_keys("110000")
time.sleep(3)

# comment
comment_locator= By.XPATH, "/html/body/div/form/div[2]/textarea"
comment_field = driver.find_element(*comment_locator)
comment_field.send_keys("please check bid amount and please confirm with us")
time.sleep(3)

# File attach
file_attach_locator= By.XPATH, "/html/body/div/form/div[3]/input"
file_attach_field = driver.find_element(*file_attach_locator)
file_attach_field.send_keys("C:\\Users\\Jigne\\OneDrive\\Desktop\\PAN CARD\\pan60kb.jpeg")
time.sleep(3)

#final submit 
sub_button = By.XPATH, "/html/body/div/form/input"
driver.find_element(*sub_button).click()
time.sleep(3)

#and then Logout
logout_locator = By.LINK_TEXT, "Logout"
logout_link = driver.find_element(*logout_locator)
logout_link.click()
time.sleep(5)

#driver.quit()

