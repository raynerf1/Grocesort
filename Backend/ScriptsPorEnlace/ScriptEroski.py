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

Supermercado = 'Eroski'

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

enlaces = ["https://supermercado.eroski.es/es/productdetail/18672295-leche-entera-del-pais-vasco-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/18843334-leche-entera-sin-lactosa-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/18672311-leche-semidesnatada-del-pais-vasco-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/14879274-leche-semidesnatada-sin-lactosa-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/447300-leche-desnatada-bomilk-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/16623084-leche-sin-lactosa-desnatada-eroski-brik-1-litro/",    

    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/4810149-yogur-natural-eroski-basic-pack-8x125-g/",
    "https://supermercado.eroski.es/es/productdetail/13228697-yogur-desnatado-natural-eroski-basic-pack-6x125-g/",
    "https://supermercado.eroski.es/es/productdetail/24284515-yogur-griego-natural-light-2-margui-tarrina-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/16237992-griego-natural-azucarado-eroski-pack-6x125-g/",

    "https://supermercado.eroski.es/es/productdetail/15636475-mantequilla-eroski-pastilla-250-g/",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/24661928-bebida-de-almendra-eroski-bio-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/24637506-bebida-de-arroz-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/24637365-bebida-de-soja-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/24637373-bebida-de-avena-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/3956554-horchata-eroski-botella-1-litro/",

    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/17426180-cuajada-natural-eroski-pack-4x125-g/",
    "https://supermercado.eroski.es/es/productdetail/17426529-cuajada-natural-azucarada-eroski-pack-4x125-g/",
    "https://supermercado.eroski.es/es/productdetail/20118360-flan-de-huevo-eroski-pack-4x100-g/",
    "https://supermercado.eroski.es/es/productdetail/13228671-flan-de-vainilla-eroski-basic-pack-6x100-g/",

    "Vacio",
    "Vacio",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/17416157-natillas-de-vainilla-eroski-pack-4x120-g/",
    "https://supermercado.eroski.es/es/productdetail/17416249-natillas-de-chocolate-eroski-pack-4x120-g/",

    "https://supermercado.eroski.es/es/productdetail/23894280-batido-de-cacao-eroski-botella-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/10825487-batido-de-cacao-eroski-pack-6x200-ml/",
    "https://supermercado.eroski.es/es/productdetail/23894421-batido-de-fresa-eroski-botella-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/10825503-batido-de-fresa-eroski-pack-6x200-ml/",
    "https://supermercado.eroski.es/es/productdetail/23894439-batido-de-vainilla-eroski-botella-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/10825495-batido-de-vainilla-eroski-pack-6x200-ml/",

    "https://supermercado.eroski.es/es/productdetail/19539204-zumo-de-naranja-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/10864825-zumo-de-naranja-eroski-pack-6x20-cl/",
    "https://supermercado.eroski.es/es/productdetail/5299912-zumo-natural-de-naranja-con-pulpa-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/8624777-zumo-de-naranja-concentrado-eroski-basic-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/19539220-zumo-de-pina-manzana-y-uva-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/10864619-zumo-de-pina-manzana-y-uva-eroski-pack-6x20-cl/4",
    "https://supermercado.eroski.es/es/productdetail/19539188-zumo-de-manzana-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/10864809-zumo-de-manzana-eroski-pack-6x20-cl/",
    "Vacio",
    "Vacio",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/377176-aceite-de-oliva-04-eroski-botella-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/366666-aceite-de-oliva-suave-eroski-garrafa-5-litros/",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/377093-aceite-de-oliva-sabor-eroski-garrafa-5-litros/",
    "https://supermercado.eroski.es/es/productdetail/377150-aceite-de-girasol-eroski-botella-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/322859-aceite-de-girasol-eroski-garrafa-5-litros/",

    "https://supermercado.eroski.es/es/productdetail/318410-vinagre-de-vino-blanco-eroski-basic-botella-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/21662283-vinagre-de-manzana-eroski-basic-botella-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/8382053-vinagre-balsamico-de-modena-eroski-botella-25-cl/",
    "https://supermercado.eroski.es/es/productdetail/16829236-vinagre-de-jerez-eroski-botella-50-cl/",

    "https://supermercado.eroski.es/es/productdetail/917372-sal-marina-fina-eroski-basic-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/917323-sal-marina-gruesa-eroski-basic-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/20965372-sal-rosa-del-himalaya-fina-toque-paquete-250-g/",

    "https://supermercado.eroski.es/es/productdetail/5481858-bicarbonato-costa-bote-200-g/",
    "https://supermercado.eroski.es/es/productdetail/22926232-bicarbonato-sal-costa-paquete-1-kg/",

    "Vacio",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/22457345-patatas-paja-eroski-bolsa-100-g/",
    "https://supermercado.eroski.es/es/productdetail/49692-patatas-fritas-lisas-eroski-basic-bolsa-170-g/",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/211326-patata-prefrita-eroski-basic-bolsa-1-kg/",

    "https://supermercado.eroski.es/es/productdetail/12526406-aceitunas-verdes-sin-hueso-eroski-frasco-400-g-/",
    "https://supermercado.eroski.es/es/productdetail/12526414-aceitunas-verdes-con-hueso-eroski-frasco-500-g-/",
    "https://supermercado.eroski.es/es/productdetail/4291845-aceitunas-negras-sin-hueso-eroski-lata-150-g/",
    "https://supermercado.eroski.es/es/productdetail/359216-aceitunas-negras-con-hueso-eroski-lata-185-g/",

    "https://supermercado.eroski.es/es/productdetail/23696271-palomitas-para-microondas-con-sal-eroski-pack-3x90-g/",
    "https://supermercado.eroski.es/es/productdetail/23696289-palomitas-para-microondas-sabor-mantequilla-eroski-pack-3x90-g/",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/25558081-galletas-saladas-mini-cracker-favorita-bote-350-g/",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/300434-arroz-extra-eroski-basic-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/4374161-arroz-largo-eroski-basic-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/9160615-arroz-basmati-eroski-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/4374153-arroz-vaporizado-eroski-paquete-1-kg/",

    "https://supermercado.eroski.es/es/productdetail/361998-macarrones-eroski-basic-paquete-500-g/",
    "https://supermercado.eroski.es/es/productdetail/70540-tiburon-eroski-paquete-500-g/",
    "https://supermercado.eroski.es/es/productdetail/70532-fideua-eroski-paquete-500-g/",
    "https://supermercado.eroski.es/es/productdetail/2685857-pasta-de-espirales-eroski-paquete-500-g/",
    "Vacio",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/2685899-espirales-con-vegetales-eroski-paquete-500-g/",
    "https://supermercado.eroski.es/es/productdetail/367391-spaghetti-eroski-basic-paquete-500-g/",
    "https://supermercado.eroski.es/es/productdetail/367409-tallarines-eroski-paquete-500-g/",

    "https://supermercado.eroski.es/es/productdetail/2453884-azucar-blanco-azucarera-paquete-1-kg/",
    "Vacio",

    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/5355789-galleta-maria-eroski-basic-pack-4x200-g/",
    "Vacio",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/5355805-galleta-tostada-eroski-basic-pack-4x200-g/",
    "https://supermercado.eroski.es/es/productdetail/5848049-galleta-digestive-eroski-paquete-800-g/",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/23113509-galleta-cookies-sin-palma-eroski-paquete-225-g/",
    "Vacio",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/5848080-galleta-rellena-de-chocolate-sin-palma-eroski-paquete-500-g/",

    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/25473505-helado-de-vainilla-eroski-tarrina-1-l/",
    "https://supermercado.eroski.es/es/productdetail/25473539-helado-de-stracciatella-eroski-tarrina-900-ml/",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/25473513-sorbete-de-limon-eroski-tarrina-1-l/",

    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/23118839-cereales-rellenos-de-chocolate-eroski-caja-500-g/",
    "https://supermercado.eroski.es/es/productdetail/23848567-copos-de-avena-integrales-eroski-bio-paquete-500-g/",
    "Vacio",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/23118912-cereales-de-arroz-inflado-chocolate-eroski-caja-500-g/",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/23117377-cereales-petalos-de-trigo-de-chocolate-eroski-caja-500-g/",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/733915-muesli-de-frutas-frutos-secos-eroski-caja-500-g/",
    "https://supermercado.eroski.es/es/productdetail/733915-muesli-de-frutas-frutos-secos-eroski-caja-500-g/",
    "https://supermercado.eroski.es/es/productdetail/733923-cereales-muesli-crunch-con-dos-chocolates-eroski-caja-500-g/",

    "https://supermercado.eroski.es/es/productdetail/25208224-barquillo-de-nata-sin-azucar-eroski-paquete-140-g/",
    "https://supermercado.eroski.es/es/productdetail/25208216-barquillo-de-chocolate-y-avellana-eroski-paquete-160-g/",

    "https://supermercado.eroski.es/es/productdetail/21789656-atun-claro-al-natural-eroski-pack-6x56-g/",
    "https://supermercado.eroski.es/es/productdetail/413864-atun-claro-en-aceite-de-oliva-eroski-lata-111-g/",
    "https://supermercado.eroski.es/es/productdetail/5348628-atun-claro-en-aceite-de-girasol-eroski-pack-6x80-g/",
    "https://supermercado.eroski.es/es/productdetail/900782-atun-claro-en-escabeche-eroski-pack-3x80-g/",

    "Vacio",
    "Vacio",

    "Vacio",
    "Vacio",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/1246396-mejillon-al-natural-1418-piezas-eroski-lata-69-g/",

    "https://supermercado.eroski.es/es/productdetail/2294114-sardina-en-tomate-eroski-lata-115-g/",
    "https://supermercado.eroski.es/es/productdetail/2294171-sardina-en-aceite-de-oliva-35-piezas-eroski-lata-115-g/",
    "Vacio",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/2294106-sardina-picantes-eroski-lata-115-g/",

    "https://supermercado.eroski.es/es/productdetail/307892-tomate-triturado-eroski-basic-lata-400-g/",
    "https://supermercado.eroski.es/es/productdetail/320267-tomate-triturado-eroski-basic-lata-800-g/",
    "https://supermercado.eroski.es/es/productdetail/316216-tomate-frito-eroski-frasco-550-g-/",
    "https://supermercado.eroski.es/es/productdetail/12771838-tomate-frito-eroski-basic-pack-3x390-g/",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/7390586-tomate-frito-casero-con-aceite-de-oliva-eroski-frasco-350-g-/",

    "https://supermercado.eroski.es/es/productdetail/2811933-judia-verde-troceada-calidad-i-eroski-frasco-350-g/",
    "https://supermercado.eroski.es/es/productdetail/21660600-judia-redonda-eroski-frasco-360-g/",
    "https://supermercado.eroski.es/es/productdetail/19519081-judias-verdes-planas-eroski-bolsa-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/19519115-judias-verdes-redondas-eroski-bolsa-1-kg/",

    "https://supermercado.eroski.es/es/productdetail/16940280-pimiento-de-piquillo-entero-eroski-frasco-260-g/",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/22238034-pimiento-del-piquillo-en-tiras-con-ajo-eroski-frasco-225-g/",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/2424059-esparrago-grueso-612-piezas-eroski-frasco-205-g/",
    "https://supermercado.eroski.es/es/productdetail/5965793-esparrago-verde-eroski-frasco-185-g/",

    "Vacio",
    "Vacio",

    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/2723252-champinon-entero-extra-eroski-lata-185-g/",
    "https://supermercado.eroski.es/es/productdetail/2723237-champinon-laminado-eroski-basic-lata-185-g/",

    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/362442-harina-de-trigo-eroski-basic-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/17043266-harina-integral-gallo-paquete-1-kg/",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/4270583-harina-de-trigo-para-reposteria-eroski-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/4270591-harina-de-trigo-para-fritos-eroski-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/7390396-harina-con-levadura-para-bizcochos-gallo-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/2570935-harina-de-maiz-pan-paquete-1-kg/",

    "https://supermercado.eroski.es/es/productdetail/18870931-levadura-fresca-levanova-pack-2x25-g/",

    "https://supermercado.eroski.es/es/productdetail/23415359-mermelada-de-fresa-eroski-basic-frasco-340-g/",
    "https://supermercado.eroski.es/es/productdetail/23415300-mermelada-de-melocoton-eroski-basic-frasco-340-g/",
    "https://supermercado.eroski.es/es/productdetail/23414717-mermelada-de-naranja-eroski-basic-frasco-350-g/",

    "https://supermercado.eroski.es/es/productdetail/6300610-miel-mil-flores-eroski-basic-frasco-1-kg-/",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/20360343-baguette-eroski-natur-250-g/",
    "https://supermercado.eroski.es/es/productdetail/17946732-pan-de-molde-con-corteza-eroski-basic-paquete-820-g/",
    "https://supermercado.eroski.es/es/productdetail/22444046-pan-de-molde-integral-con-corteza-eroski-paquete-460-g/",
    "https://supermercado.eroski.es/es/productdetail/15649726-pan-de-molde-sin-corteza-eroski-paquete-450-g/",
    "https://supermercado.eroski.es/es/productdetail/15649742-pan-de-molde-integral-sin-corteza-eroski-paquete-450-g/",
    "https://supermercado.eroski.es/es/productdetail/15700891-pan-hamburguesa-maxiburguers-eroski-4-unid-paquete-300-g/",
    "https://supermercado.eroski.es/es/productdetail/15700917-hot-dog-eroski-6-uds-paquete-330-g/",

    "https://supermercado.eroski.es/es/productdetail/22920979-tortilla-fresca-sin-cebolla-eroski-1-ud-500-g/",
    "https://supermercado.eroski.es/es/productdetail/22920805-tortilla-fresca-con-cebolla-eroski-1-ud-500-g/",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/18731240-pizza-de-4-quesos-eroski-1-ud-400-g/",
    "https://supermercado.eroski.es/es/productdetail/18731224-pizza-de-jamon-queso-eroski-1-ud-400-g/",
    "Vacio",

    "https://supermercado.eroski.es/es/productdetail/336750-garbanzos-cocidos-eroski-basic-frasco-400-g-/",
    "https://supermercado.eroski.es/es/productdetail/300293-garbanzo-extra-eroski-basic-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/336164-alubia-blanca-eroski-basic-frasco-400-g-/",
    "https://supermercado.eroski.es/es/productdetail/300210-alubia-blanca-larga-eroski-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/20389029-alubia-cocida-pinta-eroski-basic-frasco-400-g/",
    "https://supermercado.eroski.es/es/productdetail/20232443-alubia-pinta-eroski-basic-paquete-1-kg/",
    "https://supermercado.eroski.es/es/productdetail/446641-lenteja-cocidas-eroski-basic-frasco-400-g/",
    "https://supermercado.eroski.es/es/productdetail/309575-lenteja-eroski-basic-paquete-1-kg/",

    "https://supermercado.eroski.es/es/productdetail/12451431-ketchup-eroski-basic-bote-560-g/",
    "https://supermercado.eroski.es/es/productdetail/24157844-mostaza-eroski-bote-320-g/",
    "https://supermercado.eroski.es/es/productdetail/14897029-mayonesa-eroski-basic-frasco-450-ml/",
    "https://supermercado.eroski.es/es/productdetail/5084348-gazpacho-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/15783947-salmorejo-eroski-brik-1-litro/",
    "https://supermercado.eroski.es/es/productdetail/19481977-huevo-fresco-l-suelo-pais-vasco-eroski-carton-12-uds/",
    "https://supermercado.eroski.es/es/productdetail/17080961-huevo-fresco-m-pais-vasco-eroski-carton-12-uds/",
    "Vacio",
    "https://supermercado.eroski.es/es/productdetail/24114365-clara-de-huevo-pasteurizada-hobea-botella-1-litro/"]
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
            print('La pagina esta caida')
        finally:
            print(i)
            '''print(productos[i])'''
            print(seccion+' - '+seccionDetalle+':')
            print(NombreProducto + ' ' +PrecioProducto)

            '''
            sql = "INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (seccion, seccionDetalle, productos[i], NombreProducto, Supermercado, ImagenSRC)
            mycursor.execute(sql, val)
            mydb.commit()
            '''
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
            

            try:
                    sql = "SELECT id from productos where producto = %s and descripcion = %s and supermercado = %s "
                    valSelect = (productos[i], NombreProducto, Supermercado)
                    mycursor.execute(sql, valSelect)
                    result = mycursor.fetchone()
                    if result:
                            id_producto = result[0]
                            #print('La id en DB es ', id_producto)
                            sql = "INSERT INTO precios (id, producto, supermercado, precio, detalle, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
                            val = (id_producto, productos[i], Supermercado, PrecioProducto, '', FechaActual)
                            
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

            
mycursor.close()
mydb.close()  
driver.quit()
        