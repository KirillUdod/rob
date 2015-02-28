from selenium import webdriver
from selenium.webdriver.support.ui import Select
 
LOGIN = '123'
EMAIL = 'tttw@ga.ru'
PASS = '123'
 
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("http://localhost:8000/auth/register/")
login = browser.find_element_by_id("id_username")
email = browser.find_element_by_id("id_email")
password1 = browser.find_element_by_id("id_password1")
password2 = browser.find_element_by_id("id_password2")
but = browser.find_element_by_css_selector('.button')

login.send_keys(LOGIN)
email.send_keys(EMAIL)
password1.send_keys(PASS)
password2.send_keys(PASS)
but.click()

