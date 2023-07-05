# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# linked in login page
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
time.sleep(3)

# username with email
search_bar = driver.find_element("id", "username")
search_bar.send_keys("mulagura@gmail.com")
search_bar.send_keys(Keys.RETURN)
time.sleep(2)

# password
search_bar2 = driver.find_element("id", "password")
search_bar2.send_keys("10Mse@0152")
search_bar2.send_keys(Keys.RETURN)
time.sleep(2)

# chat minimize, click method
minimize_link = driver.find_element("xpath", "/html/body/div[5]/div[4]/aside/div[1]/header/div[3]/button[2]")
minimize_link.click()
time.sleep(3)

# global search with keyword
search_bar = driver.find_element("xpath", "//input[@aria-label='Search']")
search_bar.send_keys("Ruchika")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
assert "Ruchika" in driver.title
time.sleep(4)

# profile click
profile_me = driver.find_element("id", "ember16")
profile_me.click()
time.sleep(5)

# logout linkedin
logout_me = driver.find_element("css selector", "a[href*='logout']")
logout_me.click()
time.sleep(5)

# Closing the webdriver
driver.close()
