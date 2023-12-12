from time import sleep
from selenium import webdriver
import unicodedata
url = 'https://tienda.mercadona.es'
driver = webdriver.Firefox()
driver.get(url)
sleep(3)
driver.find_element("xpath", '//*[@id="root"]/div[5]/div/div[2]/div/form/div/input').send_keys('28051/n')
driver.find_element("xpath", '//*[@id="root"]/div[5]/div/div[2]/div/form/button').click()
sleep(3)
# Lista de productos a buscar
ArrayProductos = ["Pan", "Aceite", "Leche", 'Cafe', 'Huevos']

# Ciclo para buscar cada producto en el array
for ProductoABuscar in ArrayProductos:
    driver.find_element("xpath", '//*[@id="search"]').clear()
    driver.find_element("xpath", '//*[@id="search"]').send_keys(ProductoABuscar)
    sleep(3)
    casilla = 0
    error = False

    while not error and casilla<8:
        try:
            casilla = casilla + 1
            producto = 'div.product-cell:nth-child(' + str(casilla) + ') > button:nth-child(1) > div:nth-child(2) > h4:nth-child(1)'
            xpathPrecio = '/html/body/div[1]/div[3]/div[2]/div[1]/div/section/div/div[' + str(casilla) + ']/button/div[2]/div[2]/p[1]'

            ProductoNombre = driver.find_element("css selector", producto)
            elementoPrecio = driver.find_element("xpath", xpathPrecio)
            #sleep(3)

            precio = elementoPrecio.text
            precio = precio[:-1]
            producto = unicodedata.normalize('NFKD', ProductoNombre.text).encode('ascii', 'ignore').decode('utf-8')
            print(producto + ' ' + precio)
            #with open('lista.txt', 'a',  encoding='utf-8') as lista:
                #lista.write(f'{producto}, {precio}\n')
        except:
            error = True
            casilla=0
            print("No hay más precios para revisar")
driver.close()
driver.quit()
