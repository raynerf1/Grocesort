
<!DOCTYPE html>
<!--Vista precio test-->
<html data-bs-theme="light" lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Rayner</title>
    <link rel="stylesheet" href="importedassets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="importedassets/fonts/font-awesome.min.css">
    <link rel="stylesheet" href="importedassets/fonts/ionicons.min.css">
    <link rel="stylesheet" href="importedassets/css/Animated-Pretty-Product-List-v12-Animated-Pretty-Product-List.css">
    <link rel="stylesheet" href="../assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="../assets/css/styles.min.css">
    <link rel="stylesheet" href="../assets/css/preloader.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.5/gsap.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <style>
        .oculto {
            display: none;
        }
                    .col-2 button:hover {
                background-color: green;
            }
    </style>
</head>

<body>
    <header>
        <nav class="navbar navbar-expand-lg bg-light fixed-top">
            <div class="container-fluid">
              <a class="navbar-brand">Grocesort</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse justify-content-end" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                  <a class="nav-link" aria-current="page" href="secciones.php">Inicio</a>
                  <a class="nav-link" href="">Patrocinadores</a>
                  <a class="nav-link" href="">Precios</a>
                  <a class="nav-link" href="">Privacidad</a>
                  <a class="nav-link" href="">Sobre nosotros</a>
                  
</div>
                <?php 
                $carro = isset($_COOKIE["carro"]) ? json_decode($_COOKIE["carro"], true) : [];
                $cantidadElementos = count($carro);?>
                <a class="nav-link" href="carro.php">
    <button type="button" class="btn btn-primary ml-5" <?php if ($_COOKIE["FormularioCookies"] === 'No'){echo 'style="display: none"';}  ?>>
        Cesta<span class="badge text-bg-secondary"><?php echo $cantidadElementos;?></span>
    </button>
</a>
              </div>
            </div>
          </nav>
          <?php 
session_start();

if (isset($_POST['nombre_subseccion'])) {
    $seccion = $_POST['seccion'];
    $subseccion = $_POST['nombre_subseccion'];
    
    $_SESSION['nombre_subseccion'] = $subseccion;
} elseif (isset($_GET['nombre_subseccion'])) {
    $subseccion = $_GET['nombre_subseccion'];
    $testCarro = $subseccion;
} else {
}
          ?>
          <br>
          <div class="container-fluid ">
            <nav class=" ms-5 mt-5 " aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="secciones.php">Secciones</a></li>
                <li class="breadcrumb-item"><a href="javascript:void(0);" onclick="window.history.back();"><?php echo $seccion; ?></a></li>
                <li class="breadcrumb-item active" aria-current="page"><?php echo $subseccion; ?></li>
                
              </ol>
              
            </nav>
          </div>
    </header>
        <div class="container-fluid">
            <div class="row py-1 py-md-1">
                <div class="col-12 col-sm-2">
                    <h4 class="display-9">Filtros</h4>
                    <div class="d-flex flex-sm-column flex-row flex-grow-1 align-items-center align-items-sm-start px-3 text-white" style=" padding: 10px 5px 5px 5px ;border-radius: 10px;  background-color: rgb(233, 233, 233);">
                        <ul id="menu" class="nav nav-pills flex-sm-column flex-row flex-nowrap flex-shrink-1 flex-sm-grow-0 flex-grow-1 my-3 mb-sm-auto justify-content-center align-items-center align-items-sm-start w-100">

                            <li class="w-100">
                                <a class="px-2 nav-link px-sm-0 ps-2" href="#submenu1" data-bs-toggle="collapse">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down-up" viewBox="0 0 16 16" onclick="invertirOrden()">
                                    <path fill-rule="evenodd" d="M11.5 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L11 2.707V14.5a.5.5 0 0 0 .5.5zm-7-14a.5.5 0 0 1                                               .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L4 13.293V1.5a.5.5 0 0 1 .5-.5z"/>
                                </svg>
                                <span class="ms-1 d-none d-sm-inline" onclick="invertirOrden()">Invertir orden</span></a>
                            </li>
                            
                            <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-shop" viewBox="0 0 16 16">
        <path d="M2.97 1.35A1 1 0 0 1 3.73 1h8.54a1 1 0 0 1 .76.35l2.609 3.044A1.5 1.5 0 0 1 16 5.37v.255a2.375 2.375 0 0 1-4.25 1.458A2.371 2.371 0 0 1 9.875 8 2.37 2.37 0 0 1 8 7.083 2.37 2.37 0 0 1 6.125 8a2.37 2.37 0 0 1-1.875-.917A2.375 2.375 0 0 1 0 5.625V5.37a1.5 1.5 0 0 1 .361-.976l2.61-3.045zm1.78 4.275a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0 1.375 1.375 0 1 0 2.75 0V5.37a.5.5 0 0 0-.12-.325L12.27 2H3.73L1.12 5.045A.5.5 0 0 0 1 5.37v.255a1.375 1.375 0 0 0 2.75 0 .5.5 0 0 1 1 0zM1.5 8.5A.5.5 0 0 1 2 9v6h1v-5a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v5h6V9a.5.5 0 0 1 1 0v6h.5a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1H1V9a.5.5 0 0 1 .5-.5zM4 15h3v-5H4v5zm5-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1v-3zm3 0h-2v3h2v-3z"/>
    </svg>
    <span class="ms-1 d-none d-sm-inline">Supermercado</span>
</a>
                                <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="ahorramascb" onclick='ocultarElementosPorClase("Ahorra Mas");'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Ahorra Mas</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="alcampocb" onclick='ocultarElementosPorClase("Alcampo");' checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Alcampo</label>
                                        </div>
                                      </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="carrefourcb" onclick='ocultarElementosPorClase("Carrefour");' checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Carrefour</label>
                                        </div>
                                      </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="diacb" onclick='ocultarElementosPorClase("Dia");' checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Dia</label>
                                        </div>
                                      </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="eroskicb" onclick='ocultarElementosPorClase("Eroski");' checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Eroski</label>
                                        </div>
                                      </li>                                      

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="mercadonacb" onclick='ocultarElementosPorClase("Mercadona");' checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Mercadona</label>
                                        </div>
                                      </li>
                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>


                             <li class="dropdown w-100"><a id="dropdown" <?php switch ($subseccion){
                                    case 'Arroz redondo':
                                    case 'Azucar blanco':
                                    case 'Azucar moreno':
                                    case 'Barquillos nata':
                                    case 'Barquillos chocolate':
                                    case 'Bebida Almendras':
                                    case 'Bebida Arroz':
                                    case 'Bebida Soja';
                                    case 'Bebida Avena':
                                    case 'Horchata':
                                    case 'Cafe molido':
                                    case 'Cafe molido descafeinado':
                                    #case 'Cafe molido tostado':
                                    case 'Cafe soluble descafeinado':
                                    case 'Cereales cacao rellenos leche':
                                    case 'Cereales cacao rellenos chocolate':
                                    case 'Copos de avena integral suave':
                                    case 'Bolas de cacao':
                                    case 'Trigo inflado con miel':
                                    case 'Arroz inflado con cacao':
                                    case 'Copos de cacao':
                                    case 'Copos de maiz':
                                    case 'Galleta maria pack':
                                    case 'Galleta maria dorada pack':
                                    case 'Galleta maria integral pack':
                                    case 'Galleta tostada':
                                    case 'Galleta digestive':
                                    case 'Galleta digestive avena':
                                    case 'Cookies':
                                    case 'Galleta rellena crema chocolate':
                                    case 'Gazpacho':
                                    case 'Salmorejo':
                                    case 'Harina pizza':
                                    case 'Harina trigo reposteria':
                                    case 'Harina trigo fritos y rebozados':
                                    case 'Harina trigo bizcochos':
                                    case 'Harina maiz':
                                    case 'Harina de trigo integral':
                                    case 'Conos':
                                    case 'Bombon':
                                    case 'Tarrinas':
                                    case 'Docena Huevo':
                                    case 'Claras Huevo':
                                    case 'Mantequilla':
                                    case 'Levadura':
                                    case 'Mermelada de fresa':
                                    case 'Mermelada de melocoton':
                                    case 'Mermelada de naranja':
                                    case 'Barra pan':
                                    case 'Pan hamburguesa':
                                    case 'Pan hotdog':
                                    case 'Macarron pluma':
                                    case 'Macarron tiburon':
                                    case 'Fideua':
                                    case 'Macarron espiral vegetal':
                                    case 'Tallarin':
                                    case 'Spaghetti':
                                    case 'Macarron pajarita vegetal':?>
                                        style ="display:none;"
                                    <?php   
                                    break; ?> 
                                    <?php
                                    }?>
                              class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-columns-gap" viewBox="0 0 16 16">
  <path d="M6 1v3H1V1h5zM1 0a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1H1zm14 12v3h-5v-3h5zm-5-1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1h-5zM6 8v7H1V8h5zM1 7a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1H1zm14-6v7h-5V1h5zm-5-1a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1h-5z"/>
