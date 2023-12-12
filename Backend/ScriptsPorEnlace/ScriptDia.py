from time import sleep
from selenium import webdriver
import unicodedata
from datetime import date
import mysql.connector

FechaActual=date.today()

mydb = mysql.connector.connect(
  host="hostingmysql335.nominalia.com",
  user="rayner",
  password="marenas19",
  database='bdprecios'
)
mycursor = mydb.cursor()

Supermercado = 'Dia'

productos = ["Leche entera",
    "Leche entera sin lactosa",
    "Leche semidesnatada",
    "Leche semidesnatada sin lactosa",
    "Leche desnatada",
    "Leche desnatada sin lactosa",
    "Yogur sabores",
    "Yogur natural",
    "Yogur griego natural",
    "Yogur griego natural 1kg",
    "Yogur griego natural con azucar",
    "Mantequilla",
    "Margarina",
    "Bebida Almendras",
    "Bebida Arroz",
    "Bebida Soja",
    "Bebida Avena",
    "Horchata",
    "Mousse chocolate",
    "Cuajada",
    "Cuajada con azucar",
    "Flan huevo",
    "Flan vainilla",
    "Gelatina sabores",
    "Gelatina sabores light",
    "Gelatina fresa",
    "Natillas",
    "Natillas chocolate",
    "Batido chocolate 1l",
    "Batido chocolate pack",
    "Batido fresa 1l",
    "Batido fresa pack",
    "Batido vainilla 1l",
    "Batido vainilla pack",
    "Zumo naranja 1l",
    "Zumo naranja pack",
    "Zumo naranja con pulpa",
    "Zumo naranja sin pulpa",
    "Zumo pina y uva 1l",
    "Zumo pina y uva pack",
    "Zumo manzana 1l",
    "Zumo manzana pack",
    "Zumo melocoton y uva 1l",
    "Zumo melocoton y uva pack",
    "Agua",
    "Aceite oliva 1l 0,4",
    "Aceite oliva 5l 0,4",
    "Aceite oliva 1l 1",
    "Aceite oliva 5l 1",
    "Aceite girasol 1l",
    "Aceite girasol 5l",
    "Vinagre vino blanco",
    "Vinagre manzana",
    "Vinagre balsamico modena",
    "Vinagre jerez",
    "Sal mesa",
    "Sal gorda",
    "Sal rosa",
    "Bicarbonato bote",
    "Bicarbonato 1kg",
    "Patatas fritas artesanales",
    "Patatas fritas churreria",
    "Patatas fritas paja",
    "Patatas fritas lisas",
    "Patatas fritas congeladas corte fino",
    "Patatas fritas congeladas corte tradicional",
    "Aceitunas verdes sin hueso",
    "Aceitunas verdes con hueso",
    "Aceitunas negra sin hueso",
    "Aceitunas negra con hueso",
    "Palomitas microondas sal pack",
    "Palomitas microondas mantequilla pack",
    "Palomitas mantequilla pack",
    "Galletas saladas bote",
    "Galletas saladas paquete",
    "Arroz redondo",
    "Arroz largo",
    "Arroz basmati",
    "Arroz vaporizado",
    "Macarron pluma",
    "Macarron tiburon",
    "Fideua",
    "Macarron espiral",
    "Macarron rayado",
    "Macarron pajarita vegetal",
    "Macarron espiral vegetal",
    "Spaghetti",
    "Tallarin",
    "Azucar",
    "Azucar moreno",
    "Cafe molido",
    "Cafe molido descafeinado",
    "Cafe molido tostado",
    "Cafe molido tostado descafeinado",
    "Cafe expreso descafeinado",
    "Cafe soluble",
    "Cafe soluble descafeinado",
    "Galleta maria pack",
    "Galleta maria dorada pack",
    "Galleta maria integral pack",
    "Galleta tostada",
    "Galleta digestive",
    "Galleta digestive avena",
    "Cookies",
    "Galleta oreo",
    "Galleta oreo cubierta de chocolate blanco",
    "Galleta rellena crema chocolate",
    "Cono nata y fresa",
    "Cono vainilla y chocolate",
    "Cono nata y turron",
    "Cono tarta de queso",
    "Cono nata y trufa",
    "Helado bombon avellanas",
    "Helado bombon chocolate blanco",
    "Helado bombon 3 chocolates",
    "Helado bombon chocolate y nata",
    "Helado bombon almendra",
    "Tarrina helado vainilla",
    "Tarrina helado stracciatella",
    "Tarrina helado turron",
    "Tarrina nata y nueces",
    "Tarrina tres chocolates",
    "Tarrina chocolate y trozos",
    "Tarrina frutas del bosque",
    "Tarrina sorbete limon",
    "Cereales cacao rellenos leche",
    "Cereales cacao rellenos chocolate",
    "Copos de avena integral suave",
    "Bolas de cacao",
    "Trigo inflado con miel",
    "Arroz inflado con cacao",
    "Copos de arroz y trigo",
    "Copos de cacao",
    "Copos de arroz y trigo integral con frutos rojos",
    "Copos de maiz",
    "Muesli",
    "Muesli con frutas",
    "Muesli con frutos secos",
    "Muesli con chocolate",
    "Barquillos nata",
    "Barquillos chocolate",
    "Atun claro",
    "Atun claro aceite oliva",
    "Atun claro aceite girasol",
    "Atun claro en escabeche",
    "Bonito del norte en aceite de oliva",
    "Bonito del norte en escabeche",
    "Mejillon escabeche",
    "Mejillon escabeche picante",
    "Mejillones salsa vieira",
    "Mejillones al natural",
    "Sardinas en tomate",
    "Sardinas en aceite de oliva",
    "Sardinas con limon",
    "Sardinas en escabeche",
    "Sardinas picantonas",
    "Tomate triturado 400g",
    "Tomate triturado 800g",
    "Tomate frito bote",
    "Tomate frito pack",
    "Tomate frito en sarten",
    "Tomate frito casero aceite oliva",
    "Judias verdes anchas en conserva",
    "Judias verdes redondas en conserva",
    "Judias verdes anchas congeladas 1kg",
    "Judias verdes redondas congeladas 1kg",
    "Pimientos de piquillo enteros",
    "Pimiento morron",
    "Pimientos de piquillo en tiras",
    "Pimientos de piquillo enteros",
    "Esparragos blancos gruesos",
    "Esparragos verdes delgados",
    "Maiz dulce",
    "Maiz dulce congelado",
    "Guisantes finos",
    "Guisantes finos congelados",
    "Guisantes muy finos",
    "Guisantes muy finos congelados",
    "Guisantes muy finos bote",
    "Guisantes medianos",
    "Champinon entero",
    "Champinon laminado",
    "Alcachofa congelada",
    "Alcachofa baby congelada",
    "Corazon alcachofa bote",
    "Corazon alcachofa bote cristal",
    "Harina de trigo",
    "Harina de trigo integral",
    "Harina pizza",
    "Harina trigo reposteria",
    "Harina trigo fritos y rebozados",
    "Harina trigo bizcochos",
    "Harina maiz",
    "Levadura",
    "Mermelada de fresa",
    "Mermelada de melocoton",
    "Mermelada de naranja",
    "Miel de flores 1kg",
    "Miel de azahar",
    "Barra de pan",
    "Pan de molde blanco familiar",
    "Pan de molde integral",
    "Pan de molde blanco sin corteza",
    "Pan de molde integral sin corteza",
    "Pan hamburguesa",
    "Pan hotdog",
    "Tortilla patata",
    "Tortilla patata cebolla",
    "Pizza barbacoa",
    "Pizza cuatro quesos",
    "Pizza jamon y queso",
    "Pizza pollo y bacon",
    "Garbanzo cocido",
    "Garbanzo",
    "Alubia blanca cocida",
    "Alubia blanca",
    "Alubia pinta cocida",
    "Alubia pinta",
    "Lenteja cocida",
    "Lenteja",
    "Ketchup",
    "Mostaza",
    "Mayonesa",
    "Gazpacho",
    "Salmorejo",
    "Docena huevo l",
    "Docena huevo m",
    "Docena huevo xl",
    "Claras huevo"]

