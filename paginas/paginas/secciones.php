<!DOCTYPE html>
<!--Index-->

<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Grocesort by Rayner</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
        <meta name="description" content="Grocesort, aplicación web para comparar los precios de los productos en varios supermercados de España">
    <meta property="og:title" content="Grocesort">
    <meta property="og:description" content="Grocesort, aplicación web para comparar los precios de los productos en varios supermercados de España">
    <meta property="og:image" content="https://cdn.discordapp.com/attachments/1166363443637518346/1181710546878337146/GS_Logo.png?ex=65820cb5&is=656f97b5&hm=ed861c8c0bc3f030314a66d50da7e1cd14a9f4f97917927f63252dc64379481f&">
    <meta property="og:image:alt" content="Logo de Grocesort">
    <link rel="stylesheet" href="../assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="../assets/css/styles.min.css">
    <link rel="stylesheet" href="../assets/css/preloader.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.5/gsap.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <style>
        .hidden {
            display: none;
        }
        #div1 {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        #div2 {
            display: none;
        }
        #footer{
          display: none;
        }
    </style>
<link rel="icon" href="https://cdn.discordapp.com/attachments/1166363443637518346/1181710546878337146/GS_Logo.png?ex=65820cb5&is=656f97b5&hm=ed861c8c0bc3f030314a66d50da7e1cd14a9f4f97917927f63252dc64379481f&">
</head>
<body>

<header>
<nav class="navbar navbar-expand-lg bg-light fixed-top">
  <div class="container-fluid">
  <img src="https://cdn.discordapp.com/attachments/1166363443637518346/1181710546878337146/GS_Logo.png?ex=65820cb5&is=656f97b5&hm=ed861c8c0bc3f030314a66d50da7e1cd14a9f4f97917927f63252dc64379481f&" alt="Grocesort logo" class="img-fluid" style="max-height: 30px;">
    <a class="navbar-brand">Grocesort</a>
     
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-link" aria-current="page" href="../../index.html">Inicio</a>
        <a class="nav-link" href="sobremi/index.html">Sobre mí</a>
        <a class="nav-link" href="privacidad.html">Privacidad</a>
        <!--Theme mode switcher-->
        <!--
        <a class="nav-link" id="cambiarEstilos" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Cambiar modo de color de la página" style="cursor: pointer; <?php if ($_COOKIE["FormularioCookies"] === 'No'){echo 'display: none';}  ?>" >
    <span id="modoTexto">Claro</span>
    <svg xmlns="http://www.w3.org/2000/svg"  width="16" height="16" fill="currentColor" class="bi bi-brightness-high-fill" viewBox="0 0 16 16" id="modoIcono">
        <path d="M12 8a4 4 0 1 1-8 0 4 4 0 0 1 8 0M8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0m0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13m8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5M3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8m10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0m-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707M4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z"></path>
    </svg>
</a>-->


      </div>

                <?php 
                $carro = isset($_COOKIE["carro"]) ? json_decode($_COOKIE["carro"], true) : [];
                $cantidadElementos = count($carro);?>
                <a class="nav-link" href="carro.php">
                    <button type="button" class="btn btn-primary ml-5" <?php if ($_COOKIE["FormularioCookies"] === 'No'){echo 'style="display: none"';}  ?>>
                        Lista<span class="badge text-bg-secondary"><?php echo $cantidadElementos;?></span>
                    </button>
                </a>
                

                
              </div>
  </div>
</nav>
<nav class="navbar navbar-expand-lg bg-secondary mt-5 fixed-top">
  <div class="container">
  <div class="container-fluid">
    <div class="d-flex" role="search">
      <input id="buscar" class="form-control me-2" type="text" placeholder="Buscar" aria-label="Search" style="width: 50%;">
      <button id ="btnInvertir" class="btn btn-primary" onclick="invertirOrden()">A-Z <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M11.5 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L11 2.707V14.5a.5.5 0 0 0 .5.5zm-7-14a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L4 13.293V1.5a.5.5 0 0 1 .5-.5z"/>

</svg></button>
    </div>
  </div>


  </div>
</nav>
</header>



</div>
    </div>

    <div id="div1" class="CentrarTest1 bg-white">
        <div class="spinner-border text-warning" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    </div>
<nav class="mt-1">
<br>
</nav>
      <div id="div2" class="bg-white">