</svg>
    <span class="ms-1 d-none d-sm-inline">Formato</span>
</a>
    <?php 
    switch ($subseccion){
        case 'Aceite oliva':
        case 'Aceite girasol':?>
                                <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbBotella1L" onclick="ocultarBotella1L()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Botella 1L</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbGarrafa5L" onclick="ocultarGarrafa5L()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Garrafa 5L</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
     <?php  
        break;
        case 'Batido de chocolate':
        case 'Batido de fresa':
        case 'Batido de vainilla':?>
                                <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbBotella1L" onclick="ocultarBotella1L()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Botella 1L</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbPack6" onclick="ocultarPack6()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Pack</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
        <?php
            break;
        case 'Cafe soluble':?>
                                <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbCafeSoluble" onclick="ocultarCafeSolubleNormal()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Soluble normal</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbSolubleDescafeinado" onclick="ocultarCafeSolubleDescafeinado()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Descafeinado</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
        <?php
            break;
        case 'Cafe molido tostado':?>
                                <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbCafeSoluble" onclick="ocultarCafeTostadoNormal()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Tostado normal</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbSolubleDescafeinado" onclick="ocultarCafeTostadoDescafeinado()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Descafeinado</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
        <?php
            break;        
            case 'Muesli':?>
                                <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbCafeSoluble" onclick="ocultarMuesliNormal()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Muesli solo</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbSolubleDescafeinado" onclick="ocultarMuesliFruta()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Frutas</label>
                                        </div>
                                      </li>

                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbSolubleDescafeinado" onclick="ocultarMuesliFrutosSecos()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Frutos secos </label>
                                        </div>
                                      </li>

                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbSolubleDescafeinado" onclick="ocultarMuesliChocolate()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Chocolate</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
        <?php
            break;            
            case 'Copos de arroz y trigo':?>
                                <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbCafeSoluble" onclick="ocultarCoposArrozNormal()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Simples</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbSolubleDescafeinado" onclick="ocultarCoposArrozFrutosRojos()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Frutos rojos</label>
                                        </div>
                                      </li>


                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
        <?php
            break;            
            case 'Galleta estilo oreo':?>
                                <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbCafeSoluble" onclick="ocultarOreoNormal()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Simples</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbSolubleDescafeinado" onclick="ocultarOreoChocoBlanco()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Cubiertas chocolate blanco</label>
                                        </div>
                                      </li>


                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
        <?php
            break;            
            case 'Harina de trigo':?>
                                <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbCafeSoluble" onclick="ocultarHarinaTrigoNormal()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Trigo normal</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbSolubleDescafeinado" onclick="ocultarHarinaTrigoIntegral()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Trigo integral</label>
                                        </div>
                                      </li>


                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
        <?php
            break;
            case 'Bicarbonato':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbBicarbonatoBote" onclick="ocultarBotes()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Botes</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbBicarbonatoPack1kg" onclick="ocultarPaquete1kg()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Paquetes 1kg</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;            
            case 'Leche':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarLecheEntera" onclick="ocultarLecheEntera()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Entera</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarLecheEnteraSL" onclick="ocultarLecheEnteraSL()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Entera sin lactosa</label>
                                        </div>
                                      </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarLecheSemidesnatada" onclick="ocultarLecheSemidesnatada()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Semidesnatada</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarLecheSemidesnatadaSL" onclick="ocultarLecheSemidesnatadaSL()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Semidesnatada sin lactosa</label>
                                        </div>
                                      </li>                                      
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarLecheDesnatada" onclick="ocultarLecheDesnatada()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Desnatada</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarLecheDesnatadaSL" onclick="ocultarLecheDesnatadaSL()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Desnatada sin lactosa</label>
                                        </div>
                                      </li>
                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;            
            case 'Yogures':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarYogurPacks" onclick="ocultarYogurPacks()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Packs</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarYogurBote1kg" onclick="ocultarYogurBote1kg()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Botes 1kg</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;            
            case 'Garbanzos':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarGarbanzoCocido" onclick="ocultarGarbanzoCocido()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Cocidos en bote</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarGarbanzoCrudo" onclick="ocultarGarbanzoCrudo()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Paquete crudo 1kg</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;            
            case 'Alubias':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCocido" onclick="ocultarAlubiaCocida()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Cocidos en bote</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCrudo" onclick="ocultarAlubiaCrudo()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Paquete crudo 1kg</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;            
            case 'Lentejas':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCocido" onclick="ocultarLentejaCocida()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Cocidos en bote</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCrudo" onclick="ocultarLentejaCrudo()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Paquete crudo 1kg</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;            
        case 'Miel':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCocido" onclick="ocultarMielAzahar()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Bote azahar</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCrudo" onclick="ocultarMielFlores()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Tarro flores</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;        
            case 'Pan molde':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">                                       
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCocido" onclick="ocultarMoldeBlancoFamiliar()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Blanco familiar</label>
                                        </div>
                                        </li>                                     
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCocido" onclick="ocultarMoldeBlancoSinCorteza()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Blanco sin corteza</label>
                                        </div>
                                        </li>
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCocido" onclick="ocultarMoldeIntegral()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Integral</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCrudo" onclick="ocultarMoldeIntegralSinCorteza()" checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Integral sin corteza</label>
                                        </div>
                                      </li>

                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;            
            case 'Macarron espiral':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">                                       
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCocido" onclick="ocultarEspiralBlanco()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Espiral </label>
                                        </div>
                                        </li>                                     
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAlubiaCocido" onclick="ocultarEspiralVegetales()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Espiral vegetales</label>
                                        </div>
                                        </li>
                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
    }                   
    ?>
    <?php 
    switch ($subseccion){
        case 'Aceite oliva':?>
    <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-columns-gap" viewBox="0 0 16 16">
  <path d="M6 1v3H1V1h5zM1 0a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1H1zm14 12v3h-5v-3h5zm-5-1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1h-5zM6 8v7H1V8h5zM1 7a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1H1zm14-6v7h-5V1h5zm-5-1a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1h-5z"/>
</svg>
    <span class="ms-1 d-none d-sm-inline">Tipo aceite</span>
</a>
<ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbAceite04" onclick='ocultarAceite04();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Aceite 0,4</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbAceite04" onclick='ocultarAceite1();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Aceite 1</label>
                                        </div>
                                        </li>
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                                 <?php  
        break;        
        case 'Conos':?>
    <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-columns-gap" viewBox="0 0 16 16">
  <path d="M6 1v3H1V1h5zM1 0a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1H1zm14 12v3h-5v-3h5zm-5-1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1h-5zM6 8v7H1V8h5zM1 7a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1H1zm14-6v7h-5V1h5zm-5-1a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1h-5z"/>
</svg>
    <span class="ms-1 d-none d-sm-inline">Sabor</span>
</a>
<ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarNataFresa" onclick='ocultarNataFresa();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Nata y fresa</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarVainillaChocolate" onclick='ocultarVainillaChocolate();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Vainilla y chocolate</label>
                                        </div>
                                        </li>
                                     <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarNataTrufa" onclick='ocultarNataTrufa();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Nata y trufa</label>
                                        </div>
                                        </li>
                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarNataTurron" onclick='ocultarNataTurron();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Nata y turron</label>
                                        </div>
                                        </li>                                     
                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTartaQueso" onclick='ocultarTartaQueso();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Tarta de queso</label>
                                        </div>
                                        </li>
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                                 <?php  
        break;         
        case 'Bombon':?>
    <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-columns-gap" viewBox="0 0 16 16">
  <path d="M6 1v3H1V1h5zM1 0a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1H1zm14 12v3h-5v-3h5zm-5-1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1h-5zM6 8v7H1V8h5zM1 7a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1H1zm14-6v7h-5V1h5zm-5-1a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1h-5z"/>
</svg>
    <span class="ms-1 d-none d-sm-inline">Sabor</span>
</a>
<ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarNataFresa" onclick='ocultarBombonChocolateNata();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Chocolate y nata</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarVainillaChocolate" onclick='ocultarBombonAlmendra();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Bombon Almendrado</label>
                                        </div>
                                        </li>
                                     <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarNataTrufa" onclick='ocultarBombonChocolateBlanco();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Chocolate blanco</label>
                                        </div>
                                        </li>
                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarNataTurron" onclick='ocultarBombonAvellana();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Bombon avellanas</label>
                                        </div>
                                        </li>                                     
                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTartaQueso" onclick='ocultarBombonChocolateTriple();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> 3 chocolates</label>
                                        </div>
                                        </li>
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                                 <?php  
        break;        
        case 'Tarrinas':?>
    <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-columns-gap" viewBox="0 0 16 16">
  <path d="M6 1v3H1V1h5zM1 0a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1H1zm14 12v3h-5v-3h5zm-5-1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1h-5zM6 8v7H1V8h5zM1 7a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1H1zm14-6v7h-5V1h5zm-5-1a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1h-5z"/>
</svg>
    <span class="ms-1 d-none d-sm-inline">Sabor</span>
</a>
<ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTarrinaVainilla" onclick='ocultarTarrinaVainilla();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Vainilla</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTarrinaLimon" onclick='ocultarTarrinaLimon();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Sorbete limon</label>
                                        </div>
                                        </li>
                                     <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTarrinaStracciatella" onclick='ocultarTarrinaStracciatella();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Stracciatella</label>
                                        </div>
                                        </li>
                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTarrinaChocolate" onclick='ocultarTarrinaChocolate();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Chocolate y trozos</label>
                                        </div>
                                        </li>                                     
                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTarrinaNataNueces" onclick='ocultarTarrinaNataNueces();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Nata y nueces</label>
                                        </div>
                                        </li>
                                    <li>                                    
                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTarrinaChocolateTriple" onclick='ocultarTarrinaChocolateTriple();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Tres chocolates</label>
                                        </div>
                                        </li>
                                    <li>                                    
                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTarrinaFrutasBosque" onclick='ocultarTarrinaFrutasBosque();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Frutas del bosque</label>
                                        </div>
                                        </li>
                                    <li>
                                    <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTarrinaTurron" onclick='ocultarTarrinaTurron();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Turron</label>
                                        </div>
                                        </li>
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                                 <?php  
        break;        
        case 'Docena Huevo':?>
    <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-columns-gap" viewBox="0 0 16 16">
  <path d="M6 1v3H1V1h5zM1 0a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1H1zm14 12v3h-5v-3h5zm-5-1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1h-5zM6 8v7H1V8h5zM1 7a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1H1zm14-6v7h-5V1h5zm-5-1a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1h-5z"/>
</svg>
    <span class="ms-1 d-none d-sm-inline">Tamaño</span>
</a>
<ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarDocenaM" onclick='ocultarDocenaM();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> M</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarDocenaL" onclick='ocultarDocenaL();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> L</label>
                                        </div>
                                        </li>
                                     <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarDocenaXL" onclick='ocultarDocenaXL();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> XL</label>
                                        </div>
                                        </li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                                 <?php  
        break;        
        case 'Yogures':?>
    <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-columns-gap" viewBox="0 0 16 16">
  <path d="M6 1v3H1V1h5zM1 0a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1H1zm14 12v3h-5v-3h5zm-5-1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1h-5zM6 8v7H1V8h5zM1 7a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V8a1 1 0 0 0-1-1H1zm14-6v7h-5V1h5zm-5-1a1 1 0 0 0-1 1v7a1 1 0 0 0 1 1h5a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1h-5z"/>
</svg>
    <span class="ms-1 d-none d-sm-inline">Sabor</span>
</a>
<ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarYogurNatural" onclick='ocultarYogurNatural();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Natural</label>
                                        </div>
                                        </li>                                      
                                        <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarYogurNaturalGriego" onclick='ocultarYogurNaturalGriego();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Griego Natural</label>
                                        </div>
                                        </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarYogurNaturalAzucar" onclick='ocultarYogurNaturalAzucar();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Natural con azucar </label>
                                        </div>
                                        </li>
                                     <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarYogurSabores" onclick='ocultarYogurSabores();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Sabores</label>
                                        </div>
                                        </li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                                 <?php  
        break;        
    case 'Alubias':?>
    <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-capsule" viewBox="0 0 16 16">
  <path d="M1.828 8.9 8.9 1.827a4 4 0 1 1 5.657 5.657l-7.07 7.071A4 4 0 1 1 1.827 8.9Zm9.128.771 2.893-2.893a3 3 0 1 0-4.243-4.242L6.713 5.429l4.243 4.242Z"/>
</svg>

    <span class="ms-1 d-none d-sm-inline">Tipo alubia</span>
</a>
<ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarYogurNatural" onclick='ocultarAlubiaPinta();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Pintas</label>
                                        </div>
                                        </li>                                      
                                        <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarYogurNaturalGriego" onclick='ocultarAlubiaBlanca();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Blancas</label>
                                        </div>
                                        </li>

                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                                 <?php  
        break;   }                   
    ?>
    <!--
                            <li class="w-100"><a class="px-2 nav-link px-sm-0 ps-2" href="#"><i class="fa fa-th-large bi-grid fs-5 ms-2"></i><span class="ms-1 d-none d-sm-inline">Products</span></a></li>
                            <li class="w-100"><a class="px-2 nav-link px-sm-0 ps-2" href="#"><i class="fa fa-group bi-people fs-5 ms-2"></i><span class="ms-1 d-none d-sm-inline">Customers</span></a></li>-->
                        </ul>
                        <div class="input-group d-none d-md-flex mt-3"><input class="form-control" type="text" placeholder="Search..."><button class="btn btn-primary" type="button"><i class="fa fa-search"></i></button></div>
                    </div>
                </div>

                <div class="col-12 col-sm-9 col-sm-9">
                    <div class="container">
                    
                        <div class="row product-list dev">
                        <?php

                        include('../../config.php');
                        if (isset($_POST['nombre_subseccion'])) {
                            $subseccion = $_POST['nombre_subseccion'];
                            $seccion = $_POST['seccion'];



                            $consultaextra = "";
                            $consultaextra2 = "";
                            switch ($subseccion){
                                  case "Azucar blanco":
                                    $consultaextra = ' where pr.subseccion = "azucar blanco" ';
                                break;
                                case "Galleta estilo oreo":
                                    $consultaextra2 = ' or producto LIKE "galleta%chocolate%blanco" ';
                                break;
                            }

                            try{
                                
                                $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=' . DB_CHARSET, DB_USER, DB_PASSWORD, array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET SESSION SQL_BIG_SELECTS=1'));
                                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                                $consulta = "SELECT p.*, pr.seccion, pr.subseccion, pr.descripcion, pr.imagen, pr.enlace
                                                FROM precios p
                                                INNER JOIN (
                                                    SELECT producto, supermercado, MAX(fecha) AS max_fecha
                                                    FROM precios
                                                    WHERE fecha <> '' -- Para excluir registros sin fecha
                                                    AND (supermercado = 'ahorra mas' OR supermercado = 'alcampo' OR supermercado = 'dia' OR supermercado = 'eroski' OR supermercado = 'mercadona' OR supermercado = 'carrefour')
                                                    AND producto LIKE :subseccion " . $consultaextra2 ."
                                                    GROUP BY producto, supermercado
                                                ) max_precios
                                                ON p.producto = max_precios.producto
                                                AND p.supermercado = max_precios.supermercado
                                                AND p.fecha = max_precios.max_fecha
                                                LEFT JOIN productos pr
                                                ON p.producto = pr.producto
                                                AND p.supermercado = pr.supermercado " . $consultaextra ."
                                                 order by precio asc;";
                                


                                $stmt = $pdo->prepare($consulta);
                                $input = $subseccion . '%';

                                switch ($subseccion){
                                  case "Azucar blanco":
                                     $input = 'Azucar%';
                                break;
                                  case "Batido de chocolate":
                                     $input = 'Batido chocolate%';
                                break;
                                case "Batido de fresa":
                                     $input = 'Batido fresa%';
                                break;
                                case "Batido de vainilla":
                                     $input = 'Batido vainilla%';
                                break;
                                case "Cafe molido":
                                     $input = 'Cafe molido';
                                break;                                
                                case "Galleta digestive":
                                     $input = 'Galleta digestive';
                                break;                                
                                case "Galleta estilo oreo":
                                     $input = 'Galleta oreo';
                                break;
                                case "Conos":
                                     $input = 'Cono%';
                                break;
                                case "Bombon":
                                     $input = '%Bombon%';
                                break;
                                case "Tarrinas":
                                     $input = 'Tarrina%';
                                break;                                
                                case "Yogures":
                                     $input = 'Yogur%';
                                break;
                                case "Garbanzos":
                                     $input = 'Garbanzo%';
                                break;                                
                                case "Alubias":
                                     $input = 'Alubia%';
                                break;                                
                                case "Lentejas":
                                     $input = 'Lenteja%';
                                break;                                
                                case "Barra pan":
                                     $input = 'Barra de pan%';
                                break;                                
                                case "Pan molde":
                                     $input = 'Pan de molde%';
                                break;                                
                                case "Pizzas":
                                     $input = 'Pizza%';
                                break;                                
                                case "Flanes":
                                     $input = 'Flan%';
                                break;                                
                                case "Gelatinas":
                                     $input = 'Gelatina%';
                                break;
                                case "Champinones":
                                     $input = 'Champinon%';
                                break;                                
                                case "Alcachofas":
                                     $input = 'Alcachofa%';
                                break;                                
                                case "Zumo de naranja":
                                     $input = 'Zumo naranja%';
                                break;
                                case "Zumo de pina":
                                     $input = 'Zumo pina%';
                                break;                                
                                case "Zumo de naranja":
                                     $input = 'Zumo naranja%';
                                break;
                                case "Zumo de pina":
                                     $input = 'Zumo pina%';
                                break;
                                case "Zumo de manzana":
                                     $input = 'Zumo manzana%';
                                break;                                
                                case "Zumo de melocoton":
                                     $input = 'Zumo melocoton%';
                                break;
                                }

                                $stmt->bindParam(':subseccion', $input, PDO::PARAM_STR);
                                $stmt->execute();
                                if ($stmt->rowCount() > 0) {
                                    while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)) {?>
                                
                                <div id="<?php echo $fila["id"]; ?>" class="col-sm-6 col-md-4 product-item animation-element slide-top-left <?php echo $fila["supermercado"]; ?>">
                                <form method="POST" action="anadir_carro.php">
                                <input type="hidden" name="idproducto" value="<?php echo $fila["id"];?>">
                                <div class="product-container <?php switch ($subseccion){
                                    case 'Aceite oliva':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 15)); 
                                    break; 
                                    case 'Aceite girasol':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 17)); 
                                    break;
                                    case 'Batido de chocolate':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 19)); 
                                    break;
                                    case 'Batido de fresa':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 15)); 
                                    break;                                    
                                    case 'Batido de vainilla':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 19)); 
                                    break;
                                    case 'Cafe molido tostado':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 25)); 
                                    break;
                                    case 'Cafe soluble':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 18)); 
                                    break;
                                    case 'Bicarbonato':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 18)); 
                                    break;
                                    }?>">
                                    <div class="row" test="<?php echo $subseccion; ?>">
                                        <div class="col-md-12"><a class="product-image" href="#"><img src="<?php echo $fila["imagen"]; ?>"></a></div>
                                    </div>
                                    <div class="row">
                                        <div class="col-8">
                                            <h2><a href="#"><?php echo $fila["producto"];?><?php switch ($fila["producto"]){ 
                                                case 'Muesli':
                                                 echo " solo"; 
                                                break; 
                                                case 'Copos de arroz y trigo':
                                                 echo " solo"; 
                                                break;
                                                case 'Galleta oreo':
                                                 echo "."; 
                                                break; 
                                                case 'Harina de trigo':
                                                 echo "."; 
                                                break;
                                                case 'Leche entera':
                                                 echo "."; 
                                                break;
                                                case 'Leche semidesnatada':
                                                 echo "."; 
                                                break;
                                                case 'Leche desnatada':
                                                 echo "."; 
                                                break;                                                
                                                case 'Yogur griego natural':
                                                 echo "."; 
                                                break;                                                
                                                case 'Garbanzo':
                                                 echo " crudo"; 
                                                break;
                                                case 'Alubia blanca':
                                                 echo "."; 
                                                break;
                                                case 'Alubia pinta':
                                                 echo "."; 
                                                break;                                                
                                                case 'Lenteja':
                                                 echo " cruda 1kg"; 
                                                break;                                                
                                                case 'Pan de molde integral':
                                                 echo "."; 
                                                break;                                                
                                                case 'Macarron espiral':
                                                 echo "."; 
                                                break;
                                    }?></a></h2>
                                        </div>
                                        <div class="col-4"><img src="..\imagenes\supermercados\iconos/<?php echo str_replace(' ', '', strtolower($fila["supermercado"])); ?>.png" style="max-width: 100%;"></div>
                                    </div>
                                    <div class="product-rating"><a class="small-text" ><?php echo $fila["detalle"]; ?><?php echo ' '. $fila["supermercado"]; ?></a></div>
                                    <div class="row">
                                        <div class="col-12">
                                            <p class="product-description" style="height: 40px;"><?php echo $fila["descripcion"]; ?></p>
                                            <div class="row">
                                                <div class="col-6"><a href="<?php echo $fila["enlace"]; ?>" target="_blank" rel="noreferrer"><button class="btn btn-light" type="button">Comprar ahora</button></a></div>
                                                <div class="col-6"><p class="product-price"><?php echo $fila["precio"]; ?>€</p></div>
                                            </div>
                                        </div>
                                        <?php 
                                        if ($_COOKIE["FormularioCookies"] === 'Si') {
                                        ?>
                                        <div class="col-12">
                                            <div class="row">
                                                <div class="col-2"><button class="btn btn-light" type="submit">+</button></div>
                                            </div>
                                        </div><?php
                                                } else {}
                                              ?>
                                    </div>
                                </div>
                            </div>
                            </form>
                                    <?php
                                    }
                                }
                            } catch (PDOException $e) {
                echo 'Error al conectar a la base de datos: ' . $e->getMessage();
            }    
                        } elseif (isset($_GET['nombre_subseccion'])) {
                            $subseccion = $_GET['nombre_subseccion'];
                            $seccion = $_POST['seccion'];



                            $consultaextra = "";
                            $consultaextra2 = "";
                            switch ($subseccion){
                                  case "Azucar blanco":
                                    $consultaextra = ' where pr.subseccion = "azucar blanco" ';
                                break;
                                case "Galleta estilo oreo":
                                    $consultaextra2 = ' or producto LIKE "galleta%chocolate%blanco" ';
                                break;
                            }

                            try{
                                
                                $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=' . DB_CHARSET, DB_USER, DB_PASSWORD, array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET SESSION SQL_BIG_SELECTS=1'));
                                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                                $consulta = "SELECT p.*, pr.seccion, pr.subseccion, pr.descripcion, pr.imagen, pr.enlace
                                                FROM precios p
                                                INNER JOIN (
                                                    SELECT producto, supermercado, MAX(fecha) AS max_fecha
                                                    FROM precios
                                                    WHERE fecha <> '' -- Para excluir registros sin fecha
                                                    AND (supermercado = 'ahorra mas' OR supermercado = 'alcampo' OR supermercado = 'dia' OR supermercado = 'eroski' OR supermercado = 'mercadona' OR supermercado = 'carrefour')
                                                    AND producto LIKE :subseccion " . $consultaextra2 ."
                                                    GROUP BY producto, supermercado
                                                ) max_precios
                                                ON p.producto = max_precios.producto
                                                AND p.supermercado = max_precios.supermercado
                                                AND p.fecha = max_precios.max_fecha
                                                LEFT JOIN productos pr
                                                ON p.producto = pr.producto
                                                AND p.supermercado = pr.supermercado " . $consultaextra ."
                                                 order by precio asc;";
                                


                                $stmt = $pdo->prepare($consulta);
                                $input = $subseccion . '%';

                                switch ($subseccion){
                                  case "Azucar blanco":
                                     $input = 'Azucar%';
                                break;
                                  case "Batido de chocolate":
                                     $input = 'Batido chocolate%';
                                break;
                                case "Batido de fresa":
                                     $input = 'Batido fresa%';
                                break;
                                case "Batido de vainilla":
                                     $input = 'Batido vainilla%';
                                break;
                                case "Cafe molido":
                                     $input = 'Cafe molido';
                                break;                                
                                case "Galleta digestive":
                                     $input = 'Galleta digestive';
                                break;                                
                                case "Galleta estilo oreo":
                                     $input = 'Galleta oreo';
                                break;
                                case "Conos":
                                     $input = 'Cono%';
                                break;
                                case "Bombon":
                                     $input = '%Bombon%';
                                break;
                                case "Tarrinas":
                                     $input = 'Tarrina%';
                                break;                                
                                case "Yogures":
                                     $input = 'Yogur%';
                                break;
                                case "Garbanzos":
                                     $input = 'Garbanzo%';
                                break;                                
                                case "Alubias":
                                     $input = 'Alubia%';
                                break;                                
                                case "Lentejas":
                                     $input = 'Lenteja%';
                                break;                                
                                case "Barra pan":
                                     $input = 'Barra de pan%';
                                break;                                
                                case "Pan molde":
                                     $input = 'Pan de molde%';
                                break;                                
                                case "Pizzas":
                                     $input = 'Pizza%';
                                break;                                
                                case "Flanes":
                                     $input = 'Flan%';
                                break;                                
                                case "Gelatinas":
                                     $input = 'Gelatina%';
                                break;
                                case "Champinones":
                                     $input = 'Champinon%';
                                break;                                
                                case "Alcachofas":
                                     $input = 'Alcachofa%';
                                break;                                
                                case "Zumo de naranja":
                                     $input = 'Zumo naranja%';
                                break;
                                case "Zumo de pina":
                                     $input = 'Zumo pina%';
                                break;                                
                                case "Zumo de naranja":
                                     $input = 'Zumo naranja%';
                                break;
                                case "Zumo de pina":
                                     $input = 'Zumo pina%';
                                break;
                                case "Zumo de manzana":
                                     $input = 'Zumo manzana%';
                                break;                                
                                case "Zumo de melocoton":
                                     $input = 'Zumo melocoton%';
                                break;
                                }

                                $stmt->bindParam(':subseccion', $input, PDO::PARAM_STR);
                                $stmt->execute();
                                if ($stmt->rowCount() > 0) {
                                    while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)) {?>
                                
                                <div id="<?php echo $fila["id"]; ?>" class="col-sm-6 col-md-4 product-item animation-element slide-top-left <?php echo $fila["supermercado"]; ?>">
                                <form method="POST" action="anadir_carro.php">
                                <input type="hidden" name="idproducto" value="<?php echo $fila["id"];?>">
                                <div class="product-container <?php switch ($subseccion){
                                    case 'Aceite oliva':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 15)); 
                                    break; 
                                    case 'Aceite girasol':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 17)); 
                                    break;
                                    case 'Batido de chocolate':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 19)); 
                                    break;
                                    case 'Batido de fresa':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 15)); 
                                    break;                                    
                                    case 'Batido de vainilla':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 19)); 
                                    break;
                                    case 'Cafe molido tostado':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 25)); 
                                    break;
                                    case 'Cafe soluble':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 18)); 
                                    break;
                                    case 'Bicarbonato':
                                        echo str_replace(' ', '-', substr($fila["producto"], 0, 18)); 
                                    break;
                                    }?>">
                                    <div class="row" test="<?php echo $subseccion; ?>">
                                        <div class="col-md-12"><a class="product-image" href="#"><img src="<?php echo $fila["imagen"]; ?>"></a></div>
                                    </div>
                                    <div class="row">
                                        <div class="col-8">
                                            <h2><a href="#"><?php echo $fila["producto"];?><?php switch ($fila["producto"]){ 
                                                case 'Muesli':
                                                 echo " solo"; 
                                                break; 
                                                case 'Copos de arroz y trigo':
                                                 echo " solo"; 
                                                break;
                                                case 'Galleta oreo':
                                                 echo "."; 
                                                break; 
                                                case 'Harina de trigo':
                                                 echo "."; 
                                                break;
                                                case 'Leche entera':
                                                 echo "."; 
                                                break;
                                                case 'Leche semidesnatada':
                                                 echo "."; 
                                                break;
                                                case 'Leche desnatada':
                                                 echo "."; 
                                                break;                                                
                                                case 'Yogur griego natural':
                                                 echo "."; 
                                                break;                                                
                                                case 'Garbanzo':
                                                 echo " crudo"; 
                                                break;
                                                case 'Alubia blanca':
                                                 echo "."; 
                                                break;
                                                case 'Alubia pinta':
                                                 echo "."; 
                                                break;                                                
                                                case 'Lenteja':
                                                 echo " cruda 1kg"; 
                                                break;                                                
                                                case 'Pan de molde integral':
                                                 echo "."; 
                                                break;                                                
                                                case 'Macarron espiral':
                                                 echo "."; 
                                                break;
                                    }?></a></h2>
                                        </div>
                                        <div class="col-4"><img src="..\imagenes\supermercados\iconos/<?php echo str_replace(' ', '', strtolower($fila["supermercado"])); ?>.png" style="max-width: 100%;"></div>
                                    </div>
                                    <div class="product-rating"><a class="small-text" ><?php echo $fila["detalle"]; ?><?php echo ' '. $fila["supermercado"]; ?></a></div>
                                    <div class="row">
                                        <div class="col-12">
                                            <p class="product-description" style="height: 40px;"><?php echo $fila["descripcion"]; ?></p>
                                            <div class="row">
                                                <div class="col-6"><a href="<?php echo $fila["enlace"]; ?>" target="_blank" rel="noreferrer"><button class="btn btn-light" type="button">Comprar ahora</button></a></div>
                                                <div class="col-6"><p class="product-price"><?php echo $fila["precio"]; ?>€</p></div>
                                            </div>
                                        </div>
                                        <?php 
                                        if ($_COOKIE["FormularioCookies"] === 'Si') {
                                        ?>
                                        <div class="col-12">
                                            <div class="row">
                                                <div class="col-2"><button class="btn btn-light" type="submit">+</button></div>
                                            </div>
                                        </div><?php
                                                } else {}
                                              ?>
                                    </div>
                                </div>
                            </div>
                            </form>
                                    <?php
                                    }
                                }
                            } catch (PDOException $e) {
                echo 'Error al conectar a la base de datos: ' . $e->getMessage();
            }    
                        }?>
                            <!--