enlaces = ["https://www.dia.es/leche-huevos-y-mantequilla/leche/p/608?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/leche-huevos-y-mantequilla/leche/p/225278?analytics_list_id=S0001&analytics_list_name=search&index=13",
    "https://www.dia.es/leche-huevos-y-mantequilla/leche/p/504?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/leche-huevos-y-mantequilla/leche/p/130063?analytics_list_id=S0001&analytics_list_name=search&index=10",
    "https://www.dia.es/leche-huevos-y-mantequilla/leche/p/607?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/leche-huevos-y-mantequilla/leche/p/185450?analytics_list_id=S0001&analytics_list_name=search&index=7",
    
    "https://www.dia.es/yogures-y-postres/yogures-de-sabores-y-frutas/p/100604?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/yogures-y-postres/yogures-naturales/p/272536?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/yogures-y-postres/griegos-y-mousse/p/135285?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/yogures-y-postres/griegos-y-mousse/p/296515?analytics_list_id=S0001&analytics_list_name=search&index=16",
    "https://www.dia.es/yogures-y-postres/griegos-y-mousse/p/135286?analytics_list_id=S0001&analytics_list_name=search&index=31",

    "https://www.dia.es/leche-huevos-y-mantequilla/mantequilla-y-margarina/p/268201?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/leche-huevos-y-mantequilla/mantequilla-y-margarina/p/55574?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/leche-huevos-y-mantequilla/bebidas-vegetales/p/267684?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/leche-huevos-y-mantequilla/bebidas-vegetales/p/267683?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/leche-huevos-y-mantequilla/bebidas-vegetales/p/3027?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/leche-huevos-y-mantequilla/bebidas-vegetales/p/207399?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/leche-huevos-y-mantequilla/batidos-y-horchatas/p/26053?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/yogures-y-postres/gelatinas-y-otros-postres/p/46923?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/yogures-y-postres/cuajada/p/27195?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/yogures-y-postres/natillas-y-flan/p/3387?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/yogures-y-postres/natillas-y-flan/p/105814?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/yogures-y-postres/gelatinas-y-otros-postres/p/139596?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "Vacio",
    "https://www.dia.es/yogures-y-postres/gelatinas-y-otros-postres/p/108518?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/yogures-y-postres/natillas-y-flan/p/113550?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/yogures-y-postres/natillas-y-flan/p/219104?analytics_list_id=S0001&analytics_list_name=search&index=10",
    "https://www.dia.es/leche-huevos-y-mantequilla/batidos-y-horchatas/p/1269?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/leche-huevos-y-mantequilla/batidos-y-horchatas/p/115833?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/leche-huevos-y-mantequilla/batidos-y-horchatas/p/134753?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "Vacio",
    "https://www.dia.es/leche-huevos-y-mantequilla/batidos-y-horchatas/p/134754?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/agua-refrescos-y-zumos/zumos/p/288688?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/agua-refrescos-y-zumos/zumos/p/277771?analytics_list_id=S0001&analytics_list_name=search&index=5",
    "https://www.dia.es/agua-refrescos-y-zumos/zumos/p/50690?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/agua-refrescos-y-zumos/zumos/p/131262?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/agua-refrescos-y-zumos/zumos/p/146291?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/agua-refrescos-y-zumos/zumos/p/277772?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/agua-refrescos-y-zumos/zumos/p/281?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/agua-refrescos-y-zumos/zumos/p/43228?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/agua-refrescos-y-zumos/zumos/p/146282?analytics_list_id=S0001&analytics_list_name=search&index=6",
    "https://www.dia.es/agua-refrescos-y-zumos/zumos/p/146289?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "Vacio",
    "https://www.dia.es/aceites-salsas-y-especias/aceites/p/104?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/aceites-salsas-y-especias/aceites/p/49895?analytics_list_id=S0001&analytics_list_name=search&index=6",
    "https://www.dia.es/aceites-salsas-y-especias/aceites/p/216284?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/aceites-salsas-y-especias/aceites/p/107364?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/aceites-salsas-y-especias/aceites/p/101?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/aceites-salsas-y-especias/aceites/p/49894?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/aceites-salsas-y-especias/vinagres-y-alinos/p/422?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/aceites-salsas-y-especias/vinagres-y-alinos/p/84060?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/aceites-salsas-y-especias/vinagres-y-alinos/p/106144?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/aceites-salsas-y-especias/vinagres-y-alinos/p/273811?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/aceites-salsas-y-especias/sal-y-especias/p/419?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/aceites-salsas-y-especias/sal-y-especias/p/51835?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/aceites-salsas-y-especias/sal-y-especias/p/282359?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/aceites-salsas-y-especias/sal-y-especias/p/158996?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/aceites-salsas-y-especias/sal-y-especias/p/287246?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/patatas-fritas-y-snacks/p/277827?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/patatas-fritas-y-snacks/p/277831?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/patatas-fritas-y-snacks/p/33412?analytics_list_id=S0001&analytics_list_name=search&index=6",
    "https://www.dia.es/congelados/patatas-fritas/p/262863?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/congelados/patatas-fritas/p/262861?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/aceitunas-y-encurtidos/p/142072?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/aceitunas-y-encurtidos/p/46239?analytics_list_id=S0001&analytics_list_name=search&index=8",
    "https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/aceitunas-y-encurtidos/p/142058?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/aceitunas-y-encurtidos/p/273263?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/frutos-secos/p/2030?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/frutos-secos/p/129665?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/patatas-fritas-y-snacks/p/83685?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas-saladas/p/12951?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas-saladas/p/30330?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/arroz-pastas-y-legumbres/arroz/p/151?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/arroz-pastas-y-legumbres/arroz/p/5873?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/arroz-pastas-y-legumbres/arroz/p/53397?analytics_list_id=S0001&analytics_list_name=search&index=10",
    "https://www.dia.es/arroz-pastas-y-legumbres/arroz/p/28809?analytics_list_id=S0001&analytics_list_name=search&index=7",
    "https://www.dia.es/arroz-pastas-y-legumbres/pastas/p/518?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/arroz-pastas-y-legumbres/pastas/p/1127?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/arroz-pastas-y-legumbres/pastas/p/6265?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/arroz-pastas-y-legumbres/pastas/p/290664?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "Vacio",
    "https://www.dia.es/arroz-pastas-y-legumbres/pastas/p/33117?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/arroz-pastas-y-legumbres/pastas/p/52208?analytics_list_id=L2044&analytics_list_name=arroz_pastas_y_legumbres_pastas&index=3",
    "https://www.dia.es/arroz-pastas-y-legumbres/pastas/p/74729?analytics_list_id=L2044&analytics_list_name=arroz_pastas_y_legumbres_pastas&index=13",
    "https://www.dia.es/azucar-chocolates-y-caramelos/azucar-y-edulcorantes/p/81798?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/cafe-cacao-e-infusiones/cafe/p/120826?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/cafe-cacao-e-infusiones/cafe/p/218159?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "Vacio",
    "Vacio",
    "https://www.dia.es/cafe-cacao-e-infusiones/cafe/p/34615?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/cafe-cacao-e-infusiones/cafe/p/230?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/469?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/149293?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/269627?analytics_list_id=S0001&analytics_list_name=search&index=9",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/480?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/83648?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/141787?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/110671?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/220174?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/32812?analytics_list_id=S0001&analytics_list_name=search&index=16",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.dia.es/congelados/helados-y-hielo/p/19479?analytics_list_id=S0001&analytics_list_name=search&index=6",
    "https://www.dia.es/congelados/helados-y-hielo/p/19507?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/111278?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/106852?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/168881?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/76223?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/37190?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/37199?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/74305?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/10284?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/66956?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/222746?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/37203?analytics_list_id=S0001&analytics_list_name=search&index=5",
    "Vacio",
    "https://www.dia.es/galletas-bollos-y-cereales/cereales/p/135900?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/220173?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/galletas-bollos-y-cereales/galletas/p/220172?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/conservas-caldos-y-cremas/atun-bonito-y-caballa/p/262439?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/conservas-caldos-y-cremas/atun-bonito-y-caballa/p/262432?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/conservas-caldos-y-cremas/atun-bonito-y-caballa/p/262437?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/conservas-caldos-y-cremas/atun-bonito-y-caballa/p/262440?analytics_list_id=S0001&analytics_list_name=search&index=13",
    "Vacio",
    "Vacio",
    "https://www.dia.es/conservas-caldos-y-cremas/mejillones/p/50596?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/conservas-caldos-y-cremas/mejillones/p/117162?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/conservas-caldos-y-cremas/mejillones/p/176765?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/conservas-caldos-y-cremas/mejillones/p/145495?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/conservas-caldos-y-cremas/sardinas-y-sardinillas/p/6084?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/conservas-caldos-y-cremas/sardinas-y-sardinillas/p/7975?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.dia.es/aceites-salsas-y-especias/tomate/p/326?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/aceites-salsas-y-especias/tomate/p/13105?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/aceites-salsas-y-especias/tomate/p/10677?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/aceites-salsas-y-especias/tomate/p/128657?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/aceites-salsas-y-especias/tomate/p/289048?analytics_list_id=S0001&analytics_list_name=search&index=11",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/13049?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/171371?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/congelados/verduras-hortalizas-y-salteados/p/263267?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/congelados/verduras-hortalizas-y-salteados/p/264698?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/215665?analytics_list_id=S0001&analytics_list_name=search&index=6",
    "Vacio",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/46598?analytics_list_id=S0001&analytics_list_name=search&index=5",
    "Vacio",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/4118?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/124858?analytics_list_id=S0001&analytics_list_name=search&index=7",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/47592?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/1302?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/1666?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.dia.es/panes-harinas-y-masas/harinas-y-levaduras/p/505?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/panes-harinas-y-masas/harinas-y-levaduras/p/190027?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/panes-harinas-y-masas/harinas-y-levaduras/p/163262?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/panes-harinas-y-masas/harinas-y-levaduras/p/216391?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/panes-harinas-y-masas/harinas-y-levaduras/p/161360?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/panes-harinas-y-masas/harinas-y-levaduras/p/247514?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/azucar-chocolates-y-caramelos/mermeladas-y-frutas-en-almibar/p/135272?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/azucar-chocolates-y-caramelos/mermeladas-y-frutas-en-almibar/p/135271?analytics_list_id=S0001&analytics_list_name=search&index=7",
    "Vacio",
    "https://www.dia.es/azucar-chocolates-y-caramelos/miel/p/297?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/azucar-chocolates-y-caramelos/miel/p/222955?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/panes-harinas-y-masas/pan-recien-horneado/p/38109?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/panes-harinas-y-masas/pan-de-molde/p/77955?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/panes-harinas-y-masas/pan-de-molde/p/266136?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/panes-harinas-y-masas/pan-de-molde/p/48666?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/panes-harinas-y-masas/pan-de-molde/p/74397?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/panes-harinas-y-masas/pan-de-molde/p/182644?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/panes-harinas-y-masas/pan-de-molde/p/40381?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/pizzas-y-platos-preparados/tortillas-empanadas-croquetas/p/262523?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/pizzas-y-platos-preparados/tortillas-empanadas-croquetas/p/262522?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/pizzas-y-platos-preparados/pizzas/p/263619?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/pizzas-y-platos-preparados/pizzas/p/56444?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/pizzas-y-platos-preparados/pizzas/p/30479?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "Vacio",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/1232?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/arroz-pastas-y-legumbres/garbanzos/p/155?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/1233?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/arroz-pastas-y-legumbres/alubias/p/154?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/254987?analytics_list_id=S0001&analytics_list_name=search&index=4",
    "https://www.dia.es/arroz-pastas-y-legumbres/alubias/p/156?analytics_list_id=S0001&analytics_list_name=search&index=5",
    "https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/p/58809?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/arroz-pastas-y-legumbres/lentejas/p/157?analytics_list_id=S0001&analytics_list_name=search&index=3",

    "https://www.dia.es/aceites-salsas-y-especias/tomate/p/4853?analytics_list_id=S0001&analytics_list_name=search&index=2",
    "https://www.dia.es/aceites-salsas-y-especias/mayonesa-y-otras-salsas/p/56586?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/aceites-salsas-y-especias/mayonesa-y-otras-salsas/p/53720?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/pizzas-y-platos-preparados/gazpachos-salmorejos-y-ensaladas/p/43231?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/pizzas-y-platos-preparados/gazpachos-salmorejos-y-ensaladas/p/231863?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/leche-huevos-y-mantequilla/huevos/p/167072?analytics_list_id=S0001&analytics_list_name=search&index=1",
    "https://www.dia.es/leche-huevos-y-mantequilla/huevos/p/14636?analytics_list_id=S0001&analytics_list_name=search&index=3",
    "Vacio",
    "Vacio"]
