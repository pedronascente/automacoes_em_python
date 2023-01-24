import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
service = Service(
    executable_path=r'C:\Users\desenvolvimento\Documents\geckodriver-v0.32.0-win32\geckodriver.exe')
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver = webdriver.Firefox(service=service, options=options)


driver.get('https://estrelabet.com/ptb/bet/main')

time.sleep(5)


aceito_termos = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/a[2]')

time.sleep(10)
aceito_termos.click()

print('fim')
