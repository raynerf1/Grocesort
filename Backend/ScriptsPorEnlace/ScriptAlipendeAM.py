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

Supermercado = 'Ahorra Mas'

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

enlaces = ["https://www.ahorramas.com/leche-alipende-1l-entera-70864.html",
    "https://www.ahorramas.com/leche-sin-lactosa-alipende-1l-entera-48681.html",
    "https://www.ahorramas.com/leche-alipende-1l-semidesnatada-70865.html",
    "https://www.ahorramas.com/leche-sin-lactosa-alipende-1l-semidesnatada-85119.html",
    "https://www.ahorramas.com/leche-alipende-1l-desnatada-70866.html",
    "https://www.ahorramas.com/leche-sin-lactosa-alipende-1l-desnatada-85116.html",
    
    "https://www.ahorramas.com/yogur-alipende-pack-16-sabores-surtidos-83735.html",
    "https://www.ahorramas.com/yogur-alipende-pack-8-natural-69437.html",
    "https://www.ahorramas.com/yogur-estilo-griego-alipende-pack-6-natural-750g-84625.html",
    "https://www.ahorramas.com/yogur-estilo-griego-margui-1kg-natural-40484.html",
    "https://www.ahorramas.com/yogur-estilo-griego-alipende-pack-6-azucarado-750g-84626.html",
    
    "https://www.ahorramas.com/mantequilla-alipende-250g-pastilla-49516.html",
    "https://www.ahorramas.com/margarina-alipende-500g-40068.html",
    "https://www.ahorramas.com/bebida-almendra-sin-azucar-anadido-alipende-1-litro-85223.html",
    "https://www.ahorramas.com/bebida-arroz-alipende-1-litro-85224.html",
    "https://www.ahorramas.com/bebida-de-soja-alipende-1l-83536.html",
    "https://www.ahorramas.com/bebida-de-avena-alipende-1l-47223.html",
    "https://www.ahorramas.com/horchata-alipende-1l-75510.html",
    "https://www.ahorramas.com/mousse-alipende-pack-4-chocolate-70631.html",
    "https://www.ahorramas.com/cuajada-alipende-pack-4-125g-natural-81339.html",
    "https://www.ahorramas.com/cuajada-alipende-pack-4-125g-natural-azucarado-81341.html",
    "https://www.ahorramas.com/flan-de-huevo-alipende-pack-6-al-bano-maria-36285.html",
    "https://www.ahorramas.com/flan-de-vainilla-alipende-pack-600g-83066.html",
    "https://www.ahorramas.com/gelatina-gelli-sweet-reina-pack-6-sabores-13371.html",
    "https://www.ahorramas.com/gelatina-gelli-light-reina-pack-4-sabores-15174.html",
    "https://www.ahorramas.com/gelatina-gelli-sweet-reina-pack-6-fresa-12374.html",
    "https://www.ahorramas.com/natillas-sabor-vainilla-alipende-pack-4-83849.html",
    "https://www.ahorramas.com/natillas-de-chocolate-alipende-pack-4-125g-84800.html",
    "https://www.ahorramas.com/batido-alipende-1l-chocolate-69894.html",
    "https://www.ahorramas.com/batido-alipende-200ml-pack-6-cacao-82358.html",
    "https://www.ahorramas.com/batido-alipende-1l-fresa-72216.html",
    "https://www.ahorramas.com/batido-alipende-200ml-pack-6-fresa-82360.html",
    "https://www.ahorramas.com/batido-alipende-1l-vainilla-72217.html",
    "https://www.ahorramas.com/batido-alipende-200ml-pack-6-vainilla-82359.html",
    "https://www.ahorramas.com/zumo-de-naranja-alipende-brik-1l-48007.html",
    "https://www.ahorramas.com/zumo-de-naranja-alipende-pack-6-84636.html",
    "https://www.ahorramas.com/zumo-de-naranja-con-pulpa-100-exprimido-alipende-2l-84850.html",
    "https://www.ahorramas.com/zumo-de-naranja-sin-pulpa-100-exprimido-alipende-2l-84849.html",
    "https://www.ahorramas.com/zumo-de-pina-y-uva-alipende-brik-1l-48008.html",
    "https://www.ahorramas.com/zumo-de-pina-y-uva-alipende-pack-6-84637.html",
    "https://www.ahorramas.com/zumo-de-manzana-don-simon-brik-1l-42447.html",
    "https://www.ahorramas.com/zumo-de-manzana-don-simon-pack-6-45021.html",
    "https://www.ahorramas.com/zumo-de-melocoton-y-uva-alipende-brik-1l-48009.html",
    "https://www.ahorramas.com/nectar-de-melocoton-alipende-pack-6-84642.html",
    "https://www.ahorramas.com/agua-fuente-primavera-15l-39853.html",
    "https://www.ahorramas.com/aceite-de-oliva-alipende-1l-04-84584.html",
    "https://www.ahorramas.com/aceite-de-oliva-alipende-garrafa-5l-04-84585.html",
    "https://www.ahorramas.com/aceite-de-oliva-alipende-1l-1-84579.html",
    "https://www.ahorramas.com/aceite-de-oliva-alipende-garrafa-5l-1-84580.html",
    "https://www.ahorramas.com/aceite-de-girasol-alipende-1l-acidez-maxima-02-84581.html",
    "https://www.ahorramas.com/aceite-de-girasol-alipende-garrafa-5l-acidez-maxima-02-84582.html",
    "https://www.ahorramas.com/vinagre-alipende-1l-vino-blanco-74920.html",
    "https://www.ahorramas.com/vinagre-alipende-1l-manzana-83960.html",
    "https://www.ahorramas.com/vinagre-balsamico-alipende-500ml-modena-74929.html",
    "https://www.ahorramas.com/vinagre-de-jerez-alipende-500ml-74914.html",
    "https://www.ahorramas.com/sal-alipende-1kg-mesa-78990.html",
    "https://www.ahorramas.com/sal-alipende-1kg-gorda-80405.html",
    "https://www.ahorramas.com/sal-rosa-del-himalaya-alipende-1kg-47726.html",
    "https://www.ahorramas.com/bicarbonato-alipende-250g-50988.html",
    "https://www.ahorramas.com/bicarbonato-sodico-roca-1kg-52769.html",
    "https://www.ahorramas.com/patatas-fritas-alipende-200g-artesana-69361.html",
    "https://www.ahorramas.com/patatas-fritas-churreria-alipende-150g-42933.html",
    "https://www.ahorramas.com/patatas-fritas-alipende-100g-paja-44564.html",
    "https://www.ahorramas.com/patatas-fritas-lisas-alipende-300g-82807.html",
    "https://www.ahorramas.com/patatas-fritas-alipende-1kg-corte-fino-79140.html",
    "https://www.ahorramas.com/patatas-fritas-alipende-1kg-tradicional-79141.html",
    "https://www.ahorramas.com/aceitunas-sin-hueso-alipende-400g-71224.html",
    "https://www.ahorramas.com/aceitunas-verdes-con-hueso-alipende-500g-71225.html",
    "https://www.ahorramas.com/aceitunas-negra-sin-hueso-alipende-150g-71232.html",
    "https://www.ahorramas.com/aceitunas-negra-con-hueso-alipende-200g-51389.html",
    "https://www.ahorramas.com/palomitas-sal-microondas-s-gluten-alipende-pack-3-73199.html",
    "https://www.ahorramas.com/palomitas-mantequilla-microondas-s-gluten-alipende-pack-3-84506.html",
    "https://www.ahorramas.com/palomitas-alipende-90g-con-mantequilla-84997.html",
    "https://www.ahorramas.com/galletas-saladas-alipende-350g-33124.html",
    "https://www.ahorramas.com/galletas-saladas-alipende-300g-41330.html",
    "https://www.ahorramas.com/arroz-alipende-1kg-redondo-69384.html",
    "https://www.ahorramas.com/arroz-alipende-1kg-largo-67686.html",
    "https://www.ahorramas.com/arroz-alipende-1kg-basmati-84670.html",
    "https://www.ahorramas.com/arroz-alipende-1kg-vaporizado-67685.html",
    "https://www.ahorramas.com/pluma-alipende-500g-n5-49929.html",
    "https://www.ahorramas.com/tiburon-alipende-500g-49926.html",
    "https://www.ahorramas.com/fideua-alipende-500g-49925.html",
    "https://www.ahorramas.com/espirales-alipende-500g-49932.html",
    "https://www.ahorramas.com/macarron-rayado-alipende-500g-con-vegetales-49962.html",
    "https://www.ahorramas.com/pajaritas-alipende-500g-con-vegetales-49961.html",
    "https://www.ahorramas.com/espirales-alipende-500g-con-vegetales-49960.html",
    "https://www.ahorramas.com/spaghetti-alipende-500g-49928.html",
    "https://www.ahorramas.com/tallarin-alipende-500g-49927.html",
    "https://www.ahorramas.com/azucar-blanco-azucarera-1kg-54770.html",
    "https://www.ahorramas.com/azucar-moreno-de-cana-no-refinado-azucarera-1kg-55690.html",
    "https://www.ahorramas.com/cafe-molido-alipende-250g-mezcla-50-50-48072.html",
    "https://www.ahorramas.com/cafe-molido-descafeinado-alipende-250g-mezcla-50-50-48074.html",
    "https://www.ahorramas.com/cafe-molido-alipende-250g-tueste-natural-48073.html",
    "https://www.ahorramas.com/cafe-molido-descafeinado-alipende-250g-tueste-natural-75975.html",
    "https://www.ahorramas.com/cafe-molido-alipende-250g-espresso-mezcla-80-20-75976.html",
    "https://www.ahorramas.com/cafe-soluble-alipende-200g-46068.html",
    "https://www.ahorramas.com/cafe-soluble-alipende-descafeinado-200g-mezcla-46060.html",
    "https://www.ahorramas.com/galleta-maria-alipende-800g-73360.html",
    "https://www.ahorramas.com/galleta-maria-alipende-800g-dorada-73362.html",
    "https://www.ahorramas.com/galleta-maria-alipende-800g-integral-74676.html",
    "https://www.ahorramas.com/galleta-alipende-800g-tostada-73359.html",
    "https://www.ahorramas.com/galleta-digestive-alipende-800g-78454.html",
    "https://www.ahorramas.com/galleta-digestive-alipende-425g-avena-47729.html",
    "https://www.ahorramas.com/galleta-alipende-225g-cookies-con-pepitas-de-chocolate-42322.html",
    "https://www.ahorramas.com/galleta-sandwich-alipende-176g-76412.html",
    "https://www.ahorramas.com/galleta-sandwich-alipende-252g-chocolate-blanco-74732.html",
    "https://www.ahorramas.com/galletas-rellenas-crema-de-chocolate-alipende-500g-55175.html",
    "https://www.ahorramas.com/helado-cono-alipende-6-uds-nata-y-fresa-41272.html",
    "https://www.ahorramas.com/helado-cono-sin-azucar-alipende-4-uds-vainilla-choco-72908.html",
    "https://www.ahorramas.com/helado-cono-alipende-4-uds-nata-turron-72912.html",
    "https://www.ahorramas.com/helado-cono-alipende-tarta-queso-4-uds-23225.html",
    "https://www.ahorramas.com/helado-cono-alipende-6-uds-nata-y-trufa-41273.html",
    "https://www.ahorramas.com/helado-bombon-alipende-6-uds-crocanti-66937.html",
    "https://www.ahorramas.com/helado-super-bombon-alipende-360ml-3-uds-blanco-66922.html",
    "https://www.ahorramas.com/helado-super-bombon-alipende-270ml-3-uds-tres-chocolates-84656.html",
    "https://www.ahorramas.com/helado-bombon-alipende-6-uds-nata-66936.html",
    "https://www.ahorramas.com/helado-super-bombon-alipende-360-ml-3-uds-66921.html",
    "https://www.ahorramas.com/helado-en-tarrina-alipende-1l-vainilla-75283.html",
    "https://www.ahorramas.com/helado-en-tarrina-alipende-900ml-stracciatella-72905.html",
    "https://www.ahorramas.com/helado-en-tarrina-alipende-900ml-turron-67930.html",
    "https://www.ahorramas.com/helado-en-tarrina-alipende-900ml-nata-y-nuez-67931.html",
    "https://www.ahorramas.com/helado-en-tarrina-alipende-900ml-tres-chocolates-85002.html",
    "https://www.ahorramas.com/helado-en-tarrina-alipende-900ml-chocolate-con-trozos-67933.html",
    "https://www.ahorramas.com/helado-en-tarrina-alipende-900ml-frutas-del-bosque-72906.html",
    "https://www.ahorramas.com/sorbete-de-limon-alipende-1l-67929.html",
    "https://www.ahorramas.com/cereales-alipende-500g-rellenos-de-leche-48336.html",
    "https://www.ahorramas.com/cereales-rellenos-sin-gluten-alipende-500g-cacao-85171.html",
    "https://www.ahorramas.com/copos-de-avena-integrales-alipende-1kg-suaves-74134.html",
    "https://www.ahorramas.com/cereales-alipende-500g-bolas-con-cacao-29650.html",
    "https://www.ahorramas.com/cereales-crujientes-alipende-500g-trigo-con-miel-37948.html",
    "https://www.ahorramas.com/cereales-de-arroz-inflado-cacao-s-gluten-alipende-500g-48335.html",
    "https://www.ahorramas.com/cereales-integrales-alipende-500g-en-copos-55365.html",
    "https://www.ahorramas.com/cereales-alipende-500g-copos-de-cacao-76864.html",
    "https://www.ahorramas.com/cereales-integrales-alipende-500g-copos-con-frutos-rojos-55254.html",
    "https://www.ahorramas.com/corn-flakes-sin-gluten-alipende-400g-55319.html",
    "https://www.ahorramas.com/muesli-crujiente-alipende-1kg-55324.html",
    "https://www.ahorramas.com/muesli-crujiente-alipende-500g-con-frutas-55321.html",
    "https://www.ahorramas.com/muesli-crujiente-alipende-500g-con-frutos-secos-55323.html",
    "https://www.ahorramas.com/muesli-crujiente-alipende-500g-con-chocolate-negro-55322.html",
    "https://www.ahorramas.com/barquillo-alipende-150g-relleno-de-crema-de-nata-74734.html",
    "https://www.ahorramas.com/barquillo-alipende-150g-relleno-de-crema-de-chocolate-74735.html",
    "https://www.ahorramas.com/atun-claro-alipende-pack-3-al-natural-83662.html",
    "https://www.ahorramas.com/atun-alipende-pack-3-en-aceite-oliva-83610.html",
    "https://www.ahorramas.com/atun-claro-alipende-pack-3-en-aceite-girasol-83613.html",
    "https://www.ahorramas.com/atun-claro-alipende-pack-3-en-escabeche-83653.html",
    "https://www.ahorramas.com/bonito-alipende-190g-en-aceite-oliva-75843.html",
    "https://www.ahorramas.com/bonito-alipende-190g-en-escabeche-75841.html",
    "https://www.ahorramas.com/mejillon-alipende-69g-13-18-escabeche-83600.html",
    "https://www.ahorramas.com/mejillon-alipende-69g-13-18-escabeche-picante-83603.html",
    "https://www.ahorramas.com/mejillon-alipende-65g-13-18-salsa-vieira-83604.html",
    "https://www.ahorramas.com/mejillon-alipende-69g-13-18-natural-83602.html",
    "https://www.ahorramas.com/sardina-alipende-pack-2-78g-en-tomate-41352.html",
    "https://www.ahorramas.com/sardina-alipende-pack-2-84g-en-aceite-oliva-41347.html",
    "https://www.ahorramas.com/sardina-alipende-pack-2-84g-al-limon-41350.html",
    "https://www.ahorramas.com/sardina-alipende-pack-2-84g-en-escabeche-41349.html",
    "https://www.ahorramas.com/sardina-alipende-pack-2-84g-picantonas-41351.html",
    "https://www.ahorramas.com/tomate-triturado-sin-gluten-ecologico-alipende-400g-49365.html",
    "https://www.ahorramas.com/tomate-natural-triturado-apis-800g15-38030.html",
    "https://www.ahorramas.com/tomate-frito-origen-nacional-sin-gluten-alipende-550g-69293.html",
    "https://www.ahorramas.com/tomate-frito-origen-nacional-sin-gluten-alipende-p3-400g-54138.html",
    "https://www.ahorramas.com/tomate-frito-como-en-sarten-sin-gluten-alipende-560g-48479.html",
    "https://www.ahorramas.com/tomate-frito-casero-en-aceite-oliva-alipende-350g-48076.html",
    "https://www.ahorramas.com/judias-verdes-anchas-sin-gluten-alipende-360g-69283.html",
    "https://www.ahorramas.com/judia-verde-redonda-sin-gluten-alipende-360g-48332.html",
    "https://www.ahorramas.com/judias-verdes-alipende-1kg-planas-84485.html",
    "https://www.ahorramas.com/judias-verdes-alipende-1kg-redondas-84344.html",
    "https://www.ahorramas.com/pimientos-de-piquillo-enteros-sin-gluten-alipende-260g-29898.html",
    "https://www.ahorramas.com/pimiento-morron-alipende-pack-3-entero-84680.html",
    "https://www.ahorramas.com/pimientos-de-piquillo-en-tiras-sin-gluten-alipende-225g-82730.html",
    "https://www.ahorramas.com/pimientos-de-piquillo-enteros-sin-gluten-alipende-150g-82732.html",
    "https://www.ahorramas.com/esparragos-blancos-grueso-alipende-205g-9-12-piezas-82741.html",
    "https://www.ahorramas.com/esparragos-verdes-calibre-delgado-alipende-100g-82750.html",
    "https://www.ahorramas.com/maiz-dulce-alipende-pack-6-55721.html",
    "https://www.ahorramas.com/maiz-alipende-300g-superdulce-78998.html",
    "https://www.ahorramas.com/guisantes-alipende-1kg-finos-84489.html",
    "https://www.ahorramas.com/guisantes-ecologicos-alipende-500g-finos-23817.html",
    "https://www.ahorramas.com/guisantes-muy-finos-alipende-250g-81586.html",
    "https://www.ahorramas.com/guisantes-alipende-300g-extrafinos-51515.html",
    "https://www.ahorramas.com/guisantes-extra-finos-categoria-primera-alipende-230g-71249.html",
    "https://www.ahorramas.com/guisante-mediano-alipende-p3-200g-33258.html",
    "https://www.ahorramas.com/champinon-alipende-bote-185g-entero-52239.html",
    "https://www.ahorramas.com/champinon-alipende-bote-185g-laminado-52238.html",
    "https://www.ahorramas.com/alcachofas-alipende-500g-81898.html",
    "https://www.ahorramas.com/alcachofas-baby-alipende-300g-84764.html",
    "https://www.ahorramas.com/corazon-de-alcachofa-alipende-8-10-240g-59404.html",
    "https://www.ahorramas.com/alcachofa-alipende-8-11-165g-61506.html",
    "https://www.ahorramas.com/harina-de-trigo-alipende-1kg-68517.html",
    "https://www.ahorramas.com/harina-de-trigo-integral-alipende-1kg-73758.html",
    "https://www.ahorramas.com/harina-alipende-1kg-especial-pizza-84821.html",
    "https://www.ahorramas.com/harina-de-trigo-alipende-1kg-reposteria-73759.html",
    "https://www.ahorramas.com/harina-de-trigo-alipende-1kg-especial-fritos-68515.html",
    "https://www.ahorramas.com/harina-de-trigo-especial-bizcocho-levadura-alipende-1kg-84819.html",
    "https://www.ahorramas.com/harina-de-maiz-sin-gluten-alipende-400g-fina-63918.html",
    "https://www.ahorramas.com/levadura-fresca-levanova-50g-77084.html",
    "https://www.ahorramas.com/mermelada-extra-alipende-410g-fresa-50576.html",
    "https://www.ahorramas.com/mermelada-extra-alipende-410g-melocoton-50578.html",
    "https://www.ahorramas.com/mermelada-extra-alipende-410g-naranja-amarga-50575.html",
    "https://www.ahorramas.com/miel-de-flores-alipende-1kg-54753.html",
    "https://www.ahorramas.com/miel-de-azahar-de-origen-nacional-alipende-350g-70117.html",
    "https://www.ahorramas.com/barra-horno-super-250g-60527.html",
    "https://www.ahorramas.com/pan-de-molde-alipende-820g-blanco-84494.html",
    "https://www.ahorramas.com/pan-de-molde-integral-alipende-460g-50416.html",
    "https://www.ahorramas.com/pan-de-molde-sin-corteza-alipende-450g-73387.html",
    "https://www.ahorramas.com/pan-de-molde-integral-sin-corteza-alipende-450g-50417.html",
    "https://www.ahorramas.com/pan-de-hamburguesa-big-burgers-alipende-300g-84496.html",
    "https://www.ahorramas.com/pan-hot-dogs-alipende-330g-84497.html",
    "https://www.ahorramas.com/tortilla-de-patata-sin-gluten-alipende-600g-sin-cebolla-77070.html",
    "https://www.ahorramas.com/tortilla-de-patata-sin-gluten-alipende-600g-con-cebolla-77069.html",
    "https://www.ahorramas.com/pizza-alipende-400g-barbacoa-85198.html",
    "https://www.ahorramas.com/pizza-alipende-400g-cuatro-quesos-85195.html",
    "https://www.ahorramas.com/pizza-alipende-400g-jamon-y-queso-85196.html",
    "https://www.ahorramas.com/pizza-alipende-400g-pollo-y-bacon-85200.html",
    "https://www.ahorramas.com/garbanzo-cocido-alipende-400g-60125.html",
    "https://www.ahorramas.com/garbanzo-alipende-1kg-77269.html",
    "https://www.ahorramas.com/alubia-blanca-cocida-alipende-400g-60127.html",
    "https://www.ahorramas.com/alubia-alipende-1kg-blanca-77265.html",
    "https://www.ahorramas.com/alubia-pinta-cocida-alipende-400g-60128.html",
    "https://www.ahorramas.com/alubia-alipende-1kg-pinta-77266.html",
    "https://www.ahorramas.com/lenteja-cocida-alipende-400g-60129.html",
    "https://www.ahorramas.com/lenteja-alipende-1kg-castellana-77273.html",
    "https://www.ahorramas.com/ketchup-sin-gluten-alipende-500ml-85019.html",
    "https://www.ahorramas.com/mostaza-alipende-300ml-84974.html",
    "https://www.ahorramas.com/mayonesa-sin-gluten-alipende-450ml-84985.html",
    "https://www.ahorramas.com/gazpacho-garcia-millan-1l-46064.html",
    "https://www.ahorramas.com/salmorejo-alipende-1l-52018.html",
    "https://www.ahorramas.com/huevos-gallinas-criadas-suelo-alipende-12u-clase-l-34649.html",
    "https://www.ahorramas.com/huevos-gallinas-criadas-suelo-alipende-12u-clase-m-31204.html",
    "https://www.ahorramas.com/huevos-gallinas-criadas-suelo-alipende-12u-clase-l-xl-37066.html",
    "https://www.ahorramas.com/30-claras-de-huevo-ovonovo-1l-3751.html"
]
seccion = ''
seccionDetalle = ''
id_producto = ''
driver = webdriver.Firefox()
for i in range(229):

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
        
    finally:
        '''
        sql = "INSERT INTO productos (seccion, subseccion, producto, descripcion, supermercado, imagen) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (seccion, seccionDetalle, productos[i], NombreProducto, Supermercado, ImagenSRC)
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
        print(i)
        print(productos[i])
        print(seccion+' - '+seccionDetalle+':')
        print(NombreProducto + ' ' +PrecioProducto+' '+DetalleProducto)

mycursor.close()
mydb.close()      
driver.quit()
        