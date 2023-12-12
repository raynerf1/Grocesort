from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = 'https://www.dia.es/'
driver = webdriver.Firefox()
driver.get(url)
sleep(3)

ArrayProductos = ["Leche", "Aceite", "Pan", 'Cafe', 'Huevo']


driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/input').send_keys('Leche')

sleep(3)
driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/input').send_keys(Keys.CONTROL, 'a', Keys.DELETE)