from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unicodedata

url = 'https://supermercado.eroski.es/'
driver = webdriver.Firefox()
driver.get(url)
sleep(3)

ArrayProductos = ["Aceite", "Leche", "Pan", 'Cafe', 'Huevo']

for ProductoABuscar in ArrayProductos:
    driver.get(url)
    sleep(3)
    driver.find_element("xpath", '//*[@id="searchTerm"]').clear
    driver.find_element("xpath", '//*[@id="searchTerm"]').send_keys(ProductoABuscar)
    sleep(1)
    driver.find_element("xpath", '/html/body/header/div[1]/div/div/div[3]/div[2]/div/div[1]/div[3]/form[1]/input[3]').click()
    sleep(3)

    casilla=0
    error=False
    while not error and casilla < 10:
        try:
            casilla = casilla + 1
                        
            xpathNombre = '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[' + str(casilla) + ']/div/div[4]/div[1]/h2[2]/a'
            #CssNombre = 'div.product-item-lineal:nth-child(' + str(casilla) + ') > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > h2:nth-child(3) > a:nth-child(1)'
            xpathPrecio = '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[' + str(casilla) + ']/div/div[4]/div[3]/div[2]/span[2]/span[2]'
            #CssPrecio = 'div.product-item-lineal:nth-child(' + str(casilla) + ') > div:nth-child(1) > div:nth-child(5) > div:nth-child(3) > div:nth-child(2) > span:nth-child(2) > span:nth-child(2)'

            Nombre = driver.find_element("xpath", xpathNombre)
            Precio = driver.find_element("xpath", xpathPrecio)

            NombreProducto = unicodedata.normalize('NFKD', Nombre.text).encode('ascii', 'ignore').decode('utf-8')
            PrecioProducto = Precio.text

            print(NombreProducto+ ' '+ PrecioProducto)
        except:
            try:
                  
                xpathNombre = f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[{casilla}]/div/div[3]/div[1]/h2[2]/a'
                #CssNombre = 'div.product-item-lineal:nth-child(' + str(casilla) + ') > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > h2:nth-child(3) > a:nth-child(1)'
                xpathPrecio = f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[{casilla}]/div/div[3]/div[2]/div[2]/span[2]/span[2]'
                #CssPrecio = 'div.product-item-lineal:nth-child(' + str(casilla) + ') > div:nth-child(1) > div:nth-child(5) > div:nth-child(3) > div:nth-child(2) > span:nth-child(2) > span:nth-child(2)'

                Nombre = driver.find_element("xpath", xpathNombre)
                Precio = driver.find_element("xpath", xpathPrecio)

                NombreProducto = unicodedata.normalize('NFKD', Nombre.text).encode('ascii', 'ignore').decode('utf-8')
                PrecioProducto = Precio.text

                print(NombreProducto+ ' '+ PrecioProducto)
            except:
                print('No hay mas precios para revisar')
#driver.close()
driver.quit()
