import re
from time import sleep
from selenium import webdriver
import unicodedata
from datetime import date
import mysql.connector
from datetime import date, timedelta

FechaActual=date.today()
mydb = mysql.connector.connect(
  host="hostingmysql335.nominalia.com",
  user="grocesort",
  password="raynergrocesort",
  database='externalgrocesort'
)
mycursor = mydb.cursor()
driver = webdriver.Firefox()

def JuntarEnlaceProducto(ListaProductos, supermercadoArchivosEnlaces, archivoConEnlacesProductos):
    productos_array = []
    with open(ListaProductos, 'r') as Productos:
        for i in Productos:
            producto = "[" + i.strip().replace(",", "")[1:-1] + "]"
            productos_array.append(producto)
            #print(producto)
    #print(productos_array)
    with open(supermercadoArchivosEnlaces, 'r') as Enlaces, open(archivoConEnlacesProductos, 'w') as Finales:
        for i, linea_enlace in enumerate(Enlaces):
                linea_producto = productos_array[i]
                linea_final = linea_enlace.strip() + " " + linea_producto
                print(linea_final)
                Finales.write(linea_final + '\n')
    Finales.close
    Productos.close
    Enlaces.close

def ActualizarPrecios (SupermercadoEnlaces):
    print("Leyendo "+SupermercadoEnlaces)
    CPIntroducidoMercadona = False 
    with open(SupermercadoEnlaces, 'r') as Productos:
        for i, linea in enumerate(Productos, 1):  # Usa enumerate para obtener el número de línea
            # Utiliza expresiones regulares para extraer los valores entre comillas y corchetes
            match = re.match(r'"(.*?)"\s*,\s*\[(.*?)\]', linea)
            if match:
                enlace = match.group(1)
                descripcion = match.group(2)
                print(f"{i}")
                print("Enlace: " +enlace)
                print("Descripcion: " +descripcion)
                
                consultasql = 'SELECT seccion from productos where producto=%s LIMIT 1'
                marcador = (descripcion,)
                mycursor.execute(consultasql, marcador)
                result = mycursor.fetchone()
                if result is not None:
                    seccion = result[0]
                    print("Seccion: " +seccion)
                
                if enlace !="Vacio":
                    if SupermercadoEnlaces == "Alcampo_enlaces.txt":
                        Supermercado = "Alcampo"
                        driver.get(enlace)
                        sleep(1)
                        try: 
                            DescripcionXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[3]/div/div[1]/h1'
                            PrecioXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[3]/div/div[1]/div[2]/span'
                            DetalleXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[3]/div/div[1]/div[1]/span[3]'
                            imagenSRCXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[2]/div/div/div/div/div/div/div/div/div/img'
                                            
                            NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                            PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                            DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                            ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
                            

                            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                            PrecioProducto = PrecioProductoDFE.text[:-1]
                            PrecioProducto = PrecioProducto.replace(',', '.')
                            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')

                            sql = 'SELECT id from productos where producto = %s and descripcion = %s and supermercado = %s'
                            val = (descripcion, NombreProducto, Supermercado)
                            mycursor.execute(sql, val)
                            result = mycursor.fetchone()
                            if result is not None:
                                id = result[0]
                                print("ID encontrado:", id)
                                sql = "INSERT INTO precios (id, producto, supermercado, precio, detalle, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
                                val = (id, descripcion, Supermercado, PrecioProducto, DetalleProducto, FechaActual)
                                try:
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print(f"Se insertó en la base de datos el precio del producto con id: {id}")
                                except Exception as e:
                                    mydb.rollback()
                                    print(f"Error durante la inserción en la base de datos: {e}")
                                
                            else:
                                id = None
                                print("No se encontró un ID para los criterios proporcionados.")
                            
                        except Exception as ex:
                            print("Enlace caido o no se pudo entrar acceder al enlace")
                    
                    if SupermercadoEnlaces == "AhorraMas_enlaces.txt":
                        Supermercado = "Ahorra Mas"
                        driver.get(enlace)
                        sleep(1)
                        NombreProducto = None         
                        PrecioProducto = None
                        DetalleProducto = None
                        try: 
                            DescripcionXPath = '/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div[2]/p'
                            PrecioXPath = '/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div/span/span'
                            DetalleXPath = '/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/span'
                            imagenSRCXPath = '/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div[1]/div/img'
                                            

                            NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                            PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                            DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                            ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
                            

                            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                            PrecioProducto = PrecioProductoDFE.text[:-1]
                            PrecioProducto = PrecioProducto.replace(',', '.')
                            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                            ImagenSRC = ImagenDFE.get_attribute("src")

                        except:
                            try:    
                                DescripcionXPath = '/html/body/div[2]/div[3]/div[1]/div[3]/div[2]/p'
                                PrecioXPath = '/html/body/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div[1]/div/span/span'
                                DetalleXPath = '/html/body/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div[2]/span'
                                imagenSRCXPath = '/html/body/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/div[1]/div/img'

                                NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                                PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                                DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                                ImagenDFE = driver.find_element("xpath", imagenSRCXPath)

                                NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                                PrecioProducto = PrecioProductoDFE.text[:-1]
                                PrecioProducto = PrecioProducto.replace(',', '.')
                                DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                                ImagenSRC = ImagenDFE.get_attribute("src")
                            except:
                                print("Enlace caido")
                        
                        finally:
                            if NombreProducto is not None:
                                sql = 'SELECT id from productos where producto = %s and descripcion = %s and supermercado = %s'
                                val = (descripcion, NombreProducto, Supermercado)
                                mycursor.execute(sql, val)
                                result = mycursor.fetchone()
                                if result is not None:
                                    id = result[0]
                                    print("ID encontrado:", id)
                                    sql = "INSERT INTO precios (id, producto, supermercado, precio, detalle, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
                                    val = (id, descripcion, Supermercado, PrecioProducto, DetalleProducto, FechaActual)
                                    try:
                                        mycursor.execute(sql, val)
                                        mydb.commit()
                                        print(f"Se insertó en la base de datos el precio del producto con id: {id}")
                                    except Exception as e:
                                        mydb.rollback()
                                        print(f"Error durante la inserción en la base de datos: {e}")
                                else:
                                    id = None
                                    print("No se encontró un ID para los criterios proporcionados.")
        
                    if SupermercadoEnlaces == "Carrefour_enlaces.txt":
                        Supermercado = "Carrefour"
                        driver.get(enlace)
                        sleep(1)
                        try:
                            DescripcionXPath = '/html/body/div[2]/div/main/div[1]/div[1]/h1'
                            PrecioXPath = '/html/body/div[2]/div/main/div[2]/div[1]/div/div/div[1]/div[1]/span'
                            DetalleXPath = '/html/body/div[2]/div/main/div[2]/div[1]/div/div/div[1]/div[1]/div/span'
                            imagenSRCXPath = '/html/body/div[2]/div/main/div[1]/div[2]/div/div/div/div/div/div/div/img[2]'         

                            NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                            PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                            DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                            ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
                            
                            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                            PrecioProducto = PrecioProductoDFE.text[:-1]
                            PrecioProducto = PrecioProducto.replace(',', '.')
                            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                            ImagenSRC = ImagenDFE.get_attribute("src")

                            sql = 'SELECT id from productos where producto = %s and descripcion = %s and supermercado = %s'
                            val = (descripcion, NombreProducto, Supermercado)
                            mycursor.execute(sql, val)
                            result = mycursor.fetchone()

                            if result is not None:
                                id = result[0]
                                print("ID encontrado:", id)
                                sql = "INSERT INTO precios (id, producto, supermercado, precio, detalle, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
                                val = (id, descripcion, Supermercado, PrecioProducto, DetalleProducto, FechaActual)
                                try:
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print(f"Se insertó en la base de datos el precio del producto con id: {id}")
                                except Exception as e:
                                    mydb.rollback()
                                    print(f"Error durante la inserción en la base de datos: {e}")
                            else:
                                id = None
                                print("No se encontró un ID para los criterios proporcionados.")
                        except:
                            print("Enlace caido o no se pudo entrar acceder al enlace")

                    if SupermercadoEnlaces == "Dia_enlaces.txt":
                        Supermercado = "Dia"
                        driver.get(enlace)
                        sleep(1)
                        try:
                            DescripcionXPath = '/html/body/div[1]/div/div/div/div[2]/div[2]/div/h1'
                            PrecioXPath = '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/p[1]'
                            DetalleXPath = '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/p[2]'
                            imagenSRCXPath = '/html/body/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/img[1]'
                                            
                            NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                            PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                            DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                            ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
                            
                            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                            PrecioProducto = PrecioProductoDFE.text[:-1]
                            PrecioProducto = PrecioProducto.replace(',', '.')
                            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                            ImagenSRC = ImagenDFE.get_attribute("src")

                            sql = 'SELECT id from productos where producto = %s and descripcion = %s and supermercado = %s'
                            val = (descripcion, NombreProducto, Supermercado)
                            mycursor.execute(sql, val)
                            result = mycursor.fetchone()
                            if result is not None:
                                id = result[0]
                                print("ID encontrado:", id)
                                sql = "INSERT INTO precios (id, producto, supermercado, precio, detalle, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
                                val = (id, descripcion, Supermercado, PrecioProducto, DetalleProducto, FechaActual)
                                try:
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print(f"Se insertó en la base de datos el precio del producto con id: {id}")
                                except Exception as e:
                                    mydb.rollback()
                                    print(f"Error durante la inserción en la base de datos: {e}")
                                
                            else:
                                id = None
                                print("No se encontró un ID para los criterios proporcionados.")
                        except:
                            print("Enlace caido o no se pudo entrar acceder al enlace")
                    if SupermercadoEnlaces == "Eroski_enlaces.txt":
                        Supermercado = "Eroski"
                        driver.get(enlace)
                        sleep(1)
                        try:
                            DescripcionXPath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/h1'
                            PrecioXPath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/div[5]/div[2]/span[2]/span[2]'
                            #DetalleXPath = ''
                            imagenSRCXPath = '/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/img'
                                            
                            NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                            PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                            #DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                            ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
                            
                            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                            PrecioProducto = PrecioProductoDFE.text
                            PrecioProducto = PrecioProducto.replace(',', '.')
                            #DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                            ImagenSRC = ImagenDFE.get_attribute("src")

                            sql = 'SELECT id from productos where producto = %s and descripcion = %s and supermercado = %s'
                            val = (descripcion, NombreProducto, Supermercado)
                            mycursor.execute(sql, val)
                            result = mycursor.fetchone()
                            if result is not None:
                                id = result[0]
                                print("ID encontrado:", id)
                                sql = "INSERT INTO precios (id, producto, supermercado, precio, detalle, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
                                val = (id, descripcion, Supermercado, PrecioProducto, '', FechaActual)
                                try:
                                    mycursor.execute(sql, val)
                                    mydb.commit()
                                    print(f"Se insertó en la base de datos el precio del producto con id: {id}")
                                except Exception as e:
                                    mydb.rollback()
                                    print(f"Error durante la inserción en la base de datos: {e}")
                            else:
                                id = None
                                print("No se encontró un ID para los criterios proporcionados.")
                        except Exception as ex:
                            print("Enlace caido o no se pudo entrar acceder al enlace")
                       
                    if SupermercadoEnlaces == "Mercadona_enlaces.txt":
                        Supermercado = "Mercadona"
                        driver.get(enlace)
                        sleep(1)
                        
                        if CPIntroducidoMercadona == False:
                            driver.find_element("xpath", '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/form/div/input').send_keys('28051/n')
                            driver.find_element("xpath", '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/form/button').click()
                            CPIntroducidoMercadona = True    
                            driver.get(enlace)
                            sleep(2)

                        NombreProducto = None         
                        PrecioProducto = None
                        DetalleProducto = None
                        try:
                            DescripcionXPath = '.title2-r'
                            PrecioXPath = '.large-b'
                            DetalleXPath = 'span.headline1-r:nth-child(2)'
                            imagenSRCXPath = '.image-zoomer__source > img:nth-child(1)'

                            NombreProductoDFE = driver.find_element("css selector", DescripcionXPath)
                            PrecioProductoDFE = driver.find_element("css selector", PrecioXPath)
                            DetalleProductoDFE = driver.find_element("css selector", DetalleXPath)
                            ImagenDFE = driver.find_element("css selector", imagenSRCXPath)
                            

                            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                            PrecioProducto = PrecioProductoDFE.text[:-1]
                            PrecioProducto = PrecioProducto.replace(',', '.')
                            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                            ImagenSRC = ImagenDFE.get_attribute("src")
                        except:
                            try:
                                DescripcionXPath = '.title2-r'
                                PrecioXPath = '.large-b'
                                DetalleXPath = 'span.headline1-r:nth-child(2)'
                                imagenSRCXPath = '.image-zoomer__source > img:nth-child(1)'

                                NombreProductoDFE = driver.find_element("css selector", DescripcionXPath)
                                PrecioProductoDFE = driver.find_element("css selector", PrecioXPath)
                                DetalleProductoDFE = driver.find_element("css selector", DetalleXPath)
                                ImagenDFE = driver.find_element("css selector", imagenSRCXPath)
                                

                                NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                                PrecioProducto = PrecioProductoDFE.text[:-1]
                                PrecioProducto = PrecioProducto.replace(',', '.')
                                DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                                ImagenSRC = ImagenDFE.get_attribute("src")
                            except:
                                try:
                                    DescripcionXPath = '.title2-r'
                                    PrecioXPath = '.large-b'
                                    DetalleXPath = 'span.headline1-r:nth-child(1)'
                                    imagenSRCXPath = '.image-zoomer__source > img:nth-child(1)'

                                    NombreProductoDFE = driver.find_element("css selector", DescripcionXPath)
                                    PrecioProductoDFE = driver.find_element("css selector", PrecioXPath)
                                    DetalleProductoDFE = driver.find_element("css selector", DetalleXPath)
                                    ImagenDFE = driver.find_element("css selector", imagenSRCXPath)
                                    

                                    NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                                    PrecioProducto = PrecioProductoDFE.text[:-1]
                                    PrecioProducto = PrecioProducto.replace(',', '.')
                                    DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                                    ImagenSRC = ImagenDFE.get_attribute("src")
                                except Exception as ex:
                                    print("Enlace caido o no se pudo entrar acceder al enlace")
                        finally:
                            if NombreProducto is not None:
                                sql = 'SELECT id from productos where producto = %s and descripcion = %s and supermercado = %s'
                                val = (descripcion, NombreProducto, Supermercado)
                                mycursor.execute(sql, val)
                                result = mycursor.fetchone()
                                if result is not None:
                                    id = result[0]
                                    print("ID encontrado:", id)
                                    sql = "INSERT INTO precios (id, producto, supermercado, precio, detalle, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
                                    val = (id, descripcion, Supermercado, PrecioProducto, DetalleProducto, FechaActual)
                                    try:
                                        mycursor.execute(sql, val)
                                        mydb.commit()
                                        print(f"Se insertó en la base de datos el precio del producto con id: {id}")
                                    except Exception as e:
                                        mydb.rollback()
                                        print(f"Error durante la inserción en la base de datos: {e}")
                                else:
                                    id = None
                                    print("No se encontró un ID para los criterios proporcionados.")

                else:
                    print("Enlace vacío")       
                
                #enlaces.append(enlace)
                #productoDescripcion.append(descripcion)
    mycursor.close()
    mydb.close()
    driver.close() 
    driver.quit()

