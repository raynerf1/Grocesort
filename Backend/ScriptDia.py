from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unicodedata
import mysql.connector
from datetime import date
url = 'https://www.dia.es/'
driver = webdriver.Firefox()
driver.get(url)
sleep(3)

FechaActual=date.today()

Supermercado = 'Dia'

ArrayProductos = [
    "Leche", "Yogur", "Mantequilla", 
    'Bebida de almendras', 'Bebida de arroz', 'Bebida de soja', 'Bebida de avena', 
    "Mousse", "Cuajada", "Flan", "Gelatina", "Natillas",
    "Batido de cacao", "Batido de fresa", "Batido de vainilla",
    "Horchata",
    "Zumo naranja", "Zumo pina", "Zumo manzana", "Zumo uva", "Zumo melocoton",
    "Agua",
    "Aceite de oliva", "Aceite de girasol",
    "Vinagre",
    "Sal", "Bicarbonato",
    "Patatas fritas", "Aceitunas", "Frutos secos", "Snacks", "Palomitas", "Galletas saladas",
    "Arroz", "Pasta", "Lasana",
    "Azucar",
    "Cafe",
    "Galletas",
    "Helados",
    "Cereales",
    "Barquillos",
    "Atun", "Bonito", "Mejillones", "Sardinas", "Berberechos",
    "Tomate triturado", "Tomate frito", "Judias verdes", "Pimientos", "Esparragos", "Maiz", "Guisantes", "Champinones", "Alcachofas",
    "Harina", "Levadura",
    "Mermelada de fresa", "Mermelada de melocoton", "Mermelada de naranja", 
    "Miel",
    "Pan", "Pan de molde", "Pan hamburguesa",
    "Tortilla trigo",
    "Tortilla patata",
    "Pizza",
    "Garbanzo", "Alubia",
    "Ketchup", "Mostaza", "Mayonesa",
    "Gazpacho", "Salmorejo",
    "Pollo", "Cerdo", "Vacuno",
    "Huevo"]

mydb = mysql.connector.connect(
  host="hostingmysql335.nominalia.com",
  user="rayner",
  password="marenas19",
  database='bdprecios'
)
mycursor = mydb.cursor()



for indice, ProductoABuscar in enumerate(ArrayProductos):
    PosicionArray = indice
    Grupo = ''
    if 0 <= PosicionArray < 3:
        Grupo = 'Lacteos'
    elif 3 <= PosicionArray <= 6:
        Grupo = 'Bebidas vegetales'
    elif 7 <= PosicionArray <= 11:
        Grupo = 'Postres'
    elif 12 <= PosicionArray <= 14:
        Grupo = 'Batidos'
    elif PosicionArray == 15:
        Grupo = 'Horchata'
    elif 16 <= PosicionArray <= 20:
        Grupo = 'Zumos'
    elif PosicionArray == 21:
        Grupo = 'Agua'    
    elif 22 <= PosicionArray <= 23:
        Grupo = 'Aceite'    
    elif PosicionArray == 24:
        Grupo = 'Vinagre'
    elif PosicionArray == 25:
        Grupo = 'Sal'        
    elif PosicionArray == 26:
        Grupo = 'Bicarbonato'
    elif 27 <= PosicionArray <= 32:
        Grupo = 'Snacks'
    elif PosicionArray == 33:
        Grupo = 'Arroz'
    elif PosicionArray == 34:
        Grupo = 'Pasta'
    elif PosicionArray == 35:
        Grupo = 'Lasana'
    elif PosicionArray == 36:
        Grupo = 'Azucar'
    elif PosicionArray == 37:
        Grupo = 'Cafe'
    elif PosicionArray == 38:
        Grupo = 'Galletas, helados, cereales y dulces'
    elif PosicionArray == 39:
        Grupo = 'Galletas, helados, cereales y dulces'
    elif PosicionArray == 40:
        Grupo = 'Galletas, helados, cereales y dulces'
    elif PosicionArray == 41:
        Grupo = 'Galletas, helados, cereales y dulces'
    elif 42 <= PosicionArray <= 46:
        Grupo = 'Pescados y marisco en conserva'
    elif 47 <= PosicionArray <= 55:
        Grupo = 'Verduras en conserva'
    elif 56 <= PosicionArray <= 57:
        Grupo = 'Harina y levadura'
    elif 58 <= PosicionArray <= 60:
        Grupo = 'Mermelada'
    elif PosicionArray == 61:
        Grupo = 'Miel'
    elif 62 <= PosicionArray <= 64:
        Grupo = 'Panes'
    elif PosicionArray == 65:
        Grupo = 'Tortilla de trigo'
    elif PosicionArray == 66:
        Grupo = 'Platos preparados'
    elif PosicionArray == 67:
        Grupo = 'Pizzas'
    elif 68 <= PosicionArray <= 69:
        Grupo = 'Legumbres'
    elif 70 <= PosicionArray <= 72:
        Grupo = 'Salsas'
    elif 73 <= PosicionArray <= 74:
        Grupo = 'Gazpacho y salmorejo'
    elif PosicionArray > 74:
        Grupo = 'Carnes'

    print('-'*20)    
    print(Grupo)
    print(f"Posicion array {PosicionArray} -> {ProductoABuscar}")

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
            CssSelectorDetalle='li.search-product-card-list__item-container:nth-child(' + str(casilla) + ') > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > p:nth-child(2)'

            NombreProductoDFE = driver.find_element("css selector", CssSelectorNombreProducto)
            PrecioProductoDFE = driver.find_element("css selector", CssSelectorPrecio)
            DetalleProductoDFE = driver.find_element("css selector", CssSelectorDetalle)

            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
            PrecioProducto = PrecioProductoDFE.text[:-1]
            PrecioProducto = PrecioProducto.replace(',', '.')
            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')

            print(NombreProducto + ' ' + PrecioProducto+ ' ' + DetalleProducto)

            sql = "INSERT INTO productos (seccion, subseccion, supermercado, fecha, nombre, precio, precio_unitario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (Grupo, ProductoABuscar, Supermercado, FechaActual, NombreProducto, PrecioProducto, DetalleProducto)

            select_query = "SELECT * FROM productos WHERE seccion = %s AND subseccion = %s AND supermercado = %s AND fecha = %s AND nombre = %s"
            mycursor.execute(select_query, (Grupo, ProductoABuscar, Supermercado, FechaActual, NombreProducto))
            existing_record = mycursor.fetchone()

            if existing_record:
                print("Ya existe un registro en la base de datos con esa fecha, no se creara el registro.")
            else:
                sql = "INSERT INTO productos (seccion, subseccion, supermercado, fecha, nombre, precio, precio_unitario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (Grupo, ProductoABuscar, Supermercado, FechaActual, NombreProducto, PrecioProducto, DetalleProducto)
                mycursor.execute(sql, val)
                mydb.commit()

        except:
            error=True
            casilla=0
            print('No hay más precios para revisar')

mycursor.close()
mydb.close()

driver.close()
driver.quit()