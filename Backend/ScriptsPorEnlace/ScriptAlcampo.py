from time import sleep
from selenium import webdriver
import unicodedata
from datetime import date
import mysql.connector
from datetime import date, timedelta


FechaActual=date.today()
fecha2DiasAntes = FechaActual - timedelta(days=2)

mydb = mysql.connector.connect(
  host="hostingmysql335.nominalia.com",
  user="rayner",
  password="marenas19",
  database='bdprecios'
)



mycursor = mydb.cursor()

Supermercado = 'Alcampo'

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
    "Galleta rellena crema chocolate",
    "Galleta oreo cubierta de chocolate blanco",
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

enlaces = ["https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Leche-entera-de-vaca-PRODUCTO-ALCAMPO-1-l/53540",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Leche-entera-de-vaca-sin-lactosa-PRODUCTO-ALCAMPO-1-l/237633",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Leche-semidesnatada-de-vaca-PRODUCTO-ALCAMPO-1-l/191059",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Leche-semidesnatada-de-vaca-sin-lactosa-PRODUCTO-ALCAMPO-1-l/89677",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Leche-desnatada-de-vaca-PRODUCTO-ALCAMPO-1-l/53542",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Leche-desnatada-de-vaca-sin-lactosa-PRODUCTO-ALCAMPO-1-l/91869",

    "Vacio",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Yogur-griego-sabor-natural-PRODUCTO-ALCAMPO-4-x-125-g/95390",
    "https://www.compraonline.alcampo.es/products/WEIDEGLUCK-Yogur-natural-elaborado-con-leche-de-granja-WEIDEGLUCK-1-kg/95558",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Yogur-estilo-griego-natural-azucarado-PRODUCTO-ALCAMPO-4-x-125-g/51321",

    "https://www.compraonline.alcampo.es/products/KAIKU-Pastilla-de-mantequilla-KAIKU-250-g/52387",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tarrina-de-margarina-vegetal-3-4-con-sal-PRODUCTO-ALCAMPO-500-g/50026",

    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Bebida-de-almendras-con-alto-contenido-de-vitaminas-A-D-y-B12-y-calcio-PRODUCTO-ALCAMPO-1-l/883201",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Bebida-de-arroz-con-alto-contenido-de-calcio-y-vitamina-D-PRODUCTO-ALCAMPO-1-l/883190",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Bebida-de-soja-sin-gluten-y-enriquecida-con-calcio-y-vitaminas-A-y-D-PRODUCTO-ALCAMPO-1-l/52858",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Bebida-de-avena-con-alto-contenido-de-calcio-y-vitamina-D-PRODUCTO-ALCAMPO-1-l/883192",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Horchata-de-chufa-con-denominaci%C3%B3n-de-origen-Chufa-de-Valencia-PRODUCTO-ALCAMPO-botella-de-1-l/52070",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Cuajada-natural-PRODUCTO-ALCAMPO-4-x-125-g/51022",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Flan-de-huevo-elaborado-al-ba%C3%B1o-maria-con-huevos-frescos-PRODUCTO-ALCAMPO-4-x-100-g/52919",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Flan-con-sabor-a-vainilla-PRODUCTO-ECON%C3%93MICO-ALCAMPO-6-x-100-g/90995",
    "https://www.compraonline.alcampo.es/products/CLESA-Gelatina-de-varios-sabores-2-lim%C3%B3n-2-naranja-y-2-fresa-0-az%C3%BAcares-CLESA-6-x-90-g/716741",
    "https://www.compraonline.alcampo.es/products/REINA-Gelatina-sin-az%C3%BAcares-y-0-materia-grasa-de-tutti-fruti-fresa-naranja-y-lim%C3%B3n-REINA-Ekilibrio-4-x-100-g/980951",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Gelatina-con-sabor-a-fresa-4-x-100-g/54561",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Natillas-con-sabor-a-vainilla-PRODUCTO-ALCAMPO-4-x-125-g/52081",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Natillas-sabor-a-chocolate-PRODUCTO-ALCAMPO-4-x-125-g/52114",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Batido-con-sabor-a-chocolate-PRODUCTO-ALCAMPO-1-l/52283",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Batido-con-sabor-chocolate-PRODUCTO-ALCAMPO-6-x-200-ml/90013",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Batido-con-sabor-a-fresa-PRODUCTO-ALCAMPO-botella-1-l/52289",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Batido-con-sabor-a-fresa-PRODUCTO-ALCAMPO-6-x-200-ml/90014",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Batido-con-sabor-a-vainilla-PRODUCTO-ALCAMPO-1-l/52288",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Batido-con-sabor-a-vainilla-PRODUCTO-ALCAMPO-6-x-200-ml/90015",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Zumo-naranja-100-exprimido-sin-pulpa-PRODUCTO-ALCAMPO-1-l/35941",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Zumo-de-naranja-PRODUCTO-ECON%C3%93MICO-ALCAMPO-brick-de-6-uds-x-20-cl/888987",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Zumo-de-naranja-con-pulpa-refrigerado-PRODUCTO-ALCAMPO-brick-de-1-l/71695",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Zumo-de-naranja-sin-pulpa-refrigerado-PRODUCTO-ALCAMPO-1-l/58854",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Zumo-de-pi%C3%B1a-manzana-y-uva-PRODUCTO-ECON%C3%93MICO-ALCAMPO-brick-de-1-l/34332",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Zumo-de-pi%C3%B1a-manzana-y-uva-PRODUCTO-ECON%C3%93MICO-ALCAMPO-pack-de-6-uds-x-20-cl/888989",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Zumo-de-manzana-PRODUCTO-ECON%C3%93MICO-ALCAMPO-1-l/34351",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Zumo-de-melocot%C3%B3n-manzana-y-uva-PRODUCTO-ECON%C3%93MICO-ALCAMPO-brick-de-1-l/34341",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Zumo-de-melocot%C3%B3n-uva-y-manzana-PRODUCTO-ECON%C3%93MICO-ALCAMPO-brick-6-uds-x-20-cl/888988",
    "https://www.compraonline.alcampo.es/products/AQUAREL-Agua-mineral-sin-gas-AQUAREL-botella-1-50-l/36223",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Aceite-de-oliva-suave-1-l/19824",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Aceite-de-oliva-suave-PRODUCTO-ALCAMPO-garrafa-de-5-l/19827",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Aceite-de-oliva-virgen-extra-1-l/29834",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Aceite-de-oliva-virgen-extra-garrafa-de-5-l/29848",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Aceite-de-girasol-PRODUCTO-ALCAMPO-botella-de-1-l/19818",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Aceite-de-girasol-PRODUCTO-ALCAMPO-garrafa-de-5-l/19821",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Vinagre-de-vino-blanco-PRODUCTO-ECON%C3%93MICO-ALCAMPO-botella-de-1-l/23355",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Vinagre-de-manzana-PRODUCTO-ALCAMPO-1l/206839",
    "https://www.compraonline.alcampo.es/products/ALCAMPO-GOURMET-Vinagre-bals%C3%A1mico-de-M%C3%B3dena-ALCAMPO-GOURMET-botella-de-500-ml/86301",
    "https://www.compraonline.alcampo.es/products/YBARRA-Vinagre-de-vino-de-Jerez-reserva-con-denominaci%C3%B3n-de-origen-Jerez-YBARRA-botella-de-500-ml/27112",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Sal-fina-de-mesa-PRODUCTO-ALCAMPO-1-Kg/50624",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Sal-gruesa-marina-PRODUCTO-ALCAMPO-1-kg/22011",
    "https://www.compraonline.alcampo.es/products/SAL-ROCA-Sal-rosa-fina-del-Himalaya-especial-para-cocinar-y-sazonar-SAL-ROCA-500-g/886983",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Bicarbonato-s%C3%B3dico-PRODUCTO-ALCAMPO-200-g/96981",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/ANIZVI-Patatas-fritas-artesanas-en-aceite-girasol-ANIZVI-300-g/17682",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Patatas-fritas-en-sart%C3%A9n-receta-churrer%C3%ADa-PRODUCTO-ALCAMPO-150-g/505360",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Patatas-fritas-tipo-paja-PRODUCTO-ALCAMPO-100-g/234468",
    "https://www.compraonline.alcampo.es/products/ALCAMPO-GOURMET-Patatas-fritas-lisas-en-aceite-de-girasol-extra-crujientes-ALCAMPO-GOURMET-180-g/17338",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Patatas-prefritas-y-ultracongeladas-con-corte-extrafino-PRODUCTO-ALCAMPO-1-kg/61358",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Patatas-prefritas-y-ultracongeladas-PRODUCTO-ECON%C3%93MICO-ALCAMPO-1-kg/67598",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Aceitunas-verdes-sin-hueso-PRODUCTO-ALCAMPO-450-g/27142",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Aceitunas-verdes-con-hueso-PRODUCTO-ALCAMPO-bote-de-550-g/27137",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Aceitunas-negras-sin-hueso-PRODUCTO-ALCAMPO-150-g/27116",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Aceitunas-negras-con-hueso-PRODUCTO-ALCAMPO-200-g/27118",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Palomitas-de-ma%C3%ADz-para-microondas-con-sal-PRODUCTO-ALCAMPO-6-uds-X-90-g/952282",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Palomitas-de-ma%C3%ADz-para-microondas-sabor-mantequilla-PRODUCTO-ALCAMPO-3-uds-x-90-g/952295",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Palomitas-de-ma%C3%ADz-sabor-mantequilla-PRODUCTO-ALCAMPO-80-g/423221",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-saladas-redondas-PRODUCTO-ALCAMPO-350-g/18968",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-saladas-crackers-PRODUCTO-ALCAMPO-paquete-de-100-g/24371",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Arroz-redondo-extra-PRODUCTO-ALCAMPO-paquete-de-1-kg/18165",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Arroz-largo-PRODUCTO-ALCAMPO-paquete-de-1-kg/21308",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Arroz-basmati-PRODUCTO-ALCAMPO-paquete-de-1-kg/27767",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Arroz-largo-vaporizado-PRODUCTO-ALCAMPO-paquete-de-1-kg/88579",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pasta-macarr%C3%B3n-paquete-de-500-g/16539",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pasta-tibur%C3%B3n-PRODUCTO-ALCAMPO-paquete-de-500-g/886787",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pasta-Fideu%C3%A1-PRODUCTO-ALCAMPO-paquete-de-500-g/62515",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pasta-espirales-PRODUCTO-ALCAMPO-paquete-de-500-g/20562",
    "https://www.compraonline.alcampo.es/products/GALLO-Pasta-macarr%C3%B3n-rayado-GALLO-paquete-de-450-g/12657",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pasta-espiral-con-espinacas-y-tomate-PRODUCTO-ALCAMPO-paquete-500-g/23570",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pasta-espagueti-PRODUCTO-ALCAMPO-paquete-de-500-g/16542",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pasta-tallar%C3%ADn-PRODUCTO-ALCAMPO-paquete-de-500-g/20565",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Az%C3%BAcar-blanco-PRODUCTO-ALCAMPO-1-Kg/197879",
    "https://www.compraonline.alcampo.es/products/ACOR-Az%C3%BAcar-moreno-de-ca%C3%B1a-integral-ACOR-1-kilogramo/625523",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Caf%C3%A9-molido-mezcla-PRODUCTO-ECON%C3%93MICO-ALCAMPO-250-g/567673",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Caf%C3%A9-molido-mezcla-descafeinado-50-tueste-natural-descafeinado-50-torrefacto-descafeinado-PRODUCTO-ALCAMPO-250-g/10142",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Caf%C3%A9-molido-mezcla-de-tueste-natural-50-y-torrefacto-50-PRODUCTO-ALCAMPO-250-g/20433",
    "Vacio",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Caf%C3%A9-soluble-natural-PRODUCTO-ALCAMPO-200-g/543541",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Caf%C3%A9-soluble-descafe%C3%ADnado-PRODUCTO-ALCAMPO-200-g/542987",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-Mar%C3%ADa-PRODUCTO-ALCAMPO-800-g/19883",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-Mar%C3%ADa-dorada-PRODUCTO-ALCAMPO-800-g/19906",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-Mar%C3%ADa-integral-PRODUCTO-ALCAMPO-800-g/19707",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-tostadas-PRODUCTO-ALCAMPO-800-g/19918",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-Digestive-PRODUCTO-ALCAMPO-800-g/19724",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-Digestive-con-avena-PRODUCTO-ALCAMPO-425-g/10128",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-con-pepitas-de-chocolate-PRODUCTO-ALCAMPO-200-g/14914",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-rellenas-de-crema-con-sabor-a-vainilla-PRODUCTO-ALCAMPO-176-g/19729",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-sandwich-con-relleno-de-crema-y-ba%C3%B1ada-con-chocolate-blanco-PRODUCTO-ALCAMPO-252-g/10141",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Galletas-rellenas-de-chocolate-PRODUCTO-ECON%C3%93MICO-ALCAMPO-500-g/28866",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Conos-de-helado-de-nata-y-fresa-con-salsa-de-fresa-PRODUCTO-ALCAMPO-6-x-120-ml/67639",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Cono-de-helado-de-vainilla-PRODUCTO-ALCAMPO-6-x-120-ml/67645",
    "Vacio",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Cono-de-helado-de-nata-y-trufa-PRODUCTO-ALCAMPO-6-x-120-ml/20928",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Mini-bombones-de-helado-de-avellana-son-salsa-de-avellana-y-cobertura-de-chocolate-con-leche-PRODUCTO-ALCAMPO-Les-gourmands-4-x-70-ml/951205",
    "Vacio",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Bomb%C3%B3n-de-nata-recubierto-de-chocolate-negro-PRODUCTO-ALCAMPO-4-x-120-ml/68637",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Bomb%C3%B3n-almendrado-de-vainilla-recubierto-de-chocolate-con-leche-PRODUCTO-ALCAMPO-4-x-120-ml/68641",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tarrina-de-helado-con-sabor-a-vainilla-PRODUCTO-ALCAMPO-1-l/67717",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tarrina-de-helado-de-turr%C3%B3n-PRODUCTO-ALCAMPO-850-ml/68597",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tarrina-de-helado-de-chocolate-con-salsa-sabor-chocolate-y-trocitos-de-chocolate-con-leche-y-blanco-PRODUCTO-ALCAMPO-900-ml/67344",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tarrina-de-helado-de-chocolate-con-virutas-de-chocolate-PRODUCTO-ALCAMPO-1-l/67493",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tarrina-de-helado-de-yogur-con-frutos-rojos-PRODUCTO-ALCAMPO-850-ml/67833",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tarrina-de-helado-de-sorbete-de-lim%C3%B3n-PRODUCTO-ALCAMPO-1-l/68050",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Cereales-rellenos-de-leche-PRODUCTO-ALCAMPO-500-g/625502",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Cereales-rellenos-de-cacao-con-avellana-PRODUCTO-ALCAMPO-JUMBLIES-500-g/625252",
    "https://www.compraonline.alcampo.es/products/Copos-suaves-de-avena-integrales-ecol%C3%B3gicos-ALCAMPO-ECOL%C3%93GICO-500-g/793505",
    "https://www.compraonline.alcampo.es/products/NACIONAL-Cereales-Chooks-bolas-de-chocolate-300-g/745440",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Cereal-de-trigo-inflado-con-miel-PRODUCTO-ALCAMPO-BUMPIES-500-g/427516",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Cereales-de-arroz-con-cacao-sin-gluten-PROUCTO-ALCAMPO-400-g/404123",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Cereales-desayuno-de-arroz-y-ma%C3%ADz-p%C3%A9talos-de-chocolate-sin-gluten-PRODUCTO-ALCAMPO-400-g/800574",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/NACIONAL-Cereales-Corn-Flakes-500-g/745442",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Muesli-crujiente-sin-az%C3%BAcares-a%C3%B1adidos-500-g/86482",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Muesli-con-frutas-sin-az%C3%BAcar-500-g/86491",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Cereales-muesli-con-fruta-PRODUCTO-ALCAMPO-450-g/625613",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Muesli-con-pepitas-de-chocolate-sin-az%C3%BAcar-500-g/86509",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-barquillos-rellenos-con-sabor-nata-PRODUCTO-ALCAMPO-200-g/514721",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Galletas-de-barqullos-con-relleno-de-cacao-PRODUCTO-ALCAMPO-200-g/514720",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-At%C3%BAn-claro-al-natural-PRODUCTO-ALCAMPO-6-uds-x-56-g/513829",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-At%C3%BAn-claro-en-aceite-de-oliva-lata-de-52-g-pack-de-6-uds/61519",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-At%C3%BAn-claro-en-aceite-de-girasol-PRODUCTO-ALCAMPO-lata-de-52-g-pack-de-6-unds/26028",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-At%C3%BAn-claro-en-escabeche-PRODUCTO-ALCAMPO-lata-de-52-g-pack-de-3-uds/27216",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Bonito-del-norte-en-aceite-de-oliva-PRODUCTO-ALCAMPO-73-g/23149",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Mejillones-peque%C3%B1os-en-escabeche-PRODUCTO-ALCAMPO-69-g/952078",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Mejillones-escabeche-picantes-PRODUCTO-ALCAMPO-lata-de-68-g/25837",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Mejillones-salsa-de-vieira-PRODUCTO-ALCAMPO-65-g/27681",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Mejillones-al-natural-PRODUCTO-ALCAMPO-lata-de-68-g/25843",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Sardinas-en-tomate-PRODUCTO-ALCAMPO-84-g/642698",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Sardinas-en-aceite-de-oliva-PRODUCTO-ALCAMPO-84-g/642693",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Sardinillas-en-escabeche-PRODUCTO-ALCAMPO-lata-65-g/59665",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Sardinillas-picantes-en-aceite-de-girasol-PRODUCTO-ALCAMPO-lata-65-g/59691",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tomate-triturado-PRODUCTO-ALCAMPO-lata-de-400-g/10090",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tomate-triturado-PRODUCTO-ALCAMPO-lata-de-800-g/10074",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tomate-frito-PRODUCTO-ALCAMPO-frasco-de-560-g/26530",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tomate-frito-PRODUCTO-ALCAMPO-brik-de-3-uds-x-210-g/63924",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tomate-frito-con-aceite-de-oliva-PRODUCTO-ALCAMPO-390-g/235732",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Jud%C3%ADas-verdes-cortadas-en-trozos-medianos-PRODUCTO-ALCAMPO-frasco-de-360-g/22383",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Jud%C3%ADas-verdes-planas-seleccionadas-y-troceadas-PRODUCTO-ALCAMPO-1-kg/69547",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Jud%C3%ADas-verdes-redondas-troceadas-y-ultracongeladas-PRODUCTO-ALCAMPO-1-kg/69554",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pimientos-del-Piquillo-enteros-extra-PRODUCTO-ALCAMPO-frasco-de-350-g/24970",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pimientos-del-Piquillo-al-ajillo-en-tiras-PRODUCTO-ALCAMPO-frasco-de-220-g/25065",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Esp%C3%A1rragos-blancos-9-12-piezas-PRODUCTO-ALCAMPO-frasco-de-325-g/24287",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Esp%C3%A1rragos-verdes-delgados-15-35-piezas-PRODUCTO-ALCAMPO-frasco-de-100-g/882435",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Ma%C3%ADz-dulce-PRODUCTO-ALCAMPO-3-uds-x-140-g/28059",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Ma%C3%ADz-dulce-en-grano-ultracongelado-PRODUCTO-ALCAMPO-400-g/69584",
    "https://www.compraonline.alcampo.es/products/ALCAMPO-ECOL%C3%93GICO-Guisantes-al-Natural-ALCAMPO-ECOL%C3%93GICO-Frasco-de-215-g/24936",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Guisantes-finos-PRODUCTO-ALCAMPO-1-kg/69545",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Guisantes-muy-finos-al-natural-PRODUCTO-ALCAMPO-lata-de-280-g/29734",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Champi%C3%B1ones-enteros-PRODUCTO-ALCAMPO-lata-de-185-g/14027",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Champi%C3%B1ones-laminados-PRODUCTO-ALCAMPO-lata-de-185-g/27573",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Corazones-de-alcachofas-seleccionados-PRODUCTO-ALCAMPO-400-g/68666",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Alcachofas-baby-seleccionadas-y-ultracongeladas-PRODUCTO-ALCAMPO-300-g/475893",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Alcachofas-6-8-piezas-PRODUCTO-ALCAMPO-lata-de-240-g/10764",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Corazones-de-alcachofa-6-8-piezas-PRODUCTO-ALCAMPO-165-g/237920",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ECON%C3%93MICO-ALCAMPO-Harina-de-trigo-PRODUCTO-ECON%C3%93MICO-ALCAMPO-1-kg/13643",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Preparado-de-harina-para-pizza-PRODUCTO-ALCAMPO-1-kg/625547",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Harina-de-trigo-especial-reposter%C3%ADa-PRODUCTO-ALCAMPO-1-kg/12060",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Harina-de-trigo-especial-para-fritos-y-rebozados-PRODUCTO-ALCAMPO-1-kg/12057",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Preparado-de-harina-especial-para-bizcochos-PRODUCTO-ALCAMPO-1-kg/625548",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Harina-de-ma%C3%ADz-sin-gluten-controlado-por-la-FACE-PRODUCTO-ALCAMPO-1-kg/13200",
    "https://www.compraonline.alcampo.es/products/Levadura-fresca-LEVANOVA-50g/61956",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Nermelada-de-fresa-PRODUCTO-ALCAMPO-410-g/249782",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Mermelada-de-melocot%C3%B3n-PRODUCTO-ALCAMPO-410-g/249792",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Mermelada-de-naranja-amarga-PRODUCTO-ALCAMPO-410-g/249794",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Miel-de-flores-PRODUCTO-ALCAMPO-1-kg/27193",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Miel-de-azahar-100-Espa%C3%B1a-PRODUCTO-ALCAMPO-350-g/645121",
    "https://www.compraonline.alcampo.es/products/Barra-de-pan-con-masa-madre-de-Fabricaci%C3%B3n-Propia-250g/11848",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pan-de-molde-blanco-con-corteza-especial-tostada-PRODUCTO-ALCAMPO-800-g/11874",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pan-de-molde-100-integral-o-az%C3%BAcares-a%C3%B1adidos-PRODUCTO-ALCAMPO-460-g/475429",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pan-de-molde-blanco-sin-corteza-PRODUCTO-ALCAMPO-450-g/28586",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pan-de-molde-integral-sin-corteza-PRODUCTO-ALCAMPO-450-g/29110",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Maxi-pan-para-burger-PRODUCTO-ALCAMPO-4-udfs-300-g/11443",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tortilla-fresca-de-patatas-sin-cebolla-y-elaborada-sin-gluten-PRODUCTO-ALCAMPO-600-g/84554",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Tortilla-fresca-de-patata-con-cebolla-y-elaborada-sin-gluten-PRODUCTO-ALCAMPO-600-g/84548",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pizza-barbacoa-cocida-en-horno-de-piedra-PRODUCTO-ALCAMPO-400-g/84556",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pizza-4-quesos-cocida-en-horno-de-piedra-PRODUCTO-ALCAMPO-400-g/83498",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Pizza-de-jam%C3%B3n-y-queso-cocida-en-horno-de-piedra-PRODUCTO-ALCAMPO-405-g/83026",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Garbanzos-cocidos-PRODUCTO-ALCAMPO-400-g/24455",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Garbanzo-extra-PRODUCTO-ALCAMPO-1-kg/11790",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Alubias-cocidas-extra-PRODUCTO-ALCAMPO-400-g/24457",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Alubia-ri%C3%B1%C3%B3n-extra-PRODUCTO-ALCAMPO-paquete-de-1-kg/11796",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Alubias-pintas-cocidas-PRODUCTO-ALCAMPO-400-g/549302",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Alubia-pinta-extra-PRODUCTO-ALCAMPO-1-kg/20375",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Lentejas-cocidas-extra-PRODUCTO-ALCAMPO-400-g/24463",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Lentejas-extra-PRODUCTO-ALCAMPO-1-kg/11793",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Ketchup-PRODUCTO-ALCAMPO-560-g/629975",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Mostaza-PRODUCTO-ALCAMPO-bote-de-300-g/431299",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Mayonesa-bocabajo-PRODUCTO-ALCAMPO-bote-de-300-ml/431280",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Gazpacho-pasteurizado-elaborado-con-aceite-de-oliva-virgen-extra-PRODUCTO-ALCAMPO-1-l/71432",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Salmorejo-con-aceite-de-oliva-virgen-extra-PRODUCTO-ALCAMPO-1-l/87442",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Huevos-frescos-de-gallinas-criadas-en-suelo-clase-L-y-cat-A-12-uds/804318",
    "Vacio",
    "https://www.compraonline.alcampo.es/products/PRODUCTO-ALCAMPO-Huevos-frescos-de-gallinas-criadas-en-suelo-clase-L-XL-y-cat-A-12-uds/765110",
    "https://www.compraonline.alcampo.es/products/OVONOVO-Huevo-l%C3%ADquido-30-claras-pasteurizado-OVONOVO-1-l/717853"]

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
            DescripcionXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[1]/div[2]/div[2]/div[1]/h1'
            PrecioXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/span'
            DetalleXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[1]/div[2]/div[2]/div[1]/div[1]/span[2]'
            imagenSRCXPath = '/html/body/div[1]/div/div[1]/div[2]/main/div/div[1]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/img'
                            
            NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
            PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
            DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
            ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
            

            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
            PrecioProducto = PrecioProductoDFE.text[:-1]
            PrecioProducto = PrecioProducto.replace(',', '.')
            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
            ImagenSRC = ImagenDFE.get_attribute("src")
            #Insertar enlace de los productos   
            '''
            sql = 'SELECT id from productos where seccion = %s and subseccion = %s and producto = %s and descripcion = %s and supermercado = %s'
            val = (seccion, seccionDetalle, productos[i], NombreProducto, Supermercado)
            mycursor.execute(sql, val)
            result = mycursor.fetchone()
            if result is not None:
                id = result[0]
                print("ID encontrado:", id)

                sql2 = 'UPDATE productos SET enlace = %s WHERE id = %s'
                val2 = (enlaces[i], id)
                mycursor.execute(sql2, val2)
                mydb.commit()
            else:
                id = None
                print("No se encontró un ID para los criterios proporcionados.")
            '''
            #Insertar tabla productos
            '''
            sql = "INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (seccion, seccionDetalle, productos[i], NombreProducto, Supermercado, ImagenSRC)
            mycursor.execute(sql, val)
            mydb.commit()
            '''

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

        except Exception as ex:
            print("Enlace caido")
        finally:


            print(i)
            print(productos[i])
            print(seccion+' - '+seccionDetalle+':')
            print(NombreProducto + ' ' +PrecioProducto+' '+DetalleProducto)

            id_producto = ''
mycursor.close()
mydb.close()  
driver.quit()
        