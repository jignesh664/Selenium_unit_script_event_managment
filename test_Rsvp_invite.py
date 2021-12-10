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

# for Client login:
send_button = By.XPATH, "/html/body/div/div[3]/div/div[2]/button"
driver.find_element(*send_button).click()
time.sleep(3)

f_send_button = By.XPATH, "//button"
driver.find_element(*f_send_button).click()
time.sleep(3)

# enter username
u_name_locator= By.XPATH, "/html/body/div/form/div[1]/input"
u_name_field = driver.find_element(*u_name_locator)
u_name_field.send_keys("dilip")
time.sleep(3)

# enter password
password_locator= By.XPATH, "/html/body/div/form/div[2]/input"
password_field = driver.find_element(*password_locator)
password_field.send_keys("123456")
time.sleep(3)

#submit 
submit_button = By.XPATH, "/html/body/div/form/button"
driver.find_element(*submit_button).click()
time.sleep(3)

#Go to dashbord and click on rsvp
rsvp_button = By.XPATH, "/html/body/div/div[2]/div[1]/div/div[1]/div[4]/a/div/div[1]/div/i"
driver.find_element(*rsvp_button).click()
time.sleep(3)

#single invite
single_invite = By.XPATH, "/html/body/main/div[2]/div/div[1]/p[2]/a"
driver.find_element(*single_invite).click()
time.sleep(3)

#single invite fill form
single_guest_locator = By.XPATH, "/html/body/div/form/div[2]/input"
single_guest=driver.find_element(*single_guest_locator)
single_guest.send.keys("shrey")
time.sleep(5)

#attaned event
attend_event = By.XPATH, "/html/body/div/form/div[3]/div/table/tbody/tr/td[1]/div/label"
driver.find_element(*attend_event).click()
time.sleep(3)

#prefer_food
prefer_food = By.XPATH, "/html/body/div/form/div[4]/div/table/tbody/tr[1]/td[1]/div/label"
driver.find_element(*prefer_food).click()
time.sleep(3)

#cuisine
cuisine_locator = By.XPATH, "/html/body/div/form/div[5]/input"
cuisine_add=driver.find_element(*cuisine_locator)
cuisine_add.send.keys("no")
time.sleep(3)

#message
message_locator = By.XPATH, "/html/body/div/form/div[6]/input"
message_add=driver.find_element(*message_locator)
message_add.send.keys("Please provide entry")
time.sleep(3)



