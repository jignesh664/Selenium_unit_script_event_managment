import os
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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
password_field.send_keys("qwerty123")
time.sleep(3)

#submit 
submit_button = By.XPATH, "/html/body/div/form/button"
driver.find_element(*submit_button).click()
time.sleep(3)

#Go to dashbord
event_button = By.XPATH, "/html/body/div/div[2]/div[1]/div/div[1]/div[1]/a/div/div[1]/div/i"
driver.find_element(*event_button).click()
time.sleep(3)

#event_form:
#username
username_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[1]/input"
username_field = driver.find_element(*username_locator)
username_field.send_keys("dilip")
time.sleep(3)

#location
location_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[2]/select"
location_field = driver.find_element(*location_locator)
location_field.send_keys("Ahmedabad")
time.sleep(3)

#Attendence
Attendence_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[3]/div[1]/div/input"
Attendence_field = driver.find_element(*Attendence_locator)
Attendence_field.send_keys("100")
time.sleep(3)

#Budget
budget_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[3]/div[2]/div/input"
budget_field = driver.find_element(*budget_locator)
budget_field.send_keys("12000")
time.sleep(3)

# #for scrolldown all
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)

#for scrolldown one step
driver.execute_script("window.scrollTo(0,300);")
time.sleep(3)

#venue_type
venue_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/input[1]"
venue_field = driver.find_element(*venue_locator)
venue_field.click()
time.sleep(3)

# Event Duration
ed_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[4]/div[1]/div/input"
ed_field = driver.find_element(*ed_locator)
ed_field.send_keys("1")
time.sleep(3)

# Event Time
et_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[4]/div[2]/div/input"
# et_field = driver.find_element(*et_locator)
# et_field.send_keys("20-11-2021")
# time.sleep(3)
date=driver.find_element(*et_locator)
action:ActionChains=ActionChains(driver)
action.click(date)
action.send_keys("10112021")
action.send_keys(Keys.TAB)
action.send_keys("0330")
action.send_keys("P")
action.perform()
time.sleep(3)

#for scrolldown one step
driver.execute_script("window.scrollTo(300,600);")
time.sleep(3)

# choose event type
cet_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/input[5]"
cet_field = driver.find_element(*cet_locator)
cet_field.click()
time.sleep(3)

# Description
dn_locator= By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[5]/textarea"
dn_field = driver.find_element(*dn_locator)
dn_field.send_keys("I went to require event manager for my son wedding")
time.sleep(3)

#for scrolldown one step
driver.execute_script("window.scrollTo(600,900);")
time.sleep(3)

#final submit 
sub_button = By.XPATH, "/html/body/div/div[1]/div[2]/div/form/div[6]/input"
driver.find_element(*sub_button).click()
time.sleep(3)

#driver.quit()

