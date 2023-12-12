from time import sleep
from selenium import webdriver
import unicodedata
from datetime import date
import mysql.connector

EnlaceCaido = False
FechaActual=date.today()

mydb = mysql.connector.connect(
  host="hostingmysql335.nominalia.com",
  user="rayner",
  password="marenas19",
  database='bdprecios'
)
mycursor = mydb.cursor()

Supermercado = 'Carrefour'

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

enlaces = ["https://www.carrefour.es/supermercado/leche-entera-carrefour-brik-1-l/R-521006992/p",
    "https://www.carrefour.es/supermercado/leche-entera-carrefour-sin-lactosa-brik-1-l/R-847400344/p",
    "https://www.carrefour.es/supermercado/leche-semidesnatada-carrefour-brik-1-l/R-521007071/p",
    "https://www.carrefour.es/supermercado/leche-semidesnatada-carrefour-sin-lactosa-brik-1-l/R-714713105/p",
    "https://www.carrefour.es/supermercado/leche-desnatada-carrefour-brik-1-l/R-521007093/p",
    "https://www.carrefour.es/supermercado/leche-desnatada-carrefour-sin-lactosa-brik-1-l/R-714713109/p",

    "https://www.carrefour.es/supermercado/yogur-de-fresa-de-galleta-de-platano-y-de-frutos-del-bosque-de-limon-y-de-coco-carrefour-sin-gluten-pack-de-16-unidades-de-125-g/R-VC4AECOMM-025971/p",
    "https://www.carrefour.es/supermercado/yogur-natural-carrefour-pack-de-8-unidades-de-125-g/R-VC4AECOMM-441067/p",
    "https://www.carrefour.es/supermercado/yogur-griego-natural-carrefour-extra-pack-de-6-unidades-de-125-g/R-VC4AECOMM-621804/p",
    "https://www.carrefour.es/supermercado/yogur-griego-natural-carrefour-1-kg/R-843506598/p",
    "https://www.carrefour.es/supermercado/yogur-griego-natural-azucarado-carrefour-extra-pack-de-6-unidades-de-125-g/R-VC4AECOMM-621853/p",
    
    "https://www.carrefour.es/supermercado/mantequilla-pastilla-sin-sal-carrefour-250-g/R-fprod1350157/p",
    "https://www.carrefour.es/supermercado/margarina-carrefour-500-g/R-prod830327/p",
    "https://www.carrefour.es/supermercado/bebida-de-almendra-calcio-carrefour-sin-gluten-brik-1-l/R-VC4AECOMM-554218/p",
    "https://www.carrefour.es/supermercado/bebida-de-arroz-calcio-sin-azucar-anadido-carrefour-sin-gluten-brik-1-l/R-VC4AECOMM-554214/p",
    "https://www.carrefour.es/supermercado/bebida-de-soja-sin-azucar-anadido-carrefour-sin-gluten-brik-1-l/R-823818537/p",
    "https://www.carrefour.es/supermercado/bebida-de-avena-calcio-sin-azucar-anadido-carrefour-brik-1-l/R-VC4AECOMM-554220/p",
    "https://www.carrefour.es/supermercado/horchata-de-chufa-carrefour-sin-gluten-brik-1-l/R-521007113/p",

    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.carrefour.es/supermercado/flan-de-huevo-al-bano-maria-carrefour-classic-sin-gluten-pack-de-4-unidades-de-100-g/R-521029829/p",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.carrefour.es/supermercado/natillas-de-chocolate-carrefour-pack-de-4-unidades-de-125-g/R-837832786/p",
    "https://www.carrefour.es/supermercado/batido-de-cacao-carrefour-sin-gluten-botella-1-l/R-819256512/p",
    "https://www.carrefour.es/supermercado/batido-de-cacao-carrefour-sin-gluten-pack-de-6-brik-de-200-ml/R-VC4AECOMM-551221/p",
    "https://www.carrefour.es/supermercado/batido-de-fresa-oey-botella-750-ml/R-664810660/p",
    "https://www.carrefour.es/supermercado/batido-de-fresa-carrefour-sin-gluten-pack-de-3-brik-de-200-ml/R-VC4AECOMM-551212/p",
    "https://www.carrefour.es/supermercado/batido-de-vainilla-40-menos-azucar-puleva-sin-gluten-botella-1-l/R-859001938/p",
    "https://www.carrefour.es/supermercado/batido-de-vainilla-carrefour-sin-gluten-pack-de-3-brik-de-200-ml/R-VC4AECOMM-551209/p",
    "https://www.carrefour.es/supermercado/zumo-de-naranja-carrefour-brik-1-l/R-745415924/p",
    "https://www.carrefour.es/supermercado/nectar-de-naranja-sin-azucar-anadido-carrefour-pack-de-6-brik-de-20-cl/R-VC4AECOMM-670947/p",
    "https://www.carrefour.es/supermercado/zumo-de-naranja-carrefour-con-pulpa-brik-1-l/R-823705656/p",
    "https://www.carrefour.es/supermercado/zumo-de-naranja-carrefour-ecologico-exprimido-sin-pulpa-brik-1-l/R-VC4AECOMM-438468/p",
    "https://www.carrefour.es/supermercado/zumo-de-pina-carrefour-brik-1-l/R-521030032/p",
    "https://www.carrefour.es/supermercado/bebida-de-pina-carrefour-sin-azucar-pack-de-6-briks-de-20-cl/R-prod730840/p",
    "https://www.carrefour.es/supermercado/zumo-de-manzana-carrefour-brik-1-l/R-820614218/p",
    "https://www.carrefour.es/supermercado/zumo-de-manzana-carrefour-pack-de-6-briks-de-20-cl/R-704502395/p",
    "https://www.carrefour.es/supermercado/bebida-de-melocoton-carrefour-sin-azucar-anadido-pbrik-1-l/R-prod730831/p",
    "https://www.carrefour.es/supermercado/bebida-de-melocoton-carrefour-sin-azucar-pack-de-6-briks-de-20-cl/R-prod730835/p",
    "https://www.carrefour.es/supermercado/agua-mineral-carrefour-2-l/R-520661068/p",
    "https://www.carrefour.es/supermercado/aceite-de-oliva-suave-04-carrefour-1-l/R-526600666/p",
    "https://www.carrefour.es/supermercado/aceite-de-oliva-suave-04-carrefour-garrafon-5-l/R-526600668/p",
    "https://www.carrefour.es/supermercado/aceite-de-oliva-intenso-1-carrefour-1-l/R-526600670/p",
    "https://www.carrefour.es/supermercado/aceite-de-oliva-intenso-1-carrefour-garrafa-5-l/R-526600672/p",
    "https://www.carrefour.es/supermercado/aceite-de-girasol-carrefour-classic-1-l/R-521009768/p",
    "https://www.carrefour.es/supermercado/aceite-de-girasol-para-freir-carrefour-garrafa-5-l/R-520661084/p",
    "https://www.carrefour.es/supermercado/vinagre-de-vino-blanco-carrefour-1-l/R-531705309/p",
    "https://www.carrefour.es/supermercado/vinagre-de-manzana-carrefour-1-l/R-520660380/p",
    "https://www.carrefour.es/supermercado/crema-de-vinagre-balsamico-de-modena-sin-azucar-vulpi-sin-gluten-400-ml/R-828922471/p",
    "https://www.carrefour.es/supermercado/vinagre-de-jerez-carrefour-750-ml/R-520660398/p",
    "https://www.carrefour.es/supermercado/sal-marina-fina-carrefour-1-kg/R-521005130/p",
    "https://www.carrefour.es/supermercado/sal-marina-gruesa-carrefour-1-kg/R-521005136/p",
    "https://www.carrefour.es/supermercado/molinillo-sal-rosa-del-himalaya-carrefour-seleccion-100-g/R-fprod1260107/p",
    "https://www.carrefour.es/supermercado/bicarbonato-sodico-carrefour-300-g/R-VC4AECOMM-436546/p",
    "Vacio",
    "Vacio",
    "https://www.carrefour.es/supermercado/patatas-fritas-churreria-en-aceite-de-girasol-carrefour-pack-de-2-bolsas-de-150-g/R-796400335/p",
    "https://www.carrefour.es/supermercado/patatas-paja-con-aceite-de-girasol-clasic-carrefour-200-g/R-VC4AECOMM-815583/p",
    "https://www.carrefour.es/supermercado/patatas-fritas-lisas-carrefour-170-g/R-521003684/p",
    "https://www.carrefour.es/supermercado/patatas-fritas-corte-fino-especial-horno-carrefour-classic-600-g/R-677401667/p",
    "https://www.carrefour.es/supermercado/patatas-fritas-especial-horno-carrefour-classic-600-g/R-805525733/p",
    "https://www.carrefour.es/supermercado/aceitunas-verdes-manzanilla-sin-hueso-carrefour-400-g/R-VC4AECOMM-488058/p",
    "https://www.carrefour.es/supermercado/aceitunas-verdes-manzanilla-con-hueso-bajo-contenido-en-sal-carrefour-500-g/R-VC4AECOMM-487733/p",
    "https://www.carrefour.es/supermercado/aceitunas-negras-cacerenas-sin-hueso-carrefour-150-g/R-VC4AECOMM-488032/p",
    "https://www.carrefour.es/supermercado/aceitunas-negras-cacerenas-con-hueso-carrefour-200-g/R-VC4AECOMM-487986/p",
    "https://www.carrefour.es/supermercado/palomitas-saladas-para-microondas-carrefour-pack-de-6-unidades-de-100-g/R-530362838/p",
    "https://www.carrefour.es/supermercado/palomitas-sabor-mantequilla-para-microondas-carrefour-pack-de-3-bolsas-de-100-g/R-521003812/p",
    "https://www.carrefour.es/supermercado/palomitas-sabor-mantequilla-carrefour-kids-sin-gluten-80-g/R-804031851/p",
    "https://www.carrefour.es/supermercado/galletas-saladas-carrefour-350-g/R-521003836/p",
    "Vacio",
    "https://www.carrefour.es/supermercado/arroz-redondo-integral-carrefour-1-kg/R-VC4AECOMM-689578/p",
    "https://www.carrefour.es/supermercado/arroz-largo-categoria-1-carrefour-classc-1-kg/R-538408171/p",
    "https://www.carrefour.es/supermercado/arroz-basmati-sensation-carrefour-1-kg/R-VC4AECOMM-724474/p",
    "https://www.carrefour.es/supermercado/arroz-largo-vaporizado-carrefour-1-kg/R-521005536/p",
    "https://www.carrefour.es/supermercado/macarrones-carrefour-500-g/R-544101816/p",
    "https://www.carrefour.es/supermercado/tiburon-carrefour-500-g/R-544101810/p",
    "https://www.carrefour.es/supermercado/fideua-carrefour-500-g/R-544101804/p",
    "https://www.carrefour.es/supermercado/espirales-carrefour-500-g/R-544101822/p",
    "https://www.carrefour.es/supermercado/plumas-rayadas-gallo-450-g/R-VC4AECOMM-636279/p",
    "https://www.carrefour.es/supermercado/farfalle-de-tomate-y-albahaca-dalla-costa-500-g/R-804987849/p",
    "https://www.carrefour.es/supermercado/espirales-vegetales-carrefour-500-g/R-521005645/p",
    "https://www.carrefour.es/supermercado/espaguetis-carrefour-500-g/R-544101814/pe",
    "https://www.carrefour.es/supermercado/tallarines-carrefour-500-g/R-544101808/p",
    "https://www.carrefour.es/supermercado/azucar-blanco-carrefour-1-kg/R-VC4AECOMM-463155/p",
    "https://www.carrefour.es/supermercado/azucar-moreno-de-cana-in-integral-classic-carrefour-1-kg/R-VC4AECOMM-181710/p",
    "https://www.carrefour.es/supermercado/cafe-molido-mezcla-carrefour-500-g/R-fprod1280759/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "Vacio",
    "https://www.carrefour.es/supermercado/cafe-molido-natural-intenso-carrefour-250-g/R-VC4AECOMM-598247/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/cafe-molido-natural-descafeinado-carrefour-250-g/R-521003002/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/cafe-molido-mezcla-express-descafeinado-carrefour-250-g/R-521002978/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/cafe-soluble-natural-carrefour-200-g/R-521003045/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/cafe-soluble-descafeinado-carrefour-200-g/R-521003069/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/galleta-maria-carrefour-800-g/R-VC4AECOMM-602603/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/galletas-maria-dorada-carrefour-classic-800-g/R-fprod1220431/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=nse",
    "https://www.carrefour.es/supermercado/galletas-integrales-maria-classic-carrefour-800-g/R-812936349/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/galletas-tostadas-carrefour-classic-800-g/R-716511010/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/galletas-digestive-carrefour-sensation-800-g/R-596701895/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/galletas-integrales-de-avena-digestive-carrefour-425-g/R-641302286/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/cookies-con-pepitas-de-chocolate-carrefour-225-g/R-VC4AECOMM-506479/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/galletas-de-cacao-rellenas-de-crema-blackroll-carrefour-220-g/R-840300661/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/galletas-rellenas-de-crema-con-chocolate-blanco-carrefour-classic-252-g/R-839100325/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/galletas-rellenas-de-crema-de-chocolate-mega-carrefour-classic-500-g/R-prod224299/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/conos-con-helado-de-nata-y-fresa-con-salsa-de-fresa-carrefour-4-ud/R-prod301649/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/conos-con-helado-de-vainilla-carrefour-extra-6-ud/R-VC4AECOMM-485162/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.carrefour.es/supermercado/mini-bombon-helado-de-avellana-sensation-carrefour-4-ud/R-VC4AECOMM-728660/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/bombon-helado-de-chocolate-blanco-simpl-6-ud/R-VC4AECOMM-352543/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "Vacio",
    "https://www.carrefour.es/supermercado/bombon-helado-chocolate-con-leche-6-ud/R-590502786/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/bombon-helado-sabor-vainilla-con-chocolate-con-leche-y-almendras-carrefour-6-ud/R-VC4AECOMM-404035/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/helado-de-vainilla-1-l/R-538003230/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/helado-de-stracciatella-carte-dor-500-g/R-521033797/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.carrefour.es/supermercado/helado-de-chocolate-con-virutas-extra-carrefour-sin-gluten-470-g/R-VC4AECOMM-726699/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "Vacio",
    "https://www.carrefour.es/supermercado/helado-sorbete-de-limon-carrefour-580-g/R-521031876/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "Vacio",
    "https://www.carrefour.es/supermercado/cereales-rellenos-de-cacao-y-avellanas-carrefour-sin-gluten-400-g/R-VC4AECOMM-507244/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/copos-de-avena-ecologicos-carrefour-bio-doy-pack-500-gr/R-VC4AECOMM-094436/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "Vacio",
    "https://www.carrefour.es/supermercado/trigo-inflado-integral-con-miel-esgir-375-g/R-VC4AECOMM-057421/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/cereales-de-arroz-inflado-choco-rice-carrefour-classic-500-g/R-VC4AECOMM-598241/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/copos-de-arroz-y-trigo-integral-stylesse-carrefour-500-g/R-728110806/p",
    "https://www.carrefour.es/supermercado/copos-de-cereales-chocolateados-carrefour-kids-500-g/R-521003282/p",
    "Vacio",
    "https://www.carrefour.es/supermercado/cereales-de-maiz-corn-flakes-500-g/R-551801837/p",
    "https://www.carrefour.es/supermercado/muesli-crujiente-sin-azucar-anadido-carrefour-sensation-500-g/R-VC4AECOMM-108107/p",
    "https://www.carrefour.es/supermercado/cereales-con-frutas-desecadas-muesli-carrefour-750-g/R-521003315/p",
    "https://www.carrefour.es/supermercado/cereales-con-frutas-y-frutos-secos-muesli-carrefour-750-g/R-521003323/pe",
    "https://www.carrefour.es/supermercado/cereales-crujientes-con-chocolate-muesli-carrefour-750-g/R-529043295/p",
    "https://www.carrefour.es/supermercado/galletas-de-barquillo-rellenas-sabor-nata-carrefour-210-g/R-VC4AECOMM-513757/p",
    "https://www.carrefour.es/supermercado/galletas-de-barquillo-rellena-sabor-chocolate-carrefour-210-g/R-VC4AECOMM-513772/p",
    "https://www.carrefour.es/supermercado/atun-claro-al-natural-carrefour-pack-de-6-latas-de-56-g/R-prod620143/p",
    "https://www.carrefour.es/supermercado/atun-claro-en-aceite-de-oliva-classic-carrefour-pack-de-3-latas-de-52-g/R-521006173/p",
    "https://www.carrefour.es/supermercado/atun-claro-en-aceite-de-girasol-carrefour-pack-de-6-latas-de-52-g/R-521029268/p",
    "https://www.carrefour.es/supermercado/atun-claro-en-escabeche-carrefour-pack-de-6-latas-de-52-g/R-prod820097/p",
    "https://www.carrefour.es/supermercado/bonito-del-norte-en-aceite-de-oliva-carrefour-pack-de-3-latas-de-52-g/R-prod630003/p",
    "https://www.carrefour.es/supermercado/bonito-del-norte-en-escabeche-carrefour-72-g/R-521006232/p",
    "https://www.carrefour.es/supermercado/mejillones-en-escabeche-tamano-pequeno-simpl-69-g/R-VC4AECOMM-147359/p",
    "https://www.carrefour.es/supermercado/mejillones-en-escabeche-picantes-cuca-sin-gluten-y-sin-lactosa-69-g/R-521006412/p",
    "https://www.carrefour.es/supermercado/mejillones-en-salsa-vieira-13-18-isabel-sin-gluten-y-sin-lactosa-69-g/R-526517339/p",
    "https://www.carrefour.es/supermercado/mejillon-al-natural-13-18-classic-carrefour-69-g/R-678001966/p",
    "https://www.carrefour.es/supermercado/sardinas-con-tomate-isabel-115-g/R-521006314/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/sardinas-en-aceite-de-oliva-procedente-de-pesca-sostenible-carrefour-pack-de-2-unidades-de-84-g/R-prod590530/p",
    "https://www.carrefour.es/supermercado/sardinas-al-limon-cuca-85-g/R-fprod1350161/p",
    "https://www.carrefour.es/supermercado/sardinas-en-escabeche-isabel-115-g/R-522713685/p",
    "https://www.carrefour.es/supermercado/sardinas-picantes-cuca-120-g/R-521006347/p",
    "https://www.carrefour.es/supermercado/tomate-triturado-contenido-bajo-de-sal-carrefour-390-g/R-666701683/p",
    "https://www.carrefour.es/supermercado/tomate-triturado-carrefour-780-g/R-791942743/pe",
    "https://www.carrefour.es/supermercado/tomate-frito-sin-azucares-anadidos-contenido-reducido-en-sal-carrefour-tarro-550-g/R-prod730714/p",
    "https://www.carrefour.es/supermercado/tomate-frito-carrefour-pack-de-3-briks-de-390-g/R-767407262/p",
    "Vacio",
    "https://www.carrefour.es/supermercado/tomate-frito-con-aceite-de-oliva-carrefour-tarro-350-g/R-600805297/p",
    "https://www.carrefour.es/supermercado/judias-verdes-planas-cortadas-carrefour-360-g/R-521005920/p",
    "https://www.carrefour.es/supermercado/judias-verde-redondas-ybarra-360-g/R-prod301058/p",
    "https://www.carrefour.es/supermercado/judias-verdes-planas-carrefour-classic-1-kg/R-521031543/p",
    "https://www.carrefour.es/supermercado/judias-verdes-ecologicas-carrefour-bio-600-g/R-VC4AECOMM-472744/p",
    "https://www.carrefour.es/supermercado/pimientos-del-piquillo-enteros-bajo-contenido-en-sal-carrefour-225-g/R-825606407/p",
    "https://www.carrefour.es/supermercado/pimiento-morron-asado-entero-carrefour-220-g/R-604101631/p",
    "Vacio",
    "Vacio",
    "https://www.carrefour.es/supermercado/esparragos-blancos-gruesos-bajo-contenido-en-sal-carrefour-205-g/R-prod720108/p",
    "https://www.carrefour.es/supermercado/esparragos-verdes-classic-carrefour-190-g/R-871005020/p",
    "Vacio",
    "https://www.carrefour.es/supermercado/maiz-dulce-en-grano-carrefour-400-g/R-521031571/p",
    "https://www.carrefour.es/supermercado/guisantes-extra-finos-ecologico-carrefour-bio-230-g/R-522714192/p",
    "https://www.carrefour.es/supermercado/guisantes-finos-findus-1-kg/R-712515237/p",
    "https://www.carrefour.es/supermercado/guisantes-muy-finos-classic-carrefour-250-g/R-758904356/p",
    "Vacio",
    "Vacio",
    "Vacio",
    "https://www.carrefour.es/supermercado/champinones-enteros-classic-carrefour-230-g/R-521005932/p",
    "https://www.carrefour.es/supermercado/champinones-laminados-carrefour-230-g/R-521005928/p",
    "https://www.carrefour.es/supermercado/alcachofa-cortada-carrefour-classic-400-g/R-530014605/p",
    "https://www.carrefour.es/supermercado/alcachofas-baby-carrefour-classic-300-g/R-589702174/p",
    "https://www.carrefour.es/supermercado/corazones-de-alcachofa-8-10-carrefour-240-g/R-521016439/p",
    "https://www.carrefour.es/supermercado/corazones-de-alcachofas-de-tudela-extra-carrefour-250-g/R-VC4AECOMM-094692/p",
    "https://www.carrefour.es/supermercado/harina-de-trigo-classic-carrefour-1-kg/R-VC4AECOMM-253575/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/harina-de-trigo-integral-gallo-nature-1-kg/R-728807127/p?ic_source=portal-y-corporativo&ic_medium=search-empathy&ic_content=ns",
    "https://www.carrefour.es/supermercado/harina-especial-amasar-pizza-original-carreofur-1-kg/R-VC4AECOMM-034885/p",
    "https://www.carrefour.es/supermercado/harina-de-trigo-reposteria-gallo-1-kg/R-521005407/p",
    "https://www.carrefour.es/supermercado/harina-especial-para-fritos-y-rebozados-original-carrefour-1-kg/R-VC4AECOMM-034771/p",
    "https://www.carrefour.es/supermercado/harina-especial-para-bizcochos-gallo-1-kg/R-785714946/p",
    "https://www.carrefour.es/supermercado/harina-de-maiz-fina-sin-gluten-carrefour-400-g/R-fprod1480207/p",
    "https://www.carrefour.es/supermercado/levadura-fresca-levanova-sin-gluten-pack-de-2-sobres-de-25-g/R-805763827/p",
    "https://www.carrefour.es/supermercado/mermelada-de-fresa-categoria-extra-carrefour-410-g/R-521003422/p",
    "https://www.carrefour.es/supermercado/mermelada-de-melocoton-categoria-extra-carrefour-410-g/R-521003428/p",
    "https://www.carrefour.es/supermercado/mermelada-de-naranja-amarga-carrefour-410-g/R-521003430/p",
    "https://www.carrefour.es/supermercado/miel-de-flores-carrefour-1-kg/R-521029106/p",
    "Vacio",
    "https://www.carrefour.es/supermercado/barra-de-pan-pistola-carrefour-250-g/R-527063193/p",
    "https://www.carrefour.es/supermercado/pan-de-molde-con-corteza-carrefour-820-g/R-VC4AECOMM-443145/p",
    "https://www.carrefour.es/supermercado/pan-de-molde-integral-sin-azucar-anadido-carrefour-460-g/R-VC4AECOMM-470192/p",
    "https://www.carrefour.es/supermercado/pan-de-molde-sin-corteza-carrefour-450-g/R-VC4AECOMM-443179/p",
    "https://www.carrefour.es/supermercado/pan-de-molde-integral-sin-corteza-carrefour-450-g/R-VC4AECOMM-436738/p",
    "https://www.carrefour.es/supermercado/pan-de-burger-maxi-classic-carrefour-4-ud/R-521007180/p",
    "https://www.carrefour.es/supermercado/pan-de-perrito-6-ud-330-g/R-606509119/p",
    "Vacio",
    "https://www.carrefour.es/supermercado/tortilla-de-patatas-con-cebolla-carrefour-classic-sin-gluten-sin-lactosa-600-g/R-fprod1300006/p",
    "https://www.carrefour.es/supermercado/pizza-barbacoa-carrefour-400-g/R-521030200/p",
    "https://www.carrefour.es/supermercado/pizza-4-quesos-carrefour-400-g/R-521030213/p",
    "Vacio",
    "https://www.carrefour.es/supermercado/pizza-de-pollo-y-bacon-casa-tarradellas-410-g/R-prod820301/p",
    "https://www.carrefour.es/supermercado/garbanzos-cocidos-categoria-extra-carrefour-400-g/R-521005495/p",
    "https://www.carrefour.es/supermercado/garbanzo-categoria-extra-carrefour-1-kg/R-536500289/p",
    "https://www.carrefour.es/supermercado/alubias-blancas-cocidas-simpl-400-g/R-VC4AECOMM-203416/p",
    "https://www.carrefour.es/supermercado/alubia-blanca-categoria-extra-carrefour-1-kg/R-740822685/p",
    "https://www.carrefour.es/supermercado/alubia-pinta-cocida-carrefour-400-g/R-VC4AECOMM-551493/p",
    "https://www.carrefour.es/supermercado/alubia-pinta-categoria-extra-carrefour-1-kg/R-636701845/p",
    "https://www.carrefour.es/supermercado/lentejas-cocidas-categoria-extra-carrefour-400-g/R-521005501/p",
    "https://www.carrefour.es/supermercado/lenteja-categoria-extra-carrefour-1-kg/R-536500291/p",
    "https://www.carrefour.es/supermercado/ketchup-classic-carrefour-envase-560-g/R-712515965/p",
    "https://www.carrefour.es/supermercado/mostaza-orlando-sin-gluten-envase-290-g/R-520661029/p",
    "https://www.carrefour.es/supermercado/mayonesa-con-aceite-de-girasol-carrefour-tarro-450-ml/R-prod810397/p",
    "https://www.carrefour.es/supermercado/gazpacho-carrefour-sin-gluten-1-l/R-805505583/p",
    "https://www.carrefour.es/supermercado/salmorejo-carrefour-1-l/R-672907587/p",
    "https://www.carrefour.es/supermercado/huevos-frescos-carrefour-el-mercado-12-ud/R-VC4AECOMM-307927/p",
    "Vacio",
    "https://www.carrefour.es/supermercado/huevos-frescos-carrefour-el-mercado-12-ud/R-VC4AECOMM-307925/p",
    "https://www.carrefour.es/supermercado/clara-de-huevo-pasteurizada-carrefour-classic-1-l/R-VC4AECOMM-497495/p"
]
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
            DescripcionXPath = '/html/body/div[2]/div/main/div[1]/div[1]/h1'
            PrecioXPath = '/html/body/div[2]/div/main/div[2]/div[1]/div/div/div[1]/div[1]/span'
            DetalleXPath = '/html/body/div[2]/div/main/div[2]/div[1]/div/div/div[1]/div[1]/div/span'
            imagenSRCXPath = '/html/body/div[2]/div/main/div[1]/div[2]/div/div/div/div/div/div/div/img[2]'
                            

            NombreProductoDFE = driver.find_element("xpath", DescripcionXPath)
            PrecioProductoDFE = driver.find_element("xpath", PrecioXPath)
            DetalleProductoDFE = driver.find_element("xpath", DetalleXPath)
            ImagenDFE = driver.find_element("xpath", imagenSRCXPath)
            
            EnlaceCaido = False
            NombreProducto = unicodedata.normalize('NFKD', NombreProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')            
            PrecioProducto = PrecioProductoDFE.text[:-1]
            PrecioProducto = PrecioProducto.replace(',', '.')
            DetalleProducto = unicodedata.normalize('NFKD', DetalleProductoDFE.text).encode('ascii', 'ignore').decode('utf-8')
            ImagenSRC = ImagenDFE.get_attribute("src")

        except Exception as ex:
            EnlaceCaido= True
            
        finally:
            if EnlaceCaido==False:
                print(i)
                print(productos[i])
                print(seccion+' - '+seccionDetalle+':')
                print(NombreProducto + ' ' +PrecioProducto+' '+DetalleProducto)
                
                '''
                sql = "INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen, enlace) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (seccion, seccionDetalle, productos[i], NombreProducto, Supermercado, ImagenSRC, enlaces[i])
                mycursor.execute(sql, val)
                mydb.commit()
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
                    
            else:
                print('Enlace caido')
mycursor.close()
mydb.close() 
driver.quit()
        