-->
                        </div>
                    </div>
                </div>
            </div>
        </div>


    
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
    <script src="assets/js/Animated-Pretty-Product-List-v12-Animated-Pretty-Product-List.js"></script>

    <footer id="footer" class="text-center bg-dark">
        <div class="container text-white py-4 py-lg-5">
            <ul class="list-inline">
                <li class="list-inline-item me-4"><a class="link-light" href="/CRUD/login.php">Login</a></li>
                <li class="list-inline-item"><a class="link-light" href="privacidad.html">Política de privacidad</a></li>
            </ul>
            <p class="text-muted mb-0">Desarrollado por Rayner Gabú<br>GroceSort<br>©2023&nbsp;</p>
        </div>

    </footer>



    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
var elementosOcultadosPorClase = [];

function ocultarElementosPorClase(clase) {
  var elementos = document.getElementsByClassName(clase);
  for (var i = 0; i < elementos.length; i++) {
    if (elementos[i].style.display === "none") {
      // Muestra el elemento si está oculto
      elementos[i].style.display = "block";
      // Elimina el elemento de la lista de elementos ocultados
      var index = elementosOcultadosPorClase.indexOf(elementos[i]);
      if (index > -1) {
        elementosOcultadosPorClase.splice(index, 1);
      }
    } else {
      elementos[i].style.display = "none";
      elementosOcultadosPorClase.push(elementos[i]);
    }
  }
}


