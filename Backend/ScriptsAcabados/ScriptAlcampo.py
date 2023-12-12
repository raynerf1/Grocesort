from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unicodedata  # Importa el módulo unicodedata para manejar la codificación de caracteres

url = 'https://www.compraonline.alcampo.es/'
driver = webdriver.Firefox()
driver.get(url)
sleep(3)

ArrayProductos = ["Producto alcampo Leche", "Aceite", "Pan", 'Cafe', 'Huevo']

for ProductoABuscar in ArrayProductos:
    driver.find_element("xpath", '//*[@id="search"]').clear()
    driver.find_element("xpath", '//*[@id="search"]').send_keys(ProductoABuscar)
    driver.find_element("xpath", '//*[@id="search"]').send_keys(Keys.ENTER)
    sleep(3)
    casilla = 0
    error = False
    while not error and casilla < 10:
        try:
            casilla = casilla + 1

            XPathNombreProducto = '/html/body/div[1]/div/div[1]/div[2]/main/div[2]/div/div/div[2]/div/div/div[' + str(
                casilla) + ']/div[2]/div[2]/div[1]/h3/a'
            XPathSelectorPrecio = '/html/body/div[1]/div/div[1]/div[2]/main/div[2]/div/div/div[2]/div/div/div[' + str(
                casilla) + ']/div[2]/div[2]/div[1]/div[3]/strong'

            NombreProductoDFE = driver.find_element("xpath", XPathNombreProducto)
            PrecioProductoDFE = driver.find_element("xpath", XPathSelectorPrecio)

            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
            PrecioProducto = PrecioProductoDFE.text[:-1]

            print(NombreProducto + ' ' + PrecioProducto)
        except:
            print('No hay más precios para revisar')
driver.quit()
