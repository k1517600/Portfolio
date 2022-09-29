from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser
import os


driver = webdriver.Edge(executable_path="C:\\Users\\k1517600\\Desktop\\edgedriver_win64\\msedgedriver.exe")
driver.get("https://login.katyisd.org/app/katyisd_mykatycloud_1/exk1dttjo5AcJmPwc697/sso/saml")

driver.implicitly_wait(5)

text_field = driver.find_element(By.ID, "input27")

login_button = driver.find_element(By.CLASS_NAME, "button-primary")
login_button.click()
