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
password_field.send_keys("qwerty123")
time.sleep(3)

#submit 
submit_button = By.XPATH, "/html/body/div/form/button"
driver.find_element(*submit_button).click()
time.sleep(5)

#Logout 

dropdown_locator=By.XPATH,"/html/body/div/div[2]/nav/div/div[2]/ul/li/a/i" 
driver.find_element(*dropdown_locator).click()
time.sleep(4)  

logout_locator=By.XPATH,"/html/body/div/div[2]/nav/div/div[2]/ul/li/div/a[2]"
driver.find_element(*logout_locator).click()
time.sleep(4)

        

driver.quit()