def CrearProductos (SupermercadoEnlaces):
    print("Leyendo "+SupermercadoEnlaces)
    CPIntroducidoMercadona = False
    with open(SupermercadoEnlaces, 'r') as Productos:
        for i, linea in enumerate(Productos, 1):  # Usa enumerate para obtener el número de línea
            # Utiliza expresiones regulares para extraer los valores entre comillas y corchetes
            match = re.match(r'"(.*?)"\s*,\s*\[(.*?)\]', linea)
            if match:
                enlace = match.group(1)
                descripcion = match.group(2)
                print(f"{i}")
                print("Enlace: " +enlace)
                print("Descripcion: " +descripcion)
                if enlace !="Vacio":
                    if SupermercadoEnlaces == "AhorraMas_enlaces.txt":
                        Supermercado = "Ahorra Mas"
                        driver.get(enlace)
                        sleep(1)
                        NombreProducto = None         
                        PrecioProducto = None
                        DetalleProducto = None
                        try: 
                                DescripcionXPath = '/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div[2]/p'
                                PrecioXPath = '/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[1]/div/span/span'
                                DetalleXPath = '/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/span'
                                imagenSRCXPath = '/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div[1]/div/img'
                                                
                                NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                                PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                                DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                                ImagenDFE = driver.find_element("xpath", imagenSRCXPath)

                                NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                                PrecioProducto = PrecioProductoDFE.text[:-1]
                                PrecioProducto = PrecioProducto.replace(',', '.')
                                DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                                ImagenSRC = ImagenDFE.get_attribute("src")

                        except:
                                try:    
                                    DescripcionXPath = '/html/body/div[2]/div[3]/div[1]/div[3]/div[2]/p'
                                    PrecioXPath = '/html/body/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div[1]/div/span/span'
                                    DetalleXPath = '/html/body/div[2]/div[3]/div[1]/div[3]/div[2]/div[2]/div[2]/span'
                                    imagenSRCXPath = '/html/body/div[2]/div[3]/div[1]/div[3]/div[1]/div/div/div[1]/div/img'

                                    NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                                    PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                                    DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                                    ImagenDFE = driver.find_element("xpath", imagenSRCXPath)

                                    NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                                    PrecioProducto = PrecioProductoDFE.text[:-1]
                                    PrecioProducto = PrecioProducto.replace(',', '.')
                                    DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                                    ImagenSRC = ImagenDFE.get_attribute("src")
                                except:
                                    print("Enlace caido")
                            
                        finally:
                                if NombreProducto is not None:
                                    sql = 'SELECT seccion, subseccion from backendassist where producto = %s'
                                    val = (descripcion,)
                                    mycursor.execute(sql, val)
                                    result = mycursor.fetchone()
                                    seccionsql = None
                                    subseccionsql = None
                                    if result is not None:
                                        seccionsql, subseccionsql = result
                                        print("Seccion encontrada:", seccionsql)
                                        print("Subseccion encontrada:", subseccionsql)
                                        sql = 'SELECT id from productos where seccion = %s and subseccion = %s and producto = %s and descripcion = %s and supermercado = %s and enlace = %s'
                                        val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, enlace)
                                        try:
                                            mycursor.execute(sql, val)
                                            result = mycursor.fetchone()
                                            id = None
                                            if result is not None:
                                                id = result
                                                print(f"Ya hay un producto con esos valores. Id: {id}")
                                            if result is None:
                                                sql = 'INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen, enlace) VALUES (%s, %s, %s, %s, %s, %s, %s)'
                                                val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, ImagenSRC, enlace)
                                                try:
                                                    mycursor.execute(sql, val)
                                                    mydb.commit()
                                                    print(f"Se insertó en la base de datos el producto {descripcion} del supermercado {Supermercado}")
                                                except Exception as e:
                                                    mydb.rollback()
                                                    print(f"Error durante la inserción en la base de datos: {e}")
                                        except Exception as e:
                                            mydb.rollback()
                                            print(f"Error durante la búsqueda en la base de datos: {e}")
                                    else:
                                        id = None
                                        print("No se encontró una subsección para los criterios proporcionados.")
                                        
                    if SupermercadoEnlaces == "Alcampo_enlaces.txt":
                        Supermercado = "Alcampo"
                        driver.get(enlace)
                        sleep(1)
                        NombreProducto = None         
                        PrecioProducto = None
                        DetalleProducto = None
                        try: 
                                DescripcionXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[3]/div/div[1]/h1'
                                PrecioXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[3]/div/div[1]/div[2]/span'
                                DetalleXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[3]/div/div[1]/div[1]/span[3]'
                                imagenSRCXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[2]/div/div/div/div/div/div/div/div/div/img'
                                                
                                NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                                PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                                DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                                ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
                                
                                NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                                PrecioProducto = PrecioProductoDFE.text[:-1]
                                PrecioProducto = PrecioProducto.replace(',', '.')
                                DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                                ImagenSRC = ImagenDFE.get_attribute("src")
                                
                        except Exception as ex:
                                print("Enlace caido o no se pudo entrar acceder al enlace")
                        finally:
                            if NombreProducto is not None:
                                        sql = 'SELECT seccion, subseccion from backendassist where producto = %s'
                                        val = (descripcion,)
                                        mycursor.execute(sql, val)
                                        result = mycursor.fetchone()
                                        seccionsql = None
                                        subseccionsql = None
                                        if result is not None:
                                            seccionsql, subseccionsql = result
                                            print("Seccion encontrada:", seccionsql)
                                            print("Subseccion encontrada:", subseccionsql)
                                            sql = 'SELECT id from productos where seccion = %s and subseccion = %s and producto = %s and descripcion = %s and supermercado = %s and enlace = %s'
                                            val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, enlace)
                                            try:
                                                mycursor.execute(sql, val)
                                                result = mycursor.fetchone()
                                                id = None
                                                if result is not None:
                                                    id = result
                                                    print(f"Ya hay un producto con esos valores. Id: {id}")
                                                if result is None:
                                                    sql = 'INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen, enlace) VALUES (%s, %s, %s, %s, %s, %s, %s)'
                                                    val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, ImagenSRC, enlace)
                                                    try:
                                                        mycursor.execute(sql, val)
                                                        mydb.commit()
                                                        print(f"Se insertó en la base de datos el producto {descripcion} del supermercado {Supermercado}")
                                                    except Exception as e:
                                                        mydb.rollback()
                                                        print(f"Error durante la inserción en la base de datos: {e}")
                                            except Exception as e:
                                                mydb.rollback()
                                                print(f"Error durante la búsqueda en la base de datos: {e}")
                                        else:
                                            id = None
                                            print("No se encontró una subsección para los criterios proporcionados.")

                    if SupermercadoEnlaces == "Carrefour_enlaces.txt":
                        Supermercado = "Carrefour"
                        driver.get(enlace)
                        sleep(1)
                        NombreProducto = None         
                        PrecioProducto = None
                        DetalleProducto = None
                        try:
                            DescripcionXPath = '/html/body/div[2]/div/main/div[1]/div[1]/h1'
                            PrecioXPath = '/html/body/div[2]/div/main/div[2]/div[1]/div/div/div[1]/div[1]/span'
                            DetalleXPath = '/html/body/div[2]/div/main/div[2]/div[1]/div/div/div[1]/div[1]/div/span'
                            imagenSRCXPath = '/html/body/div[2]/div/main/div[1]/div[2]/div/div/div/div/div/div/div/img[2]'         

                            NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                            PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                            DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                            ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
                            
                            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                            PrecioProducto = PrecioProductoDFE.text[:-1]
                            PrecioProducto = PrecioProducto.replace(',', '.')
                            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                            ImagenSRC = ImagenDFE.get_attribute("src")

                        except:
                            print("Enlace caido o no se pudo entrar acceder al enlace")
                            NombreProducto = None         
                            PrecioProducto = None
                            DetalleProducto = None
                        finally:
                            if NombreProducto is not None:
                                        sql = 'SELECT seccion, subseccion from backendassist where producto = %s'
                                        val = (descripcion,)
                                        mycursor.execute(sql, val)
                                        result = mycursor.fetchone()
                                        seccionsql = None
                                        subseccionsql = None
                                        if result is not None:
                                            seccionsql, subseccionsql = result
                                            print("Seccion encontrada:", seccionsql)
                                            print("Subseccion encontrada:", subseccionsql)
                                            sql = 'SELECT id from productos where seccion = %s and subseccion = %s and producto = %s and descripcion = %s and supermercado = %s and enlace = %s'
                                            val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, enlace)
                                            try:
                                                mycursor.execute(sql, val)
                                                result = mycursor.fetchone()
                                                id = None
                                                if result is not None:
                                                    id = result
                                                    print(f"Ya hay un producto con esos valores. Id: {id}")
                                                if result is None:
                                                    sql = 'INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen, enlace) VALUES (%s, %s, %s, %s, %s, %s, %s)'
                                                    val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, ImagenSRC, enlace)
                                                    try:
                                                        mycursor.execute(sql, val)
                                                        mydb.commit()
                                                        print(f"Se insertó en la base de datos el producto {descripcion} del supermercado {Supermercado}")
                                                    except Exception as e:
                                                        mydb.rollback()
                                                        print(f"Error durante la inserción en la base de datos: {e}")
                                            except Exception as e:
                                                mydb.rollback()
                                                print(f"Error durante la búsqueda en la base de datos: {e}")
                                        else:
                                            id = None
                                            print("No se encontró una subsección para los criterios proporcionados.")

                    if SupermercadoEnlaces == "Dia_enlaces.txt":
                        Supermercado = "Dia"
                        driver.get(enlace)
                        sleep(1)
                        NombreProducto = None         
                        PrecioProducto = None
                        DetalleProducto = None
                        try:
                            DescripcionXPath = '/html/body/div[1]/div/div/div/div[2]/div[2]/div/h1'
                            PrecioXPath = '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/p[1]'
                            DetalleXPath = '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/p[2]'
                            imagenSRCXPath = '/html/body/div[1]/div/div/div/div[2]/div[1]/div[3]/div/div/div/img[1]'
                                            
                            NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                            PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                            DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                            ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
                            
                            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                            PrecioProducto = PrecioProductoDFE.text[:-1]
                            PrecioProducto = PrecioProducto.replace(',', '.')
                            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                            ImagenSRC = ImagenDFE.get_attribute("src")

                        except:
                            print("Enlace caido o no se pudo entrar acceder al enlace")
                        finally:
                            if NombreProducto is not None:
                                        sql = 'SELECT seccion, subseccion from backendassist where producto = %s'
                                        val = (descripcion,)
                                        mycursor.execute(sql, val)
                                        result = mycursor.fetchone()
                                        seccionsql = None
                                        subseccionsql = None
                                        if result is not None:
                                            seccionsql, subseccionsql = result
                                            print("Seccion encontrada:", seccionsql)
                                            print("Subseccion encontrada:", subseccionsql)
                                            sql = 'SELECT id from productos where seccion = %s and subseccion = %s and producto = %s and descripcion = %s and supermercado = %s and enlace = %s'
                                            val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, enlace)
                                            try:
                                                mycursor.execute(sql, val)
                                                result = mycursor.fetchone()
                                                id = None
                                                if result is not None:
                                                    id = result
                                                    print(f"Ya hay un producto con esos valores. Id: {id}")
                                                if result is None:
                                                    sql = 'INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen, enlace) VALUES (%s, %s, %s, %s, %s, %s, %s)'
                                                    val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, ImagenSRC, enlace)
                                                    try:
                                                        mycursor.execute(sql, val)
                                                        mydb.commit()
                                                        print(f"Se insertó en la base de datos el producto {descripcion} del supermercado {Supermercado}")
                                                    except Exception as e:
                                                        mydb.rollback()
                                                        print(f"Error durante la inserción en la base de datos: {e}")
                                            except Exception as e:
                                                mydb.rollback()
                                                print(f"Error durante la búsqueda en la base de datos: {e}")
                                        else:
                                            id = None
                                            print("No se encontró una subsección para los criterios proporcionados.")

                    if SupermercadoEnlaces == "Eroski_enlaces.txt":
                        Supermercado = "Eroski"
                        driver.get(enlace)
                        sleep(1)
                        NombreProducto = None         
                        PrecioProducto = None
                        DetalleProducto = None
                        try:
                            DescripcionXPath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/h1'
                            PrecioXPath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/div[5]/div[2]/span[2]/span[2]'
                            #DetalleXPath = ''
                            imagenSRCXPath = '/html/body/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/img'
                                            
                            NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
                            PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
                            #DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
                            ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
                            
                            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                            PrecioProducto = PrecioProductoDFE.text
                            PrecioProducto = PrecioProducto.replace(',', '.')
                            #DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                            ImagenSRC = ImagenDFE.get_attribute("src")

                        except Exception as ex:
                            print("Enlace caido o no se pudo entrar acceder al enlace")
                        finally:
                            if NombreProducto is not None:
                                        sql = 'SELECT seccion, subseccion from backendassist where producto = %s'
                                        val = (descripcion,)
                                        mycursor.execute(sql, val)
                                        result = mycursor.fetchone()
                                        seccionsql = None
                                        subseccionsql = None
                                        if result is not None:
                                            seccionsql, subseccionsql = result
                                            print("Seccion encontrada:", seccionsql)
                                            print("Subseccion encontrada:", subseccionsql)
                                            sql = 'SELECT id from productos where seccion = %s and subseccion = %s and producto = %s and descripcion = %s and supermercado = %s and enlace = %s'
                                            val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, enlace)
                                            try:
                                                mycursor.execute(sql, val)
                                                result = mycursor.fetchone()
                                                id = None
                                                if result is not None:
                                                    id = result
                                                    print(f"Ya hay un producto con esos valores. Id: {id}")
                                                if result is None:
                                                    sql = 'INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen, enlace) VALUES (%s, %s, %s, %s, %s, %s, %s)'
                                                    val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, ImagenSRC, enlace)
                                                    try:
                                                        mycursor.execute(sql, val)
                                                        mydb.commit()
                                                        print(f"Se insertó en la base de datos el producto {descripcion} del supermercado {Supermercado}")
                                                    except Exception as e:
                                                        mydb.rollback()
                                                        print(f"Error durante la inserción en la base de datos: {e}")
                                            except Exception as e:
                                                mydb.rollback()
                                                print(f"Error durante la búsqueda en la base de datos: {e}")
                                        else:
                                            id = None
                                            print("No se encontró una subsección para los criterios proporcionados.")

                    if SupermercadoEnlaces == "Mercadona_enlaces.txt":
                        Supermercado = "Mercadona"
                        driver.get(enlace)
                        sleep(1)
                        NombreProducto = None         
                        PrecioProducto = None
                        DetalleProducto = None

                        if CPIntroducidoMercadona == False:
                            driver.find_element("xpath", '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/form/div/input').send_keys('28051/n')
                            driver.find_element("xpath", '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/form/button').click()
                            CPIntroducidoMercadona = True    
                            driver.get(enlace)
                            sleep(2)

                        NombreProducto = None         
                        PrecioProducto = None
                        DetalleProducto = None
                        try:
                            DescripcionXPath = '.title2-r'
                            PrecioXPath = '.large-b'
                            DetalleXPath = 'span.headline1-r:nth-child(2)'
                            imagenSRCXPath = '.image-zoomer__source > img:nth-child(1)'

                            NombreProductoDFE = driver.find_element("css selector", DescripcionXPath)
                            PrecioProductoDFE = driver.find_element("css selector", PrecioXPath)
                            DetalleProductoDFE = driver.find_element("css selector", DetalleXPath)
                            ImagenDFE = driver.find_element("css selector", imagenSRCXPath)
                            

                            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                            PrecioProducto = PrecioProductoDFE.text[:-1]
                            PrecioProducto = PrecioProducto.replace(',', '.')
                            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                            ImagenSRC = ImagenDFE.get_attribute("src")
                        except:
                            try:
                                DescripcionXPath = '.title2-r'
                                PrecioXPath = '.large-b'
                                DetalleXPath = 'span.headline1-r:nth-child(2)'
                                imagenSRCXPath = '.image-zoomer__source > img:nth-child(1)'

                                NombreProductoDFE = driver.find_element("css selector", DescripcionXPath)
                                PrecioProductoDFE = driver.find_element("css selector", PrecioXPath)
                                DetalleProductoDFE = driver.find_element("css selector", DetalleXPath)
                                ImagenDFE = driver.find_element("css selector", imagenSRCXPath)
                                

                                NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                                PrecioProducto = PrecioProductoDFE.text[:-1]
                                PrecioProducto = PrecioProducto.replace(',', '.')
                                DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                                ImagenSRC = ImagenDFE.get_attribute("src")
                            except:
                                try:
                                    DescripcionXPath = '.title2-r'
                                    PrecioXPath = '.large-b'
                                    DetalleXPath = 'span.headline1-r:nth-child(1)'
                                    imagenSRCXPath = '.image-zoomer__source > img:nth-child(1)'

                                    NombreProductoDFE = driver.find_element("css selector", DescripcionXPath)
                                    PrecioProductoDFE = driver.find_element("css selector", PrecioXPath)
                                    DetalleProductoDFE = driver.find_element("css selector", DetalleXPath)
                                    ImagenDFE = driver.find_element("css selector", imagenSRCXPath)
                                    

                                    NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
                                    PrecioProducto = PrecioProductoDFE.text[:-1]
                                    PrecioProducto = PrecioProducto.replace(',', '.')
                                    DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
                                    ImagenSRC = ImagenDFE.get_attribute("src")
                                except Exception as ex:
                                    print("Enlace caido o no se pudo entrar acceder al enlace")
                                    NombreProducto = None         
                                    PrecioProducto = None
                                    DetalleProducto = None
                        finally:
                            if NombreProducto is not None:
                                        sql = 'SELECT seccion, subseccion from backendassist where producto = %s'
                                        val = (descripcion,)
                                        mycursor.execute(sql, val)
                                        result = mycursor.fetchone()
                                        seccionsql = None
                                        subseccionsql = None
                                        if result is not None:
                                            seccionsql, subseccionsql = result
                                            print("Seccion encontrada:", seccionsql)
                                            print("Subseccion encontrada:", subseccionsql)
                                            sql = 'SELECT id from productos where seccion = %s and subseccion = %s and producto = %s and descripcion = %s and supermercado = %s and enlace = %s'
                                            val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, enlace)
                                            try:
                                                mycursor.execute(sql, val)
                                                result = mycursor.fetchone()
                                                id = None
                                                if result is not None:
                                                    id = result
                                                    print(f"Ya hay un producto con esos valores. Id: {id}")
                                                if result is None:
                                                    sql = 'INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen, enlace) VALUES (%s, %s, %s, %s, %s, %s, %s)'
                                                    val = (seccionsql, subseccionsql, descripcion, NombreProducto, Supermercado, ImagenSRC, enlace)
                                                    try:
                                                        mycursor.execute(sql, val)
                                                        mydb.commit()
                                                        print(f"Se insertó en la base de datos el producto {descripcion} del supermercado {Supermercado}")
                                                    except Exception as e:
                                                        mydb.rollback()
                                                        print(f"Error durante la inserción en la base de datos: {e}")
                                            except Exception as e:
                                                mydb.rollback()
                                                print(f"Error durante la búsqueda en la base de datos: {e}")
                                        else:
                                            id = None
                                            print("No se encontró una subsección para los criterios proporcionados.")

    mycursor.close()
    mydb.close()
    driver.close() 
    driver.quit()
    
#CrearProductos("Mercadona_enlaces.txt")
ActualizarPrecios("Mercadona_enlaces.txt")#SupermercadoEnlaces
#Juntar enlaces con lista de productos en un archivo(Lista de productos, Enlaces de los productos, Nombre del fichero con productos y enlaces)
#JuntarEnlaceProducto("ListaProductos.txt", "Enlaces.txt", "Mercadona_enlaces.txt")#ListaProductos, supermercadoArchivosEnlaces, archivoConEnlacesProductos