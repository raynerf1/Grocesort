import requests
from bs4 import BeautifulSoup

# URL de la página web que quieres analizar
url = "https://tienda.mercadona.es/product/10384/leche-desnatada-hacendado-brick"  
headers = { "user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0"}

# Realiza una solicitud GET para obtener el contenido de la página
response = requests.get(url, headers=headers)
#response.status_code
#print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.title.text)
elemento_precio = soup.find('p', class_='product-price__unit-price', attrs={'data-test': 'product-price'})
# Comprueba si el elemento se encontró
if elemento_precio is not None:
    # Obtiene el texto del elemento encontrado
    precio = elemento_precio.text
    # Imprime el precio
    print(precio)
else:
    print("El elemento no se encontro en el HTML.")