<nav class="mt-5">
</nav>
<nav class="mt-5">
</nav>


        <?php
        if (isset($_COOKIE["FormularioCookies"])) {
            $valorCookie = $_COOKIE["FormularioCookies"];
        } else {
            $nombreCookie = "FormularioCookies";
            $valorCookie = "";
            $tiempoExpiracion = time() + 3600*2400; // 2,400 horas desde el momento actual

            setcookie($nombreCookie, $valorCookie, $tiempoExpiracion, "/");
            ?>
                        <!-- Modal -->
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Aviso de cookies</h1>
                    <!--<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>-->
                </div>
                <div class="modal-body">
                    Este sitio web utiliza cookies para fines estrictamente funcionales, permitiendo añadir productos a tu lista de la compra y optimizando el funcionamiento de la página. 
                    Pulsa el botón "Aceptar" para confirmar que has leído y aceptado la información presentada, rechazar las cookies implicará tener disponibles menos funcionalidades.
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" onclick="rechazarCookies()">Rechazar cookies</button>
                    <button type="button" id="btnAceptarCookies" class="btn btn-primary" data-bs-dismiss="modal" onclick="aceptarCookies()">Aceptar</button>
                </div>
                </div>
            </div>
            </div>
            <script>
            // Lógica para mostrar el modal al cargar la página
            document.addEventListener('DOMContentLoaded', function() {
            var myModal = new bootstrap.Modal(document.getElementById('exampleModal'));
            myModal.show();
            });
            function aceptarCookies() {
                document.cookie = "FormularioCookies=Si; expires=<?php echo date('D, d M Y H:i:s', $tiempoExpiracion) . ' GMT'; ?>; path=/";                
            }

            function rechazarCookies() {
                document.cookie = 'carro' + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/paginas/paginas';
                document.cookie = 'TemaModo' + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
                document.cookie = "FormularioCookies=No; expires=<?php echo date('D, d M Y H:i:s', $tiempoExpiracion) . ' GMT'; ?>; path=/";
                    var enlaceCarro = document.querySelector('.nav-link[href="carro.php"]');
                    var TemaModobtn = document.querySelector('#cambiarEstilos');
                if (enlaceCarro) {
                    enlaceCarro.remove();
                    TemaModobtn.remove();
                }
            }
            </script>
            <?php
        }
        ?>


  <?php
  $carro = isset($_COOKIE["carro"]) ? json_decode($_COOKIE["carro"], true) : [];
  $cantidadElementos = count($carro);
  
  require_once('../../config.php');#Cambiar en InfinityFree
  $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=' . DB_CHARSET, DB_USER, DB_PASSWORD);
 
  $sql = 'SELECT nombre, nombreutf, imagen FROM secciones order by nombre asc';
  
  $resultado = $pdo->prepare($sql);
  $resultado->execute();
  ?>
      <section class="py-4 py-xl-5">
        <div class="container-fluid">

        <?php
  if ($resultado->rowCount() != 0) {
?>
<div class="row row-cols-2 row-cols-sm-2 row-cols-md-2 row-cols-lg-4 row-cols-xl-4 row-cols-xxl-4 justify-content-center" id="row-1">
<?php
    while ($fila = $resultado->fetch(PDO::FETCH_ASSOC)) {
  ?>
  <div class="col justify-content-center d-flex align-items-center" id=" test <?php echo str_replace(' ', '', strtolower(trim($fila["nombre"]))); ?>">
  <form method="POST" action="vistaSecciones.php">
    <input type="hidden" name="nombre_equipo" value="<?php echo $fila["nombre"]; ?>">
    <input type="hidden" name="foto_slider" value="test<?php echo $fila["nombre"]; ?>">
    <input type="hidden" name="foto_logo" value="test<?php echo $fila["nombre"]; ?>">
    <a class="justify-content-center d-flex align-items-center columna" href="#" onclick="event.preventDefault(); this.closest('form').submit();">
      <div class="card bg-white textoOscuro" style="border-style: none;">
        <div class="card-body">
          <h1 class="text-start"><?php echo ($fila["nombreutf"] !== null) ? $fila["nombreutf"] : $fila["nombre"]; ?></h1>

          <img class="img-fluid order-4 coche" src="<?php echo $fila["imagen"]; ?>" width="700px" alt="Imagen de <?php echo ($fila["nombreutf"] !== null) ? $fila["nombreutf"] : $fila["nombre"]; ?>">
                                              
        </div>
      </div>
      <img class="logo" src=<?php echo '../imagenes/secciones/iconos/' . str_replace(' ', '', strtolower(trim($fila["nombre"]))) . '.png' ?> width="7%" style="position: absolute;">
    </a>
  </form>
</div>

<?php
    }
  ?>
    </div>

  <?php
  }
  $pdo=null;


?>

        </div>
    </section>
    <script src="../assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="../assets/js/script.min.js"></script>

  <script>
    gsap.from('section', {opacity: 0, duration: 4, y:50})
    gsap.from('.text-start', {opacity: 0, duration: 5, y:-70})
