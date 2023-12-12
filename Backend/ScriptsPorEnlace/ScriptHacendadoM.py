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

Supermercado = 'Mercadona'

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

enlaces = ["https://tienda.mercadona.es/product/10380/leche-entera-hacendado-brick",
    "https://tienda.mercadona.es/product/10699/leche-entera-sin-lactosa-hacendado-brick",
    "https://tienda.mercadona.es/product/10382/leche-semidesnatada-hacendado-brick",
    "https://tienda.mercadona.es/product/10722/leche-semidesnatada-sin-lactosa-hacendado-brick",
    "https://tienda.mercadona.es/product/10384/leche-desnatada-hacendado-brick",
    "https://tienda.mercadona.es/product/10731/leche-desnatada-sin-lactosa-hacendado-brick",
    
    "https://tienda.mercadona.es/product/20001/yogur-sabores-hacendado-pack-16",
    "https://tienda.mercadona.es/product/22313/yogur-natural-hacendado-pack-6",
    "https://tienda.mercadona.es/product/20559/yogur-griego-natural-hacendado-pack-6",
    "https://tienda.mercadona.es/product/20512/yogur-griego-natural-hacendado-bote",
    "https://tienda.mercadona.es/product/20584/yogur-natural-con-azucar-cana-hacendado-pack-6",
    
    "https://tienda.mercadona.es/product/20716/mantequilla-sin-sal-anadida-hacendado-pastilla",
    "https://tienda.mercadona.es/product/20846/margarina-hacendado-tarrina",
    "https://tienda.mercadona.es/product/15648/bebida-almendras-hacendado-brick",
    "https://tienda.mercadona.es/product/23047/bebida-arroz-sin-azucares-anadidos-hacendado-brick",
    "https://tienda.mercadona.es/product/29314/bebida-soja-0-azucares-hacendado-brick",
    "https://tienda.mercadona.es/product/52640/bebida-avena-hacendado-0-azucar-brick",
    "https://tienda.mercadona.es/product/23753/horchata-chufa-hacendado-brick",
    "https://tienda.mercadona.es/product/15802/mousse-sabor-chocolate-proteinas-hacendado-20-g-proteinas-bote",
    "https://tienda.mercadona.es/product/68322/cuajada-hacendado-pack-4",
    "https://tienda.mercadona.es/product/32358/preparado-polvo-cuajada-azucarada-royal-sabor-lacteo-16-raciones-caja",
    "https://tienda.mercadona.es/product/68149/flan-huevo-hacendado-pack-4",
    "https://tienda.mercadona.es/product/68106/flan-vainilla-con-caramelo-hacendado-pack-6",
    "https://tienda.mercadona.es/product/68271/gelatina-sabores-mango-maracuya-pina-hacendado-gellytina-pack-6",
    "https://tienda.mercadona.es/product/35683/gelatina-0-azucar-sabores-fresa-mandarina-limon-hacendado-gellytina-pack-6",
    "https://tienda.mercadona.es/product/68172/gelatina-sabor-fresa-hacendado-gellytina-pack-6",
    "https://tienda.mercadona.es/product/68137/natillas-sabor-vainilla-hacendado-pack-4",
    "https://tienda.mercadona.es/product/68138/natillas-chocolate-con-leche-hacendado-pack-4",
    "https://tienda.mercadona.es/product/23049/batido-chocolate-hacendado-botella",
    "https://tienda.mercadona.es/product/10050/batido-chocolate-hacendado-pack-6",
    "https://tienda.mercadona.es/product/23051/batido-sabor-fresa-hacendado-botella",
    "https://tienda.mercadona.es/product/10054/batido-sabor-fresa-hacendado-pack-6",
    "https://tienda.mercadona.es/product/23052/batido-sabor-vainilla-hacendado-botella",
    "https://tienda.mercadona.es/product/10051/batido-vainilla-hacendado-pack-6",
    "https://tienda.mercadona.es/product/39010/zumo-pura-naranja-hacendado-brick",
    "https://tienda.mercadona.es/product/39033/zumo-pura-naranja-hacendado-pack-6",
    "https://tienda.mercadona.es/product/39032/zumo-pura-naranja-con-pulpa-hacendado-brick",
    "https://tienda.mercadona.es/product/39919/zumo-naranja-seleccion-hacendado-brick",
    "https://tienda.mercadona.es/product/39129/zumo-pina-uva-hacendado-brick",
    "https://tienda.mercadona.es/product/39130/zumo-pina-uva-hacendado-pack-6",
    "https://tienda.mercadona.es/product/39403/zumo-manzana-hacendado-brick",
    "https://tienda.mercadona.es/product/39404/zumo-manzana-hacendado-pack-6",
    "https://tienda.mercadona.es/product/86039/zumo-melocoton-uva-hacendado-brick",
    "https://tienda.mercadona.es/product/86040/zumo-melocoton-uva-hacendado-pack-6",
    "https://tienda.mercadona.es/product/28472/agua-mineral-grande-aguadoy-mineralizacion-debil-botella",
    "https://tienda.mercadona.es/product/4240/aceite-oliva-04o-hacendado-botella",
    "https://tienda.mercadona.es/product/4204/aceite-oliva-suave-hacendado-garrafa",
    "https://tienda.mercadona.es/product/4740/aceite-oliva-virgen-extra-hacendado-botella",
    "https://tienda.mercadona.es/product/4717/aceite-oliva-virgen-extra-hacendado-garrafa",
    "https://tienda.mercadona.es/product/4046/aceite-girasol-refinado-02o-hacendado-botella",
    "https://tienda.mercadona.es/product/4047/aceite-girasol-refinado-02o-hacendado-garrafa",
    "https://tienda.mercadona.es/product/4940/vinagre-vino-blanco-hacendado-botella",
    "https://tienda.mercadona.es/product/4957/vinagre-manzana-hacendado-botella",
    "https://tienda.mercadona.es/product/4954/vinagre-balsamico-modena-hacendado-botella",
    "Vacio",
    "https://tienda.mercadona.es/product/19731/sal-fina-hacendado-paquete",
    "https://tienda.mercadona.es/product/19733/sal-gruesa-hacendado-paquete",
    "https://tienda.mercadona.es/product/19701/sal-rosa-himalaya-hacendado-bote",
    "https://tienda.mercadona.es/product/29006/bicarbonato-sodico-hacendado-bote",
    "https://tienda.mercadona.es/product/29007/bicarbonato-sodico-hacendado-paquete",
    "https://tienda.mercadona.es/product/22245/patatas-fritas-clasicas-hacendado-pack-2",
    "https://tienda.mercadona.es/product/33439/patatas-fritas-receta-churreria-hacendado-paquete",
    "https://tienda.mercadona.es/product/33624/patatas-fritas-paja-hacendado-paquete",
    "https://tienda.mercadona.es/product/33365/patatas-fritas-lisas-hacendado-paquete",
    "https://tienda.mercadona.es/product/61421/patatas-prefritas-corte-fino-hacendado-ultracongeladas-paquete",
    "https://tienda.mercadona.es/product/61405/patatas-prefritas-corte-grueso-hacendado-ultracongeladas-paquete",
    "https://tienda.mercadona.es/product/33053/aceitunas-manzanilla-hacendado-sin-hueso-tarro",
    "https://tienda.mercadona.es/product/80016/aceitunas-manzanilla-hacendado-con-hueso-tarro",
    "https://tienda.mercadona.es/product/33249/aceitunas-negras-hacendado-sin-hueso-bote",
    "https://tienda.mercadona.es/product/16851/aceitunas-negras-hacendado-con-hueso-bote",
    "https://tienda.mercadona.es/product/34822/palomitas-maiz-con-sal-hacendado-microondas-paquete",
    "https://tienda.mercadona.es/product/34212/palomitas-maiz-sabor-mantequilla-hacendado-microondas-paquete",
    "Vacio",
    "Vacio",
    "https://tienda.mercadona.es/product/82585/galletas-saladas-salpicks-galbusera-paquete",
    "https://tienda.mercadona.es/product/5044/arroz-redondo-hacendado-paquete",
    "https://tienda.mercadona.es/product/5063/arroz-largo-hacendado-paquete",
    "https://tienda.mercadona.es/product/5002/arroz-basmati-aromatico-hacendado-paquete",
    "https://tienda.mercadona.es/product/5020/arroz-vaporizado-hacendado-paquete",
    "https://tienda.mercadona.es/product/6326/macarron-hacendado-paquete",
    "https://tienda.mercadona.es/product/6244/pasta-tiburon-hacendado-paquete",
    "https://tienda.mercadona.es/product/6253/fideua-hacendado-paquete",
    "https://tienda.mercadona.es/product/6238/helices-hacendado-paquete",
    "https://tienda.mercadona.es/product/6278/macarron-rayado-hacendado-paquete",
    "https://tienda.mercadona.es/product/6305/pajaritas-vegetales-hacendado-paquete",
    "https://tienda.mercadona.es/product/6344/helices-con-vegetales-hacendado-paquete",
    "https://tienda.mercadona.es/product/6331/spaghetti-hacendado-paquete",
    "https://tienda.mercadona.es/product/6246/pasta-linguine-hacendado-paquete",
    "https://tienda.mercadona.es/product/19897/azucar-blanco-paquete",
    "https://tienda.mercadona.es/product/22349/azucar-moreno-cana-hacendado-paquete",
    "https://tienda.mercadona.es/product/15923/cafe-molido-mezcla-fuerte-hacendado-paquete",
    "https://tienda.mercadona.es/product/11711/cafe-molido-descafeinado-mezcla-hacendado-paquete",
    "https://tienda.mercadona.es/product/11172/cafe-molido-natural-hacendado-paquete",
    "https://tienda.mercadona.es/product/13592/cafe-molido-descafeinado-natural-hacendado-paquete",
    "https://tienda.mercadona.es/product/11845/cafe-molido-mezcla-marcilla-creme-express-caja",
    "https://tienda.mercadona.es/product/22163/cafe-soluble-classic-hacendado-bote",
    "https://tienda.mercadona.es/product/22164/cafe-soluble-descafeinado-hacendado-bote",
    "https://tienda.mercadona.es/product/14102/galletas-maria-hacendado-paquete",
    "https://tienda.mercadona.es/product/14132/galletas-maria-dorada-hacendado-paquete",
    "https://tienda.mercadona.es/product/14006/galletas-maria-integral-hacendado-paquete",
    "https://tienda.mercadona.es/product/14325/galletas-tostadas-hacendado-paquete",
    "https://tienda.mercadona.es/product/14214/galletas-digestive-hacendado-paquete",
    "https://tienda.mercadona.es/product/14213/galletas-digestive-avena-hacendado-paquete",
    "https://tienda.mercadona.es/product/14212/galletas-cookies-hacendado-40-pepitas-chocolate-paquete",
    "https://tienda.mercadona.es/product/15597/galletas-caocream-hacendado-rellenas-crema-caja",
    "https://tienda.mercadona.es/product/14153/galletas-caocream-chocolate-blanco-hacendado-rellenas-crema-caja",
    "https://tienda.mercadona.es/product/14157/galletas-rebuenas-hacendado-rellenas-chocolate-paquete",
    "https://tienda.mercadona.es/product/64221/helado-cucurucho-fresa-nata-caja",
    "https://tienda.mercadona.es/product/86236/helado-cucurucho-vainilla-hacendado-caja",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://tienda.mercadona.es/product/23851/helado-vegetal-mini-triple-chocolate-base-anacardo-hacendado-caja",
    "https://tienda.mercadona.es/product/64248/helado-negro-hacendado-caja",
    "https://tienda.mercadona.es/product/64000/helado-almendrado-hacendado-caja",
    "https://tienda.mercadona.es/product/64518/helado-vainilla-hacendado-tarrina",
    "https://tienda.mercadona.es/product/52562/helado-stracciatella-hacendado-tarrina",
    "Vacio",
    "https://tienda.mercadona.es/product/52560/helado-vainilla-praline-con-nueces-pecan-hacendado-tarrina",
    "Vacio",
    "https://tienda.mercadona.es/product/64400/helado-chocolate-hacendado-con-trocitos-sabor-chocolate-tarrina",
    "Vacio",
    "https://tienda.mercadona.es/product/64509/sorbete-con-limon-hacendado-tarrina",
    "https://tienda.mercadona.es/product/9264/cereales-rellenos-leche-hacendado-caja",
    "https://tienda.mercadona.es/product/9377/cereales-rellenos-chocolate-avellana-hacendado-paquete",
    "https://tienda.mercadona.es/product/9222/copos-avena-bruggen-caja",
    "Vacio",
    "Vacio",
    "https://tienda.mercadona.es/product/9592/cereales-arroz-inflado-choco-rice-hacendado-con-chocolate-caja",
    "https://tienda.mercadona.es/product/9488/cereales-copos-trigo-integral-arroz-hacendado-0-azucares-anadidos-linnea-v-caja",
    "https://tienda.mercadona.es/product/9508/cereales-copos-trigo-chocodays-hacendado-con-chocolate-caja",
    "Vacio",
    "https://tienda.mercadona.es/product/22966/cereales-copos-maiz-corn-flakes-hacendado-0-azucares-anadidos-caja",
    "https://tienda.mercadona.es/product/35892/muesli-crunchy-hacendado-0-azucares-anadidos-0-edulcorantes-paquete",
    "https://tienda.mercadona.es/product/9356/muesli-crunchy-hacendado-con-fruta-20-fruta-paquete",
    "https://tienda.mercadona.es/product/9357/muesli-crunchy-hacendado-con-frutos-secos-paquete",
    "https://tienda.mercadona.es/product/9355/muesli-crunchy-hacendado-con-chocolate-15-chocolate-paquete",
    "https://tienda.mercadona.es/product/14576/barquillos-rellenos-sabor-nata-hacendado-paquete",
    "https://tienda.mercadona.es/product/14135/barquillos-rellenos-chocolate-hacendado-paquete",
    "https://tienda.mercadona.es/product/18018/atun-claro-natural-hacendado",
    "https://tienda.mercadona.es/product/18002/atun-claro-aceite-oliva-hacendado-pack-6",
    "https://tienda.mercadona.es/product/18055/atun-claro-aceite-girasol-hacendado-pack-6",
    "https://tienda.mercadona.es/product/18031/atun-claro-escabeche-blanco-hacendado",
    "https://tienda.mercadona.es/product/18116/bonito-norte-aceite-oliva-hacendado-pack-2",
    "https://tienda.mercadona.es/product/18108/bonito-norte-escabeche-hacendado-lata",
    "https://tienda.mercadona.es/product/18619/mejillones-escabeche-hacendado-pequenos-13-18-piezas-lata",
    "https://tienda.mercadona.es/product/18621/mejillones-picantes-escabeche-hacendado-pequenos-13-18-piezas-lata",
    "https://tienda.mercadona.es/product/18622/mejillones-salsa-vieira-hacendado-pequenos-13-18-piezas-lata",
    "https://tienda.mercadona.es/product/18620/mejillones-natural-hacendado-pequenos-15-20-piezas-lata",
    "https://tienda.mercadona.es/product/18209/sardinillas-tomate-hacendado-6-12-ud-pack-2",
    "https://tienda.mercadona.es/product/18225/sardinas-aceite-oliva-hacendado-pack-2",
    "Vacio",
    "https://tienda.mercadona.es/product/18211/sardinillas-escabeche-hacendado-6-10-ud-pack-2",
    "https://tienda.mercadona.es/product/18212/sardinillas-picantes-aceite-girasol-hacendado-6-12-ud-pack-2",
    "https://tienda.mercadona.es/product/16044/tomate-triturado-hacendado-freir-bote",
    "https://tienda.mercadona.es/product/16043/tomate-triturado-hacendado-freir-bote",
    "https://tienda.mercadona.es/product/17108/tomate-frito-hacendado-tarro",
    "https://tienda.mercadona.es/product/17132/tomate-frito-hacendado-pack-3",
    "Vacio",
    "https://tienda.mercadona.es/product/17163/tomate-frito-receta-artesana-hacendado-con-aceite-oliva-tarro",
    "https://tienda.mercadona.es/product/16313/judias-verdes-planas-hacendado-tarro",
    "https://tienda.mercadona.es/product/16315/judias-verdes-redondas-hacendado-tarro",
    "https://tienda.mercadona.es/product/61283/judia-verde-plana-hacendado-ultracongelada-paquete",
    "https://tienda.mercadona.es/product/61282/judia-verde-redonda-hacendado-ultracongelada-paquete",
    "https://tienda.mercadona.es/product/16005/pimientos-piquillo-enteros-hacendado-extra-tarro",
    "Vacio",
    "https://tienda.mercadona.es/product/16008/pimientos-piquillo-tiras-con-ajo-hacendado-tarro",
    "Vacio",
    "https://tienda.mercadona.es/product/18562/esparragos-medianos-hacendado-tarro",
    "https://tienda.mercadona.es/product/16510/esparragos-delgados-verdes-hacendado-enteros-tarro",
    "https://tienda.mercadona.es/product/16712/maiz-dulce-hacendado-pack-3",
    "https://tienda.mercadona.es/product/61289/maiz-dulce-hacendado-ultracongelado-paquete",
    "Vacio",
    "https://tienda.mercadona.es/product/61215/guisante-fino-hacendado-ultracongelado-paquete",
    "https://tienda.mercadona.es/product/16416/guisantes-extra-hacendado-bote",
    "https://tienda.mercadona.es/product/61200/guisante-muy-tierno-hacendado-ultracongelado-paquete",
    "Vacio",
    "https://tienda.mercadona.es/product/16415/guisantes-extra-hacendado-pack-3",
    "https://tienda.mercadona.es/product/16625/champinon-entero-hacendado-bote",
    "https://tienda.mercadona.es/product/16618/champinones-laminados-hacendado-bote",
    "https://tienda.mercadona.es/product/61274/alcachofa-corazones-hacendado-ultracongelada-paquete",
    "https://tienda.mercadona.es/product/61205/alcachofa-baby-hacendado-ultracongelada-paquete",
    "https://tienda.mercadona.es/product/16039/corazones-alcachofas-hacendado-bote",
    "https://tienda.mercadona.es/product/16040/corazones-alcachofa-hacendado-tarro",
    "https://tienda.mercadona.es/product/29100/harina-trigo-hacendado-paquete",
    "https://tienda.mercadona.es/product/29134/harina-integral-trigo-hacendado-paquete",
    "https://tienda.mercadona.es/product/23646/preparado-pizzas-hacendado-paquete",
    "Vacio",
    "https://tienda.mercadona.es/product/29180/harina-semolosa-trigo-hacendado-especial-fritos-paquete",
    "https://tienda.mercadona.es/product/29017/preparado-bizcochos-con-levadura-incorporada-hacendado-paquete",
    "https://tienda.mercadona.es/product/29165/harina-maiz-blanco-precocida-hacendado-paquete",
    "https://tienda.mercadona.es/product/87811/levadura-fresca-levital-paquete",
    "https://tienda.mercadona.es/product/86755/mermelada-fresa-hacendado-tarro",
    "https://tienda.mercadona.es/product/86684/mermelada-melocoton-hacendado-tarro",
    "https://tienda.mercadona.es/product/15076/mermelada-naranja-amarga-hacendado-tarro",
    "https://tienda.mercadona.es/product/15436/miel-flores-hacendado-tarro",
    "Vacio",
    "https://tienda.mercadona.es/product/83202.1/barra-pan",
    "https://tienda.mercadona.es/product/83867/pan-molde-blanco-familiar-hacendado-paquete",
    "https://tienda.mercadona.es/product/82328/pan-molde-100-integral-hacendado-paquete",
    "https://tienda.mercadona.es/product/82322/pan-molde-blanco-sin-corteza-hacendado-paquete",
    "https://tienda.mercadona.es/product/23643/pan-molde-100-integral-sin-corteza-hacendado-0-azucares-anadidos-paquete",
    "https://tienda.mercadona.es/product/82330/pan-maxi-hamburguesa-hacendado-paquete",
    "https://tienda.mercadona.es/product/82332/pan-hot-dog-hacendado-paquete",
    "https://tienda.mercadona.es/product/80771/tortilla-patata-hacendado-bandeja",
    "https://tienda.mercadona.es/product/80895/tortilla-patata-cebolla-hacendado-con-aceite-oliva-bandeja",
    "https://tienda.mercadona.es/product/63613/pizza-barbacoa-hacendado",
    "https://tienda.mercadona.es/product/63580/pizza-4-quesos-hacendado",
    "https://tienda.mercadona.es/product/63581/pizza-jamon-queso-hacendado",
    "https://tienda.mercadona.es/product/63645/pizza-pollo-bacon-hacendado",
    "https://tienda.mercadona.es/product/26029/garbanzo-cocido-hacendado-tarro",
    "https://tienda.mercadona.es/product/5214/garbanzo-hacendado-categoria-extra-paquete",
    "https://tienda.mercadona.es/product/26019/alubia-cocida-blanca-hacendado-tarro",
    "https://tienda.mercadona.es/product/5124/alubia-blanca-hacendado-categoria-extra-paquete",
    "https://tienda.mercadona.es/product/26001/alubia-cocida-pinta-hacendado-tarro",
    "https://tienda.mercadona.es/product/23453/alubia-pinta-hacendado-categoria-extra-paquete",
    "https://tienda.mercadona.es/product/26030/lenteja-cocida-hacendado-tarro",
    "https://tienda.mercadona.es/product/5325/lenteja-hacendado-categoria-extra-paquete",
    "https://tienda.mercadona.es/product/23579/ketchup-hacendado-bote",
    "https://tienda.mercadona.es/product/23410/mostaza-clasica-hacendado-bote",
    "https://tienda.mercadona.es/product/13407/mayonesa-hacendado-bote",
    "https://tienda.mercadona.es/product/39900/gazpacho-fresco-hacendado-botella",
    "https://tienda.mercadona.es/product/39901/salmorejo-fresco-hacendado-botella",
    "https://tienda.mercadona.es/product/31504/huevos-grandes-l-paquete",
    "https://tienda.mercadona.es/product/31505/huevos-medianos-m-paquete",
    "https://tienda.mercadona.es/product/31592/huevos-super-grandes-xl-paquete",
    "https://tienda.mercadona.es/product/31312/claras-huevo-liquidas-pasteurizadas-botella"]

seccion = ''
seccionDetalle = ''
id_producto = ''
driver = webdriver.Firefox()

CPIntroducido = False
for i in range(229):
    if enlaces[i] == 'Vacio':
        print(i)
        print('No hay enlace')
    else:
        url = enlaces[i]
        driver.get(url)
        sleep(3)

        if CPIntroducido == False:
            driver.find_element("xpath", '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/form/div/input').send_keys('28051/n')
            driver.find_element("xpath", '/html/body/div[1]/div[3]/div[1]/div/div[2]/div/form/button').click()
            CPIntroducido = True    
            driver.get(url)
            sleep(2)

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
            DescripcionXPath = '.title2-r'
            PrecioXPath = '.large-b'
            DetalleXPath = 'span.headline1-r:nth-child(3)'
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
                except:
                    print('Enlace caido')


        print(i)
        print(productos[i])
        print(seccion+' - '+seccionDetalle+':')
        print(NombreProducto + ' ' + PrecioProducto + ' ' + DetalleProducto)
        
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
                    
mycursor.close()
mydb.close()         
driver.quit()
        