from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox()
driver.get('https://easyseg.com/lp/')

celular = driver.find_element(By.NAME, 'telefone')
enviar = driver.find_element(By.CLASS_NAME, 'formulario-c2c-boton')

celular.send_keys('5192399880')

enviar.click()

# print(driver.page_source)

driver.get('https://accounts.rdstation.com.br/')

email = driver.find_element(By.NAME, 'email')
password = driver.find_element(By.NAME, 'password')

enviar = driver.find_element(
    By.XPATH, '/html/body/div/div/div/div/div[2]/div/form/button')


email.send_keys('adm.linka.pt@gmail.com')
password.send_keys('LINKA1289portugal')

enviar.submit()

time.sleep(4)

driver.get('https://app.rdstation.com.br/dashboard')

time.sleep(4)

driver.get('https://app.rdstation.com.br/segmentation/index')

time.sleep(5)

excluir2 = driver.find_element(
    By.XPATH, '//*[@id="7724337"]')

excluir2.click()
time.sleep(5)


excluir3 = driver.find_element(
    By.XPATH, '/html/body/section/div[2]/div/div[1]/table/tbody/tr[2]/td[3]/div/div/div[3]/div/span')

excluir3.click()

time.sleep(2)

span_excluir_lead = driver.find_element(By.CLASS_NAME, 'sc-euMpXR')
print(span_excluir_lead.text)

time.sleep(2)

campo_input = driver.find_element(
    By.XPATH, '//*[@id="delete-leads-description"]/div[2]/div[2]/div/input').send_keys(span_excluir_lead.text)

campo_checkbox = driver.find_element(
    By.XPATH, '//*[@id="delete-leads-description"]/label/span').click()

time.sleep(3)

btn_excluir = driver.find_element(
    By.XPATH, '//*[@data-testid="deleteLeadsConfirmButton"]').click()

print('fim')
