from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/Sahar.itzhak/Downloads/Chromedriver/chromedriver")
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
assert "Google" in driver.title

time.sleep(2)
print("Success")
print("I have made some changes!-!")
driver.quit()
