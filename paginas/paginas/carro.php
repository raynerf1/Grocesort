<!DOCTYPE html>
<!--Carro--->
<html data-bs-theme="light" lang="es">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Lista de la compra - Grocesort</title>
        <link rel="stylesheet" href="../assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="../assets/css/styles.min.css">
    <link rel="stylesheet" href="../assets/css/preloader.css">
    <link rel="stylesheet" href="carroassets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="carroassets/fonts/font-awesome.min.css">
    <link rel="icon" href="https://cdn.discordapp.com/attachments/1166363443637518346/1181710546878337146/GS_Logo.png?ex=65820cb5&is=656f97b5&hm=ed861c8c0bc3f030314a66d50da7e1cd14a9f4f97917927f63252dc64379481f&">
</head>
    <?php
$carro = isset($_COOKIE["carro"]) ? json_decode($_COOKIE["carro"], true) : [];
$cantidadElementos = count($carro);
echo $cantidadElementos;
$total = 0;

?>
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
      </div>
    </div>
  </div>
</nav>
</header>
<div class="shopping-cart">
<div class="px-4 px-lg-0">

  <div class="pb-5">
    <div class="container">
      <div class="row">
        <div class="col-12 p-5 bg-white rounded shadow-sm mb-5">

          <!-- Shopping cart table -->
          <div class="table-responsive">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col" class="border-0 bg-light">
                    <div class="p-2 px-3 text-uppercase">Producto</div>
                  </th>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 text-uppercase">Precio</div>
                  </th>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 text-uppercase">Cantidad</div>
                  </th>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 text-uppercase">Quitar</div>
                  </th>
                </tr>
              </thead>
              <tbody>
                        <?php 
                        foreach ($carro as $producto) {
                            $total += $producto["precio"]*$producto['cantidad'];
                        ?>
                <tr>
                
                  <th scope="row" class="border-0">
                    <div class="p-2">
                      <img src="<?php echo $producto["imagen"]; ?>" alt="" width="70" class="img-fluid rounded shadow-sm">
                      <div class="ml-3 d-inline-block align-middle">
                        <h5 class="mb-0"> <a href="<?php echo $producto["enlace"]; ?>" class="text-dark d-inline-block align-middle" target="_blank" rel="noreferrer"><?php echo $producto["producto"]; ?></a></h5><span class="text-muted font-weight-normal font-italic d-block">Supermercado: <?php echo $producto["supermercado"]; ?></span>
                      </div>
                    </div>
                  </th>
                  <td class="border-0 align-middle"><strong><?php echo $producto["precio"]; ?>€</strong></td>
                  <td class="border-0 align-middle">

<form method="POST" action="modificar_carro.php" class="d-flex align-items-center">
    <input type="hidden" name="idproducto" value="<?php echo $producto["idProducto"]; ?>">
    
    <button type="submit" class="btn btn-primary me-2" name="accion" value="restar">-</button>
    <strong class="me-2 cantidad"><?php echo $producto["cantidad"]; ?></strong>
    <button type="submit" class="btn btn-primary" name="accion" value="sumar">+</button>
</form>



                  <td class="border-0 align-middle"><a href="#" class="text-dark">
                  <form method="POST" action="eliminar_carro.php">
                  <input type="hidden" name="idproducto" value="<?php echo $producto["idProducto"]; ?>">
                  <button type="submit" class="btn btn-danger"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
  <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
  <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
</svg></button></a></form></td>

                </tr>

                        <?php
                        }?>
              </tbody>
            </table>
            <!---->
                        <table class="table">
              <thead>
                <tr>
                  <th scope="col" class="border-0 bg-light">
                    <div class="p-2 px-3 text-uppercase"></div>
                  </th>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 text-uppercase"></div>
                  </th>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 text-uppercase">Total</div>
                  </th>
                  <th scope="col" class="border-0 bg-light">
                    <div class="py-2 text-uppercase"></div>
                  </th>
                </tr>
              </thead>
              <tbody>

                <tr>
                
                  <th scope="row" class="border-0">
                    <div class="p-2">

                    </div>
                  </th>
                                    <th scope="row" class="border-0">
                    <div class="p-2">
                    
                      <img src="" alt="" width="70" class="img-fluid rounded shadow-sm">
                      <div class="ml-3 d-inline-block align-middle">
                        <h5 class="mb-0"> <a href="#" class="text-dark d-inline-block align-middle"></a></h5><span class="text-muted font-weight-normal font-italic d-block"></span>
                      </div>
                    </div>
                  </th>
                  <td class="border-0 align-middle"><strong><?php echo number_format($total, 2); ?>€</strong></td>
                  <td class="border-0 align-middle">
                  <td class="border-0 align-middle"><a href="#" class="text-dark"></td>
                </tr>

              </tbody>
            </table>
          </div>
          <!-- End -->
        </div>
      </div>


    </div>
  </div>
</div>
</div>
    <script src="carroassets/bootstrap/js/bootstrap.min.js"></script>
    <footer id="footer" class="text-center bg-black">
        <div class="container text-white py-4 py-lg-5">
        <li class="list-inline-item me-4"><a class="link-light" href="sobremi/index.html" target="_blank" content="no-referrer" rel="noreferrer">Sobre el desarrollador</a></li> <br>
        <li id="androidTest" class="list-inline-item me-4"><a class="link-light" href="../../android/apk/grocesort.apk" content="no-referrer" rel="noreferrer" download>Descargar aplicación Android</a></li>
            <ul class="list-inline">
                <li class="list-inline-item me-4"><a class="link-light" href="cookies.html">Política de Cookies</a></li>
                <li class="list-inline-item"><a class="link-light" href="privacidad.html">Política de privacidad</a></li>
            </ul>
            <p style="font-family: 'font-awesome', sans-serif;">Desarrollado por Rayner Gabú<br>GroceSort<br>©2023&nbsp;</p>
        </div>
    </footer>
</body>

</html>