window.onload = function() {
    var checkboxes = ["ahorramascb", "alcampocb", "carrefourcb", "diacb", "eroskicb", "mercadonacb"];
    checkboxes.forEach(function(id) {
        var checkbox = document.getElementById(id);
        checkbox.checked = true; 
    });
};

    function invertirOrden() {
        // Obtiene los elementos con la clase "product-item"
        var productItems = document.getElementsByClassName("product-item");
        // Convierte la colección de elementos en un array
        var productItemsArray = Array.from(productItems);
        // Invierte el orden del array
        productItemsArray.reverse();
        // Elimina los elementos originales del DOM
        for (var i = 0; i < productItems.length; i++) {
            productItems[i].remove();
        }
        // Agrega los elementos en el nuevo orden al DOM
        var container = document.querySelector(".row.product-list");
        for (var i = 0; i < productItemsArray.length; i++) {
            container.appendChild(productItemsArray[i]);
        }
    }
    <?php 
    switch ($subseccion){
        case 'Aceite oliva':?>
    function ocultarBotella1L (){
    var elementos1L = document.getElementsByClassName("Aceite-oliva-1l");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display ==="none"){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
    function ocultarGarrafa5L (){
    var elementos1L = document.getElementsByClassName("Aceite-oliva-5l");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display ==="none"){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}

function ocultarAceite04() {
  // Selecciona todos los elementos h2
  var elementosH2 = document.querySelectorAll("h2 a");
  // Recorre los elementos h2 y verifica si contienen el texto "Aceite oliva 1l 0,4" o "Aceite oliva 5l 0,4"
  elementosH2.forEach(function (elementoH2) {
    var texto = elementoH2.textContent;
    if (texto.includes('Aceite oliva 1l 0,4') || texto.includes('Aceite oliva 5l 0,4')) {
      // Encuentra el elemento "product-item" más cercano al elemento h2
      var productItem = elementoH2.closest(".product-item");
      if (productItem) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
          // No hagas nada si ya está oculto
        } else {
          // Verifica si el elemento está oculto
          if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
          } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
          }
        }
      }
    }
  });
}

