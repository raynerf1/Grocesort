from time import sleep
from selenium import webdriver
url = 'https://tienda.mercadona.es'
driver = webdriver.Firefox()
driver.get(url)
sleep(3)
driver.find_element("xpath", '//*[@id="root"]/div[5]/div/div[2]/div/form/div/input').send_keys('28051/n')
driver.find_element("xpath", '//*[@id="root"]/div[5]/div/div[2]/div/form/button').click()
sleep(3)
driver.find_element("xpath", '//*[@id="search"]').send_keys('Leche entera brick')
sleep(3)
elemento = driver.find_element("xpath", '/html/body/div[1]/div[3]/div[2]/div[1]/div/section/div/div[1]/button/div[2]/div[2]/p[1]')
sleep(3)
precio = elemento.text
precio = precio[:-1]
print(precio)
