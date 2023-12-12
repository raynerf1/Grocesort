from time import sleep
from selenium import webdriver
import unicodedata 
url = 'https://www.ahorramas.com/'
driver = webdriver.Firefox()
driver.get(url)
sleep(3)

ArrayProductos = ["Leche Alipende", "Aceite", "Pan", 'Cafe', 'Huevo']

for ProductoABuscar in ArrayProductos:
    driver.find_element("xpath", '/html/body/div[2]/header/nav/div/div[4]/div/div[3]/div/form/input[1]').clear
    driver.find_element("xpath", '/html/body/div[2]/header/nav/div/div[4]/div/div[3]/div/form/input[1]').send_keys(ProductoABuscar)
    driver.find_element("xpath", '/html/body/div[2]/header/nav/div/div[4]/div/div[3]/div/form/button[2]').click()
    sleep(3)

    casilla=0
    error=False

    while not error and casilla<4:
        try:
            casilla = casilla + 1

            xpathNombreProducto='/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/div[4]/div[3]/div[' + str(casilla) + ']/div/div/div[4]/div[4]/a/h2'
            xpathPrecioProducto='/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/div[4]/div[3]/div[' + str(casilla) + ']/div/div/div[4]/div[2]/div[1]/div/span/span'

            NombreProductoDFE = driver.find_element("xpath", xpathNombreProducto)
            PrecioProductoDFE = driver.find_element("xpath", xpathPrecioProducto)

            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
            PrecioProducto = PrecioProductoDFE.text[:-1]
            print(NombreProducto + ' ' +PrecioProducto)
        except:
            error=True
            casilla=0
            print("No hay más precios para revisar")
driver.close()
driver.quit()