function ocultarAceite1() {
  // Selecciona todos los elementos h2
  var elementosH2 = document.querySelectorAll("h2 a");
  // Recorre los elementos h2 y verifica si contienen el texto "Aceite oliva 1l 0,4" o "Aceite oliva 5l 0,4"
  elementosH2.forEach(function (elementoH2) {
    var texto = elementoH2.textContent;
    if (texto.includes('Aceite oliva 1l 1') || texto.includes('Aceite oliva 5l 1')) {
      // Encuentra el elemento "product-item" más cercano al elemento h2
      var productItem = elementoH2.closest(".product-item");
      if (productItem) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
          // No hagas nada si ya está oculto
        } else {
          // Verifica si el elemento está oculto
          if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
          } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
          }
        }
      }
    }
  });
}

     <?php break; ?>
    <?php
        case 'Aceite girasol':?>
                function ocultarBotella1L (){
    var elementos1L = document.getElementsByClassName("Aceite-girasol-1l");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
    function ocultarGarrafa5L (){
    var elementos1L = document.getElementsByClassName("Aceite-girasol-5l");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display ==="none"){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
    <?php
        break;
     case 'Batido de chocolate':?>
    function ocultarBotella1L (){
    var elementos1L = document.getElementsByClassName("Batido-chocolate-1l");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
    function ocultarPack6 (){
    var elementos1L = document.getElementsByClassName("Batido-chocolate-pa");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
     <?php
             break;
     case 'Batido de fresa':?>
    function ocultarBotella1L (){
    var elementos1L = document.getElementsByClassName("Batido-fresa-1l");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
    function ocultarPack6 (){
    var elementos1L = document.getElementsByClassName("Batido-fresa-pa");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
    <?php
        break;
     case 'Batido de vainilla':?>    
     function ocultarBotella1L (){
    var elementos1L = document.getElementsByClassName("Batido-vainilla-1l");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
    function ocultarPack6 (){
    var elementos1L = document.getElementsByClassName("Batido-vainilla-pac");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}    
    <?php
        break;     
        case 'Cafe molido tostado':?>    
     function ocultarCafeTostadoNormal (){
    var elementos1L = document.getElementsByClassName("Cafe-molido-tostado");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
    function ocultarCafeTostadoDescafeinado (){
    var elementos1L = document.getElementsByClassName("Cafe-molido-tostado-desca");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}    
    <?php
        break;
        case 'Cafe soluble':?>    
     function ocultarCafeSolubleNormal (){
    var elementos1L = document.getElementsByClassName("Cafe-soluble");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
    function ocultarCafeSolubleDescafeinado (){
    var elementos1L = document.getElementsByClassName("Cafe-soluble-desca");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}    
    <?php
        break;        
        case 'Muesli':?>    
var elementosOcultadosPorClase = [];

function ocultarMuesli(textoBuscado) {
  // Selecciona todos los elementos con la clase "product-item"
  var elementosProductItem = document.querySelectorAll(".product-item");

  // Recorre los elementos "product-item" y verifica si contienen el texto buscado
  elementosProductItem.forEach(function (productItem) {
    var h2 = productItem.querySelector("h2 a");
    var texto = h2.textContent;
    if (texto.includes(textoBuscado)) {
      // Verifica si el elemento está en la lista de elementos ocultados por clase
      if (elementosOcultadosPorClase.includes(productItem)) {
        // No hagas nada si ya está oculto
      } else {
        // Verifica si el elemento está oculto
        if (productItem.style.display === "none") {
          // Muestra el elemento
          productItem.style.display = "block";
        } else {
          // Oculta el elemento si no está oculto
          productItem.style.display = "none";
        }
      }
    }
  });
}

function ocultarMuesliNormal() {
  ocultarMuesli('Muesli solo');
}

function ocultarMuesliFruta() {
  ocultarMuesli('Muesli con frutas');
}

function ocultarMuesliFrutosSecos() {
  ocultarMuesli('Muesli con frutos secos');
}

function ocultarMuesliChocolate() {
  ocultarMuesli('Muesli con chocolate');
}
 
    <?php
        break;        
        case 'Copos de arroz y trigo':?>    
    var elementosOcultadosPorClase = [];

    function ocultarCoposArroz(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarCoposArrozNormal() {
    ocultarCoposArroz('Copos de arroz y trigo solo');
    }

    function ocultarCoposArrozFrutosRojos() {
    ocultarCoposArroz('Copos de arroz y trigo integral con frutos rojos');
    } 
    <?php
        break;        
    case 'Galleta estilo oreo':?>    
    var elementosOcultadosPorClase = [];

    function ocultarOreo(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarOreoNormal() {
    ocultarOreo('Galleta oreo.');
    }

    function ocultarOreoChocoBlanco() {
    ocultarOreo('Galleta oreo cubierta de chocolate blanco');
    } 
    <?php
        break;      
        case 'Harina de trigo':?>    
    var elementosOcultadosPorClase = [];

    function ocultarHarinaTrigo(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarHarinaTrigoNormal() {
    ocultarHarinaTrigo('Harina de trigo.');
    }

    function ocultarHarinaTrigoIntegral() {
    ocultarHarinaTrigo('Harina de trigo integral');
    } 
    <?php
        break;        
    case 'Conos':?>    
    var elementosOcultadosPorClase = [];

    function ocultarConos(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarNataFresa() {
    ocultarConos('Cono nata y fresa');
    }
    function ocultarNataTrufa() {
    ocultarConos('Cono nata y trufa');
    }
    function ocultarNataTurron() {
    ocultarConos('Cono nata y turron');
    }    
    function ocultarTartaQueso() {
    ocultarConos('Cono tarta de queso');
    }
   function ocultarVainillaChocolate() {
    ocultarConos('Cono vainilla y chocolate');
    } 
    <?php
        break;    
    case 'Bombon':?>    
    var elementosOcultadosPorClase = [];

    function ocultarBombon(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarBombonAlmendra() {
    ocultarBombon('Helado bombon almendra');
    }
    function ocultarBombonAvellana() {
    ocultarBombon('Helado bombon avellanas');
    }
    function ocultarBombonChocolateBlanco() {
    ocultarBombon('Helado bombon chocolate blanco');
    }    
    function ocultarBombonChocolateNata() {
    ocultarBombon('Helado bombon chocolate y nata');
    }
   function ocultarBombonChocolateTriple() {
    ocultarBombon('Helado bombon 3 chocolates');
    } 
    <?php
        break;     
    case 'Tarrinas':?>    
    var elementosOcultadosPorClase = [];

    function ocultarTarrina(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarTarrinaChocolate() {
    ocultarTarrina('Tarrina chocolate y trozos');
    }
    function ocultarTarrinaChocolateTriple() {
    ocultarTarrina('Tarrina tres chocolates');
    }
    function ocultarTarrinaFrutasBosque() {
    ocultarTarrina('Tarrina frutas del bosque');
    }    
    function ocultarTarrinaLimon() {
    ocultarTarrina('Tarrina sorbete limon');
    }
    function ocultarTarrinaNataNueces() {
    ocultarTarrina('Tarrina nata y nueces');
    }
    function ocultarTarrinaStracciatella() {
    ocultarTarrina('Tarrina helado stracciatella');
    }
    function ocultarTarrinaTurron() {
    ocultarTarrina('Tarrina helado turron');
    }
    function ocultarTarrinaVainilla() {
    ocultarTarrina('Tarrina helado vainilla');
    } 
    <?php
        break;    
    case 'Docena Huevo':?>    
    var elementosOcultadosPorClase = [];

    function ocultarHuevo(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarDocenaL() {
    ocultarHuevo('Docena huevo l');
    }
    function ocultarDocenaM() {
    ocultarHuevo('Docena huevo m');
    }
    function ocultarDocenaXL() {
    ocultarHuevo('Docena huevo xl');
    }     
    <?php
        break;     
    case 'Leche':?>    
    var elementosOcultadosPorClase = [];

    function ocultarLeche(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarLecheDesnatada() {
    ocultarLeche('Leche desnatada.');
    }
    function ocultarLecheDesnatadaSL() {
    ocultarLeche('Leche desnatada sin lactosa');
    }
    function ocultarLecheEntera() {
    ocultarLeche('Leche entera.');
    }    
    function ocultarLecheEnteraSL() {
    ocultarLeche('Leche entera sin lactosa');
    }
    function ocultarLecheSemidesnatada() {
    ocultarLeche('Leche semidesnatada.');
    } 
    function ocultarLecheSemidesnatadaSL() {
    ocultarLeche('Leche semidesnatada sin lactosa');
    }     
    <?php
        break;    
    case 'Yogures':?>    
    var elementosOcultadosPorClase = [];

function ocultarYogur(textoBuscado) {
  // Selecciona todos los elementos con la clase "product-item"
  var elementosProductItem = document.querySelectorAll(".product-item");

  // Recorre los elementos "product-item" y verifica si contienen el texto buscado
  elementosProductItem.forEach(function (productItem) {
    var h2 = productItem.querySelector("h2 a");
    var texto = h2.textContent;
    // Verifica si el texto coincide con el texto buscado
    if (texto === textoBuscado) {
      // Verifica si el elemento está en la lista de elementos ocultados por clase
      if (elementosOcultadosPorClase.includes(productItem)) {
        // No hagas nada si ya está oculto
      } else {
        // Verifica si el elemento está oculto
        if (productItem.style.display === "none") {
          // Muestra el elemento
          productItem.style.display = "block";
        } else {
          // Oculta el elemento si no está oculto
          productItem.style.display = "none";
        }
      }
    }
  });
}

function ocultarYogurBote1kg() {
  ocultarYogur('Yogur griego natural 1kg');
}

function ocultarYogurPacks() {
  // Selecciona todos los elementos con la clase "product-item"
  var elementosProductItem = document.querySelectorAll(".product-item");

  // Recorre los elementos "product-item" y oculta aquellos que no coinciden con el texto buscado
  elementosProductItem.forEach(function (productItem) {
    var h2 = productItem.querySelector("h2 a");
    var texto = h2.textContent;
    // Verifica si el texto no coincide con el texto buscado
    if (texto !== 'Yogur griego natural 1kg') {
      // Verifica si el elemento está en la lista de elementos ocultados por clase
      if (elementosOcultadosPorClase.includes(productItem)) {
        // No hagas nada si ya está oculto
      } else {
        // Verifica si el elemento está oculto
        if (productItem.style.display === "none") {
          // Muestra el elemento
          productItem.style.display = "block";
        } else {
          // Oculta el elemento si no está oculto
          productItem.style.display = "none";
        }
      }
    }
  });
}

//
function ocultarYogurSabor(textosBuscados) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen alguno de los textos buscados
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;

        // Verifica si al menos uno de los textos buscados está contenido en el elemento
        if (textosBuscados.some(busqueda => texto.includes(busqueda))) {
            // Verifica si el elemento está en la lista de elementos ocultados por clase
            if (elementosOcultadosPorClase.includes(productItem)) {
                // No hagas nada si ya está oculto
            } else {
                // Verifica si el elemento está oculto
                if (productItem.style.display === "none") {
                    // Muestra el elemento
                    productItem.style.display = "block";
                } else {
                    // Oculta el elemento si no está oculto
                    productItem.style.display = "none";
                }
            }
        }
    });
}

function ocultarYogurNatural() {
    ocultarYogurSabor(['Yogur natural']);
}

function ocultarYogurNaturalAzucar() {
    ocultarYogurSabor(['Yogur griego natural con azucar']);
}

function ocultarYogurNaturalGriego() {
    ocultarYogurSabor(['Yogur griego natural.', 'Yogur griego natural 1kg']);
}

function ocultarYogurSabores() {
    ocultarYogurSabor(['Yogur sabores']);
}

    <?php
        break;    
    case 'Garbanzos':?>    
    var elementosOcultadosPorClase = [];

    function ocultarGarbanzos(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarGarbanzoCocido() {
    ocultarGarbanzos('Garbanzo cocido');
    }
    function ocultarGarbanzoCrudo() {
    ocultarGarbanzos('Garbanzo crudo');
    }  
    <?php
        break;    
    case 'Alubias':?>    
function ocultarAlubias(textosBuscados) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen alguno de los textos buscados
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;

        // Verifica si al menos uno de los textos buscados está contenido en el elemento
        if (textosBuscados.some(busqueda => texto.includes(busqueda))) {
            // Verifica si el elemento está en la lista de elementos ocultados por clase
            if (elementosOcultadosPorClase.includes(productItem)) {
                // No hagas nada si ya está oculto
            } else {
                // Verifica si el elemento está oculto
                if (productItem.style.display === "none") {
                    // Muestra el elemento
                    productItem.style.display = "block";
                } else {
                    // Oculta el elemento si no está oculto
                    productItem.style.display = "none";
                }
            }
        }
    });
}

function ocultarAlubiaCocida() {
    ocultarAlubias(['Alubia pinta cocida', 'Alubia blanca cocida']);
}

function ocultarAlubiaCrudo() {
    ocultarAlubias(['Alubia blanca.', 'Alubia pinta.']);
}

function ocultarAlubiaBlanca() {
    ocultarAlubias(['Alubia blanca.', 'Alubia blanca cocida']);
}

function ocultarAlubiaPinta() {
    ocultarAlubias(['Alubia pinta cocida', 'Alubia pinta.']);
}
    <?php
        break;    
    case 'Lentejas':?>    
function ocultarLentejas(textosBuscados) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen alguno de los textos buscados
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;

        // Verifica si al menos uno de los textos buscados está contenido en el elemento
        if (textosBuscados.some(busqueda => texto.includes(busqueda))) {
            // Verifica si el elemento está en la lista de elementos ocultados por clase
            if (elementosOcultadosPorClase.includes(productItem)) {
                // No hagas nada si ya está oculto
            } else {
                // Verifica si el elemento está oculto
                if (productItem.style.display === "none") {
                    // Muestra el elemento
                    productItem.style.display = "block";
                } else {
                    // Oculta el elemento si no está oculto
                    productItem.style.display = "none";
                }
            }
        }
    });
}

function ocultarLentejaCocida() {
    ocultarLentejas(['Lenteja cocida']);
}

function ocultarLentejaCrudo() {
    ocultarLentejas(['Lenteja cruda 1kg']);
}

    <?php
        break;     
    case 'Miel':?> 
    var elementosOcultadosPorClase = [];   
function ocultarMiel(textosBuscados) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen alguno de los textos buscados
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;

        // Verifica si al menos uno de los textos buscados está contenido en el elemento
        if (textosBuscados.some(busqueda => texto.includes(busqueda))) {
            // Verifica si el elemento está en la lista de elementos ocultados por clase
            if (elementosOcultadosPorClase.includes(productItem)) {
                // No hagas nada si ya está oculto
            } else {
                // Verifica si el elemento está oculto
                if (productItem.style.display === "none") {
                    // Muestra el elemento
                    productItem.style.display = "block";
                } else {
                    // Oculta el elemento si no está oculto
                    productItem.style.display = "none";
                }
            }
        }
    });
}

function ocultarMielAzahar() {
    ocultarMiel(['Miel de azahar']);
}

function ocultarMielFlores() {
    ocultarMiel(['Miel de flores 1kg']);
}

    <?php
        break;    
    case 'Pan molde':?>    
    var elementosOcultadosPorClase = [];

    function ocultarPanMolde(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarMoldeIntegral() {
    ocultarPanMolde('Pan de molde integral.');
    }
    function ocultarMoldeBlancoSinCorteza() {
    ocultarPanMolde('Pan de molde blanco sin corteza');
    }
    function ocultarMoldeBlancoFamiliar() {
    ocultarPanMolde('Pan de molde blanco familiar');
    }    
    function ocultarMoldeIntegralSinCorteza() {
    ocultarPanMolde('Pan de molde integral sin corteza');
    }

    <?php
        break;     
    case 'Macarron espiral':?>    
    var elementosOcultadosPorClase = [];

    function ocultarMacarronEspiral(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h2 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            productItem.style.display = "block";
            } else {
            // Oculta el elemento si no está oculto
            productItem.style.display = "none";
            }
        }
        }
    });
    }

    function ocultarEspiralBlanco() {
    ocultarMacarronEspiral('Macarron espiral.');
    }
    function ocultarEspiralVegetales() {
    ocultarMacarronEspiral('Macarron espiral vegetal');
    }


    <?php
        break;       
    case 'Bicarbonato':?>
    function ocultarBotes (){
    var elementos1L = document.getElementsByClassName("Bicarbonato-bote");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}
     function ocultarPaquete1kg (){
    var elementos1L = document.getElementsByClassName("Bicarbonato-1kg");
    for (var i = 0; i < elementos1L.length; i++) {
        if(elementos1L[i].style.display  ==="none" ){
            elementos1L[i].style.display = "block";
        } else{
            elementos1L[i].style.display = "none";
            }
    }
}    
    <?php
        break;
    }?>


    </script>
</body>
</html>