</script>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    $(document).ready(function() {
        aplicarEstilos();

        setTimeout(function() {
            $('#div1').hide();
            $('#div2').show();
            $('#footer').show();
        }, 1000);

        $(document).on("keyup", "#buscar", function() {
            var input = $(this).val();
            var btnInvertir = $("#btnInvertir");
            btnInvertir.hide();

            if (input !== "") {
                $.ajax({
                    url: "busqueda.php",
                    method: "POST",
                    data: { input: input },
                    success: function(data) {
                        $("#resultadoBusqueda").html(data);
                        $("#resultadoBusqueda").css("display", "block");
                        $('#div2').hide();
                    }
                });
            } else {
                $('#div2').show();
                $("#resultadoBusqueda").css("display", "none");
                btnInvertir.show();
            }
        });

        $(window).scroll(function() {
            var nav = $("#headerNavbar");
            if ($(window).scrollTop() <= 40) {
                nav.removeClass("bg-light");
            } else {
                nav.addClass("bg-light");
            }
        });
    });

function getCookie(nombre) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${nombre}=`);
    
    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
    
    return null;
}

// Obtén el valor de la cookie
var modo = getCookie('TemaModo');
var FCookies = getCookie('FormularioCookies');

// Si la cookie está vacía, establece el valor predeterminado y actualiza la cookie
if (!modo && FCookies === "Si") {
    modo = "claro";
    document.cookie = "TemaModo=claro; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/";
}

// Función para aplicar estilos según el modo
function aplicarEstilos() {
    if (modo === "oscuro") {
        $('.bg-white').removeClass('bg-white').addClass('bg-dark');
        $('.textoOscuro').removeClass('textoOscuro').addClass('text-white');
        $('#modoTexto').text('Oscuro');
        $('#modoIcono').show(); // Muestra el icono
        modo = "oscuro";
    } else {
        $('.bg-dark').removeClass('bg-dark').addClass('bg-white');
        $('.text-white').removeClass('text-white').addClass('textoOscuro');
        $('#modoTexto').text('Claro');
        $('#modoIcono').show(); // Muestra el icono
        modo = "claro";
    }
}

// Llama a la función para aplicar estilos al cargar la página


// Función para cambiar los estilos y actualizar la cookie
function cambiarEstilos() {
    var textoModoBoton = document.getElementById("cambiarEstilos");

    if (modo == "claro") {        
        $('.bg-white').removeClass('bg-white').addClass('bg-dark');
        $('.textoOscuro').removeClass('textoOscuro').addClass('text-white');
        textoModoBoton.firstChild.nodeValue = '';
        modo = "oscuro";
    } else {
        $('.bg-dark').removeClass('bg-dark').addClass('bg-white');
        $('.text-white').removeClass('text-white').addClass('textoOscuro');
        textoModoBoton.firstChild.nodeValue = "";
        modo = "claro";
    }

    // Actualiza el valor de la cookie con el nuevo modo
    document.cookie = "TemaModo=" + modo + "; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/";
    aplicarEstilos(); // Llama a la función para aplicar estilos después de cambiarlos
}


    $(document).ready(function () {
        // Asigna la función al evento click del botón
        $('#cambiarEstilos').click(cambiarEstilos);
    });

</script>
  </div>
  <div id="resultadoBusqueda">
  </div>
    <footer id="footer" class="text-center bg-black">
        <div class="container text-white py-4 py-lg-5">
            <ul><li class="list-inline-item me-4"><a class="link-light" href="sobremi/index.html" target="_blank" content="no-referrer" rel="noreferrer">Sobre el desarrollador</a></li></ul>
            <ul><li id="androidTest" class="list-inline-item me-4"><a class="link-light" href="grocesort.apk" content="no-referrer" rel="noreferrer" download>Descargar aplicación Android</a></li></ul>
            <ul class="list-inline">
                <li class="list-inline-item me-4"><a class="link-light" href="cookies.html">Política de Cookies</a></li>
                <li class="list-inline-item"><a class="link-light" href="privacidad.html">Política de privacidad</a></li>
                <li class="list-inline-item"><a class="link-light" onclick="eliminarYRecargar()" style="cursor: pointer;">Cambiar elección de cookies</a></li>
                <script>
                function eliminarYRecargar() {
                    eliminarCookie('FormularioCookies');
                    location.reload();
                }

                function eliminarCookie(nombre) {
                    document.cookie = nombre + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/';
                }
                </script>


            </ul>
            <p class="text-muted mb-0">Desarrollado por Rayner Gabú<br>GroceSort<br>©2023&nbsp;</p>
        </div>

    </footer>
                       
    <script>
        function invertirOrden() {
            var container = document.querySelector(".row-cols-2");
            var elementos = container.children;
            var elementosArray = Array.from(elementos);

            // Invierte el orden del array
            elementosArray.reverse();

            // Elimina los elementos originales del DOM
            for (var i = 0; i < elementos.length; i++) {
                elementos[i].remove();
            }

            // Agrega los elementos en el nuevo orden al DOM
            for (var i = 0; i < elementosArray.length; i++) {
                container.appendChild(elementosArray[i]);
            }
        }

    </script>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>


</body>
</html>
