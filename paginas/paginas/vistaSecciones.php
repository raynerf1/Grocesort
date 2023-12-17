<!DOCTYPE html>
<!--Vista secciones-->
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Grocesort by Rayner</title>
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
        <a class="nav-link" aria-current="page" href="secciones.php">Secciones</a>
        <a class="nav-link" href="sobremi/index.html">Sobre mí</a>
        <a class="nav-link" href="privacidad.html">Privacidad</a>
        <!--
        <a class="nav-link" id="cambiarEstilos" data-bs-toggle="tooltip" data-bs-placement="bottom" title="Cambiar modo de color de la página" style="cursor: pointer; <?php if ($_COOKIE["FormularioCookies"] === 'No'){echo 'display: none';}  ?>"
    <span id="modoTexto"></span>
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
          <?php 
          if (isset($_POST['nombre_equipo'])) {
            //$seccion = $_POST['seccion'];
            $subseccion = $_POST['nombre_equipo'];
            
        }
          ?>
          <br>
          <div class="container-fluid">
            <nav class=" ms-5 mt-5 " aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="secciones.php">Secciones</a></li>
                <!--<li class="breadcrumb-item"><a href="javascript:void(0);" onclick="window.history.back();"><?php echo $seccion; ?></a></li>-->
                <li class="breadcrumb-item active" aria-current="page"><?php echo $subseccion; ?></li>
              </ol>
            </nav>
          </div>
    </header>


<div id="div3" class="bg-white">

    <section class="py-4 py-xl-5">
        <div class="container-fluid">
        <div class="row row-cols-2 row-cols-sm-2 row-cols-md-2 row-cols-lg-4 row-cols-xl-4 row-cols-xxl-4 justify-content-center" id="row-1">
        <?php
        include('../../config.php'); // Asegúrate de que config.php contiene la configuración de la base de datos.

        //$resultados = array(); 
        if (isset($_POST['nombre_equipo'])) {
            $input = $_POST['nombre_equipo'];

            try {
                $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=' . DB_CHARSET, DB_USER, DB_PASSWORD);
                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                $consulta = "SELECT subseccion, subseccionutf, imagen FROM `subsecciones` where seccion = :input";
                $stmt = $pdo->prepare($consulta);
                //$input = '%' . $input . '%';
                $stmt->bindParam(':input', $input, PDO::PARAM_STR);

                $stmt->execute();

                if ($stmt->rowCount() > 0) {
                    while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)) {
                        ?>
                        <div class="col justify-content-center d-flex align-items-center"
                        id="<?php echo str_replace(' ', '', strtolower(trim($fila["subseccion"]))); ?>">

                            <form method="POST" action="vistaPrecioTest.php"><!--Cambiar en IF-->
                                <input type="hidden" name="nombre_subseccion" value="<?php echo $fila["subseccion"]; ?>">
                                <input type="hidden" name="seccion" value="<?php echo $input; ?>">
                                <input type="hidden" name="foto_logo" value="test<?php echo $fila["subseccion"]; ?>">
                                <a class="justify-content-center d-flex align-items-center columna"
                                   href="#"
                                   onclick="event.preventDefault(); this.closest('form').submit();">
                                    <div class="card bg-white textoOscuro" style="border-style: none;">
                                        <div class="card-body">
                                            <h1 class="text-start"><?php echo isset($fila["subseccionutf"]) ? $fila["subseccionutf"] : $fila["subseccion"]; ?></h1>
                                            <img class="img-fluid order-4 coche"
                                                 src=<?php echo $fila["imagen"]; ?>
                                                 width="700px">
                                        </div>
                                    </div>

                                </a>
                            </form>
                        </div>
                        <?php
                    }
                } else {
                    echo 'No se encontraron resultados.';
                    echo '    <nav class="mb-5">
    </nav>
    <nav class="pb-5">
    </nav>
    <nav class="pb-5">
    </nav>
    <nav class="pb-5">
    </nav>
    <nav class="pb-5">
    </nav>
    <nav class="pb-5">
    </nav>
    <nav class="pb-5">
    </nav>    
    <nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav>'
    ;
                }
            } catch (PDOException $e) {
                echo 'Error al conectar a la base de datos: ' . $e->getMessage();
            }
        }
        ?>
        </div>
        </div>
    </section>
    <nav class="mb-5">
    </nav>
    <nav class="pb-5">
    </nav>
    <nav class="pb-5">
    </nav>
    <nav class="pb-5">
    </nav>
    <nav class="pb-5">
    </nav>

</div>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    <footer id="footer" class="text-center bg-black" style="display: block;">
        <div class="container text-light py-4 py-lg-5">
        <li class="list-inline-item me-4"><a class="link-light" href="sobremi/index.html" target="_blank" content="no-referrer" rel="noreferrer">Sobre el desarrollador</a></li> <br>
        <li id="androidTest" class="list-inline-item me-4"><a class="link-light" href="../../android/apk/grocesort.apk" content="no-referrer" rel="noreferrer" download>Descargar aplicación Android</a></li>
            <ul class="list-inline">
                <li class="list-inline-item me-4"><a class="link-light" href="cookies.html">Política de Cookies</a></li>
                <li class="list-inline-item"><a class="link-light" href="privacidad.html">Política de privacidad</a></li>
            </ul>
            <p style="font-family: 'font-awesome', sans-serif;">Desarrollado por Rayner Gabú<br>GroceSort<br>©2023&nbsp;</p>
        </div>
    </footer>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    $(document).ready(function() {
        aplicarEstilos();

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
        textoModoBoton.firstChild.nodeValue = 'Oscuro';
        modo = "oscuro";
    } else {
        $('.bg-dark').removeClass('bg-dark').addClass('bg-white');
        $('.text-white').removeClass('text-white').addClass('textoOscuro');
        textoModoBoton.firstChild.nodeValue = "Claro";
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
</body>
</html>
