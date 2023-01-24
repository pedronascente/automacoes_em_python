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

# Abrir site
driver.get('https://seguidor.com.br/api.rdstation.v2/')

# Pegar o valor dos campos de entradas
email = driver.find_element(By.ID, 'inputEmail')
password = driver.find_element(By.ID, 'inputPassword')
btn_enviar = driver.find_element(By.CLASS_NAME, 'btn-primary')

# Atribuir valor nos campos imputs
email.send_keys('admin@rd.com.br')
password.send_keys('123')

# Enviar requisição:
btn_enviar.submit()

# Autenticar app
time.sleep(1)
driver.get(
    'https://seguidor.com.br/api.rdstation.v2/app/index.php?app=app.linkadigital')

print('fim')
