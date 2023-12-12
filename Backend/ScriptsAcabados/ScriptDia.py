from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unicodedata
url = 'https://www.dia.es/'
driver = webdriver.Firefox()
driver.get(url)
sleep(3)

ArrayProductos = ["Leche", "Aceite", "Pan", 'Cafe', 'Huevo']

for ProductoABuscar in ArrayProductos:
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/input').send_keys(Keys.CONTROL, 'a', Keys.DELETE)
    driver.find_element("xpath", '/html/body/div[1]/div/div/div/div[1]/div[1]/div[2]/div/input').send_keys(ProductoABuscar)

    casilla=0
    error=False
    sleep(3)
    while not error and casilla < 10:
        try:
            casilla = casilla + 1
            if casilla == 8:
                casilla = 9
            CssSelectorNombreProducto = 'li.search-product-card-list__item-container:nth-child(' + str(casilla) + ') > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(2) > p:nth-child(1)'
            CssSelectorPrecio = 'li.search-product-card-list__item-container:nth-child(' + str(casilla) + ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > p:nth-child(1)'

            NombreProductoDFE = driver.find_element("css selector", CssSelectorNombreProducto)
            PrecioProductoDFE = driver.find_element("css selector", CssSelectorPrecio)

            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
            PrecioProducto = PrecioProductoDFE.text[:-1]

            print(NombreProducto + ' ' + PrecioProducto)
        except:
            error=True
            casilla=0
            print('No hay más precios para revisar')
driver.close()
driver.quit()