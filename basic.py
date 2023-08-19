import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opts)


driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()

valid_data={"admin":"manager","trainee":"trainee"}

username="admin"
password="manager"

assert username in valid_data,"invalid user name"
driver.find_element("name","username").send_keys(username)
time.sleep(1)

assert password==valid_data[username],"invalid password"
driver.find_element("name","pwd").send_keys(password)

driver.find_element("xpath",'//div[text()="Login "]').click()