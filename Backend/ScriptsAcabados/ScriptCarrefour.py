from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unicodedata

url = 'https://www.carrefour.es/?q=L'
driver = webdriver.Firefox()
driver.get(url)
sleep(3)

ArrayProductos = ["Brick leche carrefour", "Aceite", "Pan", 'Cafe', 'Huevo']

for ProductoABuscar in ArrayProductos:
    driver.find_element("css selector", 'input.ebx-search-box__input:nth-child(3)').send_keys(Keys.CONTROL, 'a', Keys.DELETE)
    driver.find_element("xpath", '/html/body/section/header/div[1]/div/input[3]').send_keys(ProductoABuscar)
    sleep(3)

    casilla=0
    error=False
    while not error and casilla < 10:
        try:
            casilla = casilla + 1
            if casilla == 3:
                casilla = 4
            if casilla == 6:
                casilla = 7
            xpathNombreProducto = '/html/body/section/main/div/section/section/article[' + str(casilla) + ']/div/div[3]/a/h1'
            xpathPrecioProducto = '/html/body/section/main/div/section/section/article[' + str(casilla) + ']/div/p/strong'

            NombreProductoDFE = driver.find_element("xpath", xpathNombreProducto)
            PrecioProductoDFE = driver.find_element("xpath", xpathPrecioProducto)

            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
            PrecioProducto = PrecioProductoDFE.text[:-1]
            print(NombreProducto + ' ' + PrecioProducto)
        except:
            print("No hay más precios para revisar")
driver.quit()