seccion = ''
seccionDetalle = ''
id_producto = ''
driver = webdriver.Firefox()
for i in range(229):
    if enlaces[i] == 'Vacio':
        print(i)
        print('No hay enlace')
    else:
        url = enlaces[i]
        driver.get(url)
        sleep(1)
        if i < 12:
            seccion = 'Lacteos'
            if i < 6:
                seccionDetalle = 'Leche'
            if i > 5 and i< 11:
                seccionDetalle = 'Yogures'
            if i >10 and i < 13:
                seccionDetalle = 'Mantequilla'
        
        if i > 12 and i < 18:
            seccion = 'Bebidas vegetales'
            seccionDetalle = productos[i]
        
        if i > 17 and i < 27:
            seccion = 'Postres'

            if i > 17 and i< 19:
                seccionDetalle = productos[i]
            if i > 18 and i< 21:
                seccionDetalle = 'Cuajada'
            if i > 20 and i< 23:
                seccionDetalle = 'Flanes'
            if i > 22 and i< 26:
                seccionDetalle = 'Gelatinas'
            if i > 25 and i< 27:
                seccionDetalle = 'Natillas'     

        if i > 27 and i < 33:
            seccion = 'Batidos'

            if i > 27 and i< 30:
                seccionDetalle = 'Batido de chocolate'
            if i > 29 and i< 32:
                seccionDetalle = 'Batido de fresa'
            if i > 31 and i< 34:
                seccionDetalle = 'Batido de vainilla'

        if i > 33 and i < 43:
            seccion = 'Zumos'
            if i > 33 and i< 38:
                seccionDetalle = 'Zumo de naranja'
            if i > 37 and i< 40:
                seccionDetalle = 'Zumo de pina' 
            if i > 39 and i< 42:
                seccionDetalle = 'Zumo de manzana' 
            if i > 41 and i< 44:
                seccionDetalle = 'Zumo de melocoton' 
        if i == 44:
            seccion = 'Agua'
            seccionDetalle = 'Agua'
        if i > 44 and i < 50:
            seccion = 'Aceite'
            if i > 44 and i< 49:
                seccionDetalle = 'Aceite oliva' 
            if i > 48 and i< 51:
                seccionDetalle = 'Aceite girasol'
        if i > 50 and i < 55:
            seccion = 'Vinagre'
            seccionDetalle = productos[i]
        if i > 54 and i < 58:
            seccion = 'Sal'
            seccionDetalle = productos[i]
        if i > 57 and i < 59:
            seccion = 'Bicarbonato'
            seccionDetalle = 'Bicarbonato'
        if i > 59 and i < 75:
            seccion = 'Snacks'
            if i > 59 and i< 66:
                seccionDetalle = 'Patatas fritas' 
            if i > 65 and i< 66:
                seccionDetalle = 'Patatas fritas congeladas'
            if i > 65 and i< 70:
                seccionDetalle = 'Aceitunas'
            if i > 69 and i< 73:
                seccionDetalle = 'Palomitas'
            if i > 72 and i< 75:
                seccionDetalle = 'Galletas saladas'
        if i > 74 and i < 79:
            seccion = 'Arroz'
            seccionDetalle = 'Arroz'
        if i > 78 and i < 88:
            seccion = 'Pasta'
            seccionDetalle = productos[i]
        if i > 87 and i < 90:
            seccion = 'Azucar'
            if i == 88:
                seccionDetalle = 'Azucar blanco'
            if i == 89:
                seccionDetalle = 'Azucar moreno'
        if i > 89 and i < 97:
            seccion = 'Cafe'
            seccionDetalle = productos[i]
        if i > 96 and i < 107:
            seccion = 'Galletas'
            if i > 103 and i < 106:
                seccionDetalle = 'Galleta estilo oreo'
            else:
                seccionDetalle = productos[i]
        if i > 106 and i < 125:
            seccion = 'Helados'
            if i > 106 and i < 112:
                seccionDetalle = 'Conos'
            if i > 111 and i < 117:
                seccionDetalle = 'Bombon'
            if i > 116 and i < 125:
                seccionDetalle = 'Tarrinas'
        if i > 124 and i < 139:
            seccion = 'Cereales'
            if i == 125:
                seccionDetalle = 'Cereales rellenos leche'
            if i == 126:
                seccionDetalle = 'Cereales rellenos cacao'
            if i == 127:
                seccionDetalle = 'Copos de avena'
            if i == 129:
                seccionDetalle = 'Trigo inflado'
            if i == 131 or i == 133:
                seccionDetalle = 'Copos de arroz y trigo'
            if i > 134 and i < 139:
                seccionDetalle = 'Muesli'
            else:
                seccionDetalle = productos[i]
        if i > 138 and i < 141:
            seccion = 'Barquillos'
            seccionDetalle = productos[i]
        if i > 140 and i < 155:
            seccion = 'Pescados y marisco en conserva'
            
            if i > 140 and i < 145:
                seccionDetalle = 'Atun'
            
            if i > 144 and i < 147:
                seccionDetalle = 'Bonito'
            
            if i > 146 and i < 151:
                seccionDetalle = 'Mejillones'
            if i > 150 and i < 155:
                seccionDetalle = 'Sardinas'

        if i > 155 and i < 186:
            seccion = 'Verduras en conserva'
            if i > 155 and i < 162:
                seccionDetalle = 'Tomate'
            if i > 161 and i < 166:
                seccionDetalle = 'Judias verdes'
            if i > 165 and i < 170:
                seccionDetalle = 'Pimientos'
            if i > 169 and i < 172:
                seccionDetalle = 'Esparragos'
            if i > 171 and i < 174:
                seccionDetalle = 'Maiz'
            if i > 173 and i < 180:
                seccionDetalle = 'Guisantes'
            if i > 179 and i < 182:
                seccionDetalle = 'Champinones'
            if i > 181 and i < 186:
                seccionDetalle = 'Alcachofas'
        if i > 185 and i < 193:
            seccion = 'Harinas'
            seccionDetalle = productos[i]
        if i == 193:
            seccion = 'Levadura'
            seccionDetalle = 'Levadura'
        if i > 193 and i < 197:
            seccion = 'Mermelada'
            seccionDetalle = productos[i]
        if i > 196 and i < 199:
            seccion = 'Miel'
            seccionDetalle = 'Miel'
        if i > 198 and i < 206:
            seccion = 'Panes'
            if i == 199:
                seccionDetalle = 'Barra pan'
            if i > 199 and i < 204:
                seccionDetalle = 'Pan molde'
            if i == 204:
                seccionDetalle = 'Pan hamburguesa'
            if i == 205:
                seccionDetalle = 'Pan hotdog'
        if i > 205 and i < 212:
            seccion = 'Platos preparados'
            if i > 207 and i < 212:
                seccionDetalle = 'Pizzas'
            else:
                seccionDetalle = productos[i]
        if i > 211 and i < 220:
            seccion = 'Legumbres'
            if i > 211 and i < 214:
                seccionDetalle = 'Garbanzos'
            if i > 213 and i < 218:
                seccionDetalle = 'Alubias'
            if i > 217 and i < 220:
                seccionDetalle = 'Lentejas'
        if i > 219 and i < 223:
            seccion = 'Salsas'
            seccionDetalle = productos[i]
        if i == 223:
            seccion = 'Gazpacho y salmorejo'
            seccionDetalle = 'Gazpacho'
        if i == 224:
            seccion = 'Gazpacho y salmorejo'
            seccionDetalle = 'Salmorejo'
        if i > 224:
            seccion = 'Huevos'
            seccionDetalle = 'Docena Huevo'
            if i == 228:
                seccionDetalle = 'Claras Huevo'
            
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

            try:
                    sql = "SELECT id from productos where producto = %s and descripcion = %s and supermercado = %s "
                    valSelect = (productos[i], NombreProducto, Supermercado)
                    mycursor.execute(sql, valSelect)
                    result = mycursor.fetchone()
                    if result:
                            id_producto = result[0]
                            #print('La id en DB es ', id_producto)
                            sql = "INSERT INTO precios (id, producto, supermercado, precio, detalle, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
                            val = (id_producto, productos[i], Supermercado, PrecioProducto, DetalleProducto, FechaActual)
                            
                            try:
                                mycursor.execute(sql, val)
                                mydb.commit()
                                print("La inserción en la base de datos se realizó con éxito.")
                            except Exception as e:
                                mydb.rollback()
                                print(f"Error durante la inserción en la base de datos: {e}")

                    else:
                            id_producto = '' 
                            print('No hay un producto con esa id en la base de datos')
            except:
                    print("No se pudieron realizar transacciones con la base de datos")

        except Exception as ex:
            driver.quit()
        finally:
            print(i)
            '''print(productos[i])'''
            print(seccion+' - '+seccionDetalle+':')
            print(NombreProducto + ' ' +PrecioProducto+' '+DetalleProducto)
            '''
            sql = "INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (seccion, seccionDetalle, productos[i], NombreProducto, Supermercado, ImagenSRC)
            mycursor.execute(sql, val)
            mydb.commit()
            '''
mycursor.close()
mydb.close()         
driver.quit()
        