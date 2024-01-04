
<!DOCTYPE html>
<!--Vista precio test-->
<html data-bs-theme="light" lang="es">

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
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <style>
        .oculto {
            display: none;
        }
                    .col-2 button:hover {
                background-color: green;
            }
    </style>
<link rel="icon" href="https://cdn.discordapp.com/attachments/1166363443637518346/1181710546878337146/GS_Logo.png?ex=65820cb5&is=656f97b5&hm=ed861c8c0bc3f030314a66d50da7e1cd14a9f4f97917927f63252dc64379481f&">
    <meta name="google-adsense-account" content="ca-pub-8360200834189110">
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
    <div class="modal fade" id="ModalPrecio" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Historial de precios</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
      </div>
    </div>
  </div>
</div>
        <div class="container-fluid">
            <div class="row py-1 py-md-1">
                <div class="col-12 col-sm-3 col-lg-2">
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
                                    case 'Aceite de coco':
                                    case 'Agua':
                                    case 'Arroz largo':
                                    case 'Arroz redondo':
                                    case 'Arroz vaporizado':
                                    case 'Arroz basmati':
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
                                    case 'Cafe molido tostado descafeinado':
                                    case 'Cafe expreso descafeinado':
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
                                    case 'Macarron pajarita vegetal':
                                    case 'Flanes':
                                    case 'Gelatinas':
                                    case 'Natillas':
                                    case 'Mousse chocolate':
                                    case 'Sal mesa':
                                    case 'Sal gorda':
                                    case 'Sal rosa':
                                    case 'Ketchup':
                                    case 'Mostaza':
                                    case 'Mayonesa':
                                    case 'Vinagre vino blanco':
                                    case 'Vinagre manzana':
                                    case 'Vinagre balsamico modena':
                                    case 'Vinagre jerez':?>
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
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Garrafas</label>
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
            case 'Atun':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAtunClaro" onclick="ocultarAtunClaro()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Claro </label>
                                        </div>
                                        </li>                                     
                                      <li>                                       
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAtunAceiteOliva" onclick="ocultarAtunAceiteOliva()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Claro en aceite oliva </label>
                                        </div>
                                        </li>                                     
                                      <li>                                      
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAtunAceiteGirasol" onclick="ocultarAtunAceiteGirasol()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Claro en aceite girasol </label>
                                        </div>
                                        </li>                                     
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarAtunEscabeche" onclick="ocultarAtunEscabeche()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Claro en escabeche</label>
                                        </div>
                                        </li>
                                      
                                    <li>
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;            
            case 'Bonito':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarBonitoAceiteOliva" onclick="ocultarBonitoAceiteOliva()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> En aceite de oliva </label>
                                        </div>
                                        </li>                                     
                                      <li>                                       
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarBonitoEscabeche" onclick="ocultarBonitoEscabeche()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> En escabeche </label>
                                        </div>
                                        </li>                                     
                                      <li>                                      
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Mejillones':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarMejillon" onclick="ocultarMejillon()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Al natural </label>
                                        </div>
                                        </li>                                     
                                      <li>                                       
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarMejillonSalsa" onclick="ocultarMejillonSalsa()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> En salsa vieira </label>
                                        </div>
                                        </li>                                     
                                      <li>                                      
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Sardinas':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarSardinasEnTomate" onclick="ocultarSardinasEnTomate()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> En tomate </label>
                                        </div>
                                        </li>                                     
                                      <li>                                       
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarSardinasEnTomate" onclick="ocultarSardinasEscabeche()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> En escabeche </label>
                                        </div>
                                        </li>
                                        <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarSardinasPicantonas" onclick="ocultarSardinasPicantonas()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Picantonas </label>
                                        </div>
                                        </li>
                                        <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarSardinasAceiteOliva" onclick="ocultarSardinasAceiteOliva()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> En aceite oliva </label>
                                        </div>
                                        </li>
                                        <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarSardinasLimon" onclick="ocultarSardinasLimon()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Con limon </label>
                                        </div>
                                        </li>                                      
                                      <li>                                      
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Tortilla patata':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTortillaSinCebolla" onclick="ocultarTortillaSinCebolla()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Sin cebolla </label>
                                        </div>
                                        </li>                                     
                                                                             
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarTortillaConCebolla" onclick="ocultarTortillaConCebolla()"  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Con cebolla </label>
                                        </div>
                                        </li>                                     
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Pizzas':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPizza4Quesos" onclick="ocultarPizza4Quesos()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> 4 quesos </label>
                                            </div>
                                        </li>

                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPizzaJamonQueso" onclick="ocultarPizzaJamonQueso()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Jamon y queso </label>
                                            </div>
                                        </li>

                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPizzaBarbacoa" onclick="ocultarPizzaBarbacoa()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaBarbacoa"> Barbacoa </label>
                                            </div>
                                        </li>

                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPizzaPolloyBacon" onclick="ocultarPizzaPolloyBacon()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaPolloyBacon"> Pollo y bacon </label>
                                            </div>
                                        </li>                                    
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Cuajada':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarCuajada" onclick="ocultarCuajada()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Natural </label>
                                            </div>
                                        </li>

                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarCuajadaAzucar" onclick="ocultarCuajadaAzucar()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Con Azúcar </label>
                                            </div>
                                        </li>                                   
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Patatas fritas':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPatatasPaja" onclick="ocultarPatatasPaja()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Patatas fritas paja </label>
                                            </div>
                                        </li>

                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPatatasChurreria" onclick="ocultarPatatasChurreria()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Patatas fritas churreria </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPatatasLisas" onclick="ocultarPatatasLisas()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Patatas fritas lisas </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPatatasArtesanales" onclick="ocultarPatatasArtesanales()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Patatas fritas artesanales </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPatatasCongeladasFino" onclick="ocultarPatatasCongeladasFino()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Congeladas corte fino </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPatatasCongeladasTradicional" onclick="ocultarPatatasCongeladasTradicional()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Congeladas corte tradicional </label>
                                            </div>
                                        </li>                                    
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Aceitunas':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarAceitunaNegraSinHueso" onclick="ocultarAceitunaNegraSinHueso()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Aceituna negra sin hueso </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarAceitunaNegraConHueso" onclick="ocultarAceitunaNegraConHueso()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Aceituna negra con hueso </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarAceitunaVerdeSinHueso" onclick="ocultarAceitunaVerdeSinHueso()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Aceituna verde sin hueso </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarAceitunaVerdeConHueso" onclick="ocultarAceitunaVerdeConHueso()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Aceituna verde con hueso </label>
                                            </div>
                                        </li>                                    
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Galletas saladas':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarGalletasSaladasPaquete" onclick="ocultarGalletaSaladaPaquete()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Paquete </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarGalletaSaladaBote" onclick="ocultarGalletaSaladaBote()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Bote </label>
                                            </div>
                                        </li>
                                 
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Palomitas':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPalomitasMantequilla" onclick="ocultarPalomitasMantequilla()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Mantequilla bolsa </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPalomitasMicroondasSal" onclick="ocultarPalomitasMicroondasSal()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Microondas sal pack </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPalomitasMicroondasMantequilla" onclick="ocultarPalomitasMicroondasMantequilla()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Microondas mantequilla pack </label>
                                            </div>
                                        </li>
                                 
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Tomate':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarTomateTriturado400g" onclick="ocultarTomateTriturado400g()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Triturado 400g </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarTomateTriturado800g" onclick="ocultarTomateTriturado800g()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Triturado 800g </label>
                                            </div>
                                        </li>
                                        
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarTomateFritoBote" onclick="ocultarTomateFritoBote()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Frito bote </label>
                                            </div>
                                        </li>

                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarTomateFritoPack" onclick="ocultarTomateFritoPack()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Frito pack </label>
                                            </div>
                                        </li>

                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarTomateFrito" onclick="ocultarTomateFritoSarten()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Frito en sarten </label>
                                            </div>
                                        </li>

                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarTomateFritoCaseroAceite" onclick="ocultarTomateFritoCaseroAceite()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Frito casero aceite oliva </label>
                                            </div>
                                        </li>
                                 
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Judias verdes':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarJudiasVerdesAnchasConserva" onclick="ocultarJudiasVerdesAnchasConserva()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Verdes anchas en conserva </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarJudiasVerdesRedondasConserva" onclick="ocultarJudiasVerdesRedondasConserva()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Verdes redondas en conserva </label>
                                            </div>
                                        </li>
                                        
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarJudiasVerdesRedondasCongeladas" onclick="ocultarJudiasVerdesRedondasCongeladas()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Verdes redondas congeladas </label>
                                            </div>
                                        </li>

                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarJudiasVerdesAnchasCongeladas" onclick="ocultarJudiasVerdesAnchasCongeladas()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Verdes anchas congeladas </label>
                                            </div>
                                        </li>
                                 
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Pimientos':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPimientosPiquilloEnTiras" onclick="ocultarPimientosPiquilloEnTiras()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Piquillo en tiras </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarPimientosPiquilloEntero" onclick="ocultarPimientosPiquilloEntero()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Piquillo enteros </label>
                                            </div>
                                        </li>
                                 
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Esparragos':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarEsparragoBlanco" onclick="ocultarEsparragoBlanco()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Blancos </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarEsparragoVerde" onclick="ocultarEsparragoVerde()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Verdes </label>
                                            </div>
                                        </li>
                                 
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Maiz':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarMaizDulceCongelado" onclick="ocultarMaizDulceCongelado()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Congelado </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarMaizDulceLata" onclick="ocultarMaizDulceLata()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> En lata </label>
                                            </div>
                                        </li>
                                 
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Champinones':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarChampinonesLaminados" onclick="ocultarChampinonesLaminados()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Laminados </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarChampinonesEnteros" onclick="ocultarChampinonesEnteros()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Enteros </label>
                                            </div>
                                        </li>
                                 
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Alcachofas':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarAlcachofaBaby" onclick="ocultarAlcachofaBaby()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Baby </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarAlcachofaNormal" onclick="ocultarAlcachofaNormal()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Normales </label>
                                            </div>
                                        </li>
                                 
                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                    <?php
            break;
            case 'Guisantes':?>
                                    <ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarGuisantesFinosLata" onclick="ocultarGuisantesFinosLata()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaSinCebolla"> Muy finos lata </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarGuisantesMuyFinosBote" onclick="ocultarGuisantesMuyFinosBote()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Muy finos bote </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarGuisantesMuyFinosCongelados" onclick="ocultarGuisantesMuyFinosCongelados()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Muy finos congelados </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarGuisantesFinosCongelados" onclick="ocultarGuisantesFinosCongelados()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Finos congelados </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarGuisantesFinosBote" onclick="ocultarGuisantesFinosBote()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Finos bote </label>
                                            </div>
                                        </li>
                                        <li>
                                            <div class="form-check">
                                                <input class="form-check-input ms-1" type="checkbox" value="" id="cbocultarGuisantesMedianosLata" onclick="ocultarGuisantesMedianosLata()" checked>
                                                <label class="form-check-label ms-1" for="cbocultarTortillaConCebolla"> Medianos lata </label>
                                            </div>
                                        </li>
                                 
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
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbAceite04" onclick='ocultarAceiteOV();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Aceite oliva virgen</label>
                                        </div>
                                      </li>

                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbAceite04" onclick='ocultarAceiteOVE();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Aceite oliva virgen extra</label>
                                        </div>
                                        </li>
                                      <li>                                      
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
        break;
    case 'Flanes':?>
    <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-capsule" viewBox="0 0 16 16">
  <path d="M1.828 8.9 8.9 1.827a4 4 0 1 1 5.657 5.657l-7.07 7.071A4 4 0 1 1 1.827 8.9Zm9.128.771 2.893-2.893a3 3 0 1 0-4.243-4.242L6.713 5.429l4.243 4.242Z"/>
</svg>

    <span class="ms-1 d-none d-sm-inline">Sabor</span>
</a>
<ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarFlanVainilla" onclick='ocultarFlanVainilla();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Vainilla</label>
                                        </div>
                                      </li>
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarFlanHuevo" onclick='ocultarFlanHuevo();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Huevo</label>
                                        </div>
                                     </li>                                      
                                        

                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                                 <?php  
        break;
    case 'Gelatinas':?>
    <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-capsule" viewBox="0 0 16 16">
  <path d="M1.828 8.9 8.9 1.827a4 4 0 1 1 5.657 5.657l-7.07 7.071A4 4 0 1 1 1.827 8.9Zm9.128.771 2.893-2.893a3 3 0 1 0-4.243-4.242L6.713 5.429l4.243 4.242Z"/>
</svg>

    <span class="ms-1 d-none d-sm-inline">Sabor</span>
</a>
<ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarGelatinaSabores" onclick='ocultarGelatinaSabores();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Sabores</label>
                                        </div>
                                      </li>
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarGelatinaSaboresLight" onclick='ocultarGelatinaSaboresLight();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Sabores light</label>
                                        </div>
                                     </li>
                                     <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarGelatinaFresa" onclick='ocultarGelatinaFresa();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Fresa</label>
                                        </div>
                                     </li>                                      
                                        

                                        <hr class="dropdown-divider">
                                    </li>
                                </ul>
                            </li>
                                 <?php  
        break;
        case 'Natillas':?>
    <li class="dropdown w-100"><a id="dropdown" class="dropdown-toggle px-1 nav-link px-sm-0 ps-2" href="#" data-bs-toggle="dropdown" aria-expanded="false">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-capsule" viewBox="0 0 16 16">
  <path d="M1.828 8.9 8.9 1.827a4 4 0 1 1 5.657 5.657l-7.07 7.071A4 4 0 1 1 1.827 8.9Zm9.128.771 2.893-2.893a3 3 0 1 0-4.243-4.242L6.713 5.429l4.243 4.242Z"/>
</svg>

    <span class="ms-1 d-none d-sm-inline">Sabor</span>
</a>
<ul class="dropdown-menu dropdown-menu-light text-small shadow" aria-labelledby="dropdown">
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarNatillasVainilla" onclick='ocultarNatillasVainilla();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Vainilla</label>
                                        </div>
                                      </li>
                                      <li>
                                        <div class="form-check">
                                          <input class="form-check-input ms-1"  type="checkbox" value="" id="cbocultarNatillasChoco" onclick='ocultarNatillasChoco();'  checked>
                                          <label class="form-check-label ms-1" for="flexCheckChecked"> Chocolate</label>
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
                        <!--
                        <div class="input-group d-none d-md-flex mt-3"><input class="form-control" type="text" placeholder="Search..."><button class="btn btn-primary" type="button"><i class="fa fa-search"></i></button></div>
                        -->
                    </div>
                    <!---->
                    
                        <section class="anuncios" style="display: none;">
                            <br>
                            <h4>Otras secciones</h4>
                            <div class="d-flex flex-sm-column flex-row flex-grow-1 align-items-center align-items-sm-start px-3 text-white" style=" padding: 10px 5px 5px 5px ;border-radius: 10px;  background-color: rgb(233, 233, 233);">
                                <ul id="menu2" class="nav nav-pills flex-sm-column flex-row flex-nowrap flex-shrink-1 flex-sm-grow-0 flex-grow-1 my-3 mb-sm-auto justify-content-center align-items-center align-items-sm-start w-100">

                                    <a href="https://www.raynergrocesort.rf.gd/paginas/paginas/vistaPrecioTest.php?nombre_subseccion=Aceite%20girasol"><li class="text-black ps-3">Aceite oliva</li></a>

                                    <li class="text-black ps-3">Test</li>
                                    
                            </div>
                        </section>
                    <!---->
                </div>

                <div class="col-12 col-sm-9 col-sm-9">
                    <div class="container">
                    
                        <div id="elementosMostrados" class="row product-list dev">
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
                                        //echo str_replace(' ', '-', substr($fila["producto"], 0, 15));
                                        //echo ($fila["producto"] === "Aceite oliva virgen 1L") ? "AOV1L" : str_replace(' ', '-', substr($fila["producto"], 0, 15));
                                        echo ($fila["producto"] === "Aceite oliva virgen 1L") ? "AOV1L Aceite-oliva-1l" :
                                        (($fila["producto"] === "Aceite oliva virgen 3L") ? "AOV3L Aceite-oliva-5l" :
                                        (($fila["producto"] === "Aceite oliva virgen 5L") ? "AOV5L Aceite-oliva-5l" :
                                        (($fila["producto"] === "Aceite oliva virgen extra 1L") ? "AOVE1L Aceite-oliva-1l" :
                                        (($fila["producto"] === "Aceite oliva virgen extra 3L") ? "AOVE3L Aceite-oliva-5l" :
                                        (($fila["producto"] === "Aceite oliva virgen extra 5L") ? "AOVE5L Aceite-oliva-5l" :
                                        str_replace(' ', '-', substr($fila["producto"], 0, 15)))))));
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
                                        <div class="col-md-12"><a class="product-image" ><img src="<?php echo $fila["imagen"]; ?>"></a></div>
                                    </div>
                                    <div class="row">
                                        <div class="col-8">
                                        <style>
                                        @media (min-width: 0px) and (max-width: 575px) {
                                            #nombreeProductoH3{
                                            height: 30px;
                                            }
                                        }
                                        @media (min-width: 768px) and (max-width: 1199px) {
                                            #nombreeProductoH3{
                                            height: 70px;
                                            }
                                        }
                                        @media (min-width: 1200px) and (max-width: 2160px) {
                                            #nombreeProductoH3{
                                            height: 30px;
                                            }
                                        }
                                        </style>
                                            <h3 id="nombreeProductoH3" style ="font-size: 18px; font-weight: 800;" ><a class="ModalTrigger" id="nombreeProducto"
                                            style="cursor: pointer; color: inherit; text-decoration: none;"><?php echo $fila["producto"];?><?php switch                                                   ($fila["producto"]){ 
                                                case 'Aceite oliva 1l 1':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva 3l 1':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva 5l 1':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva 1l 0,4':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva 3l 0,4':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva 5l 0,4':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva virgen 1L':
                                                 echo ".";
                                                break;
                                                case 'Aceite oliva virgen 3L':
                                                 echo ".";
                                                break;
                                                case 'Aceite oliva virgen 5L':
                                                 echo ".";
                                                break;
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
                                                case 'Cafe molido tostado':
                                                 echo ".";
                                                break;
                                                case 'Cafe soluble':
                                                 echo ".";
                                                break;
                                                case 'Atun claro':
                                                 echo ".";
                                                break;                                                
                                                case 'Tortilla patata':
                                                 echo " sin cebolla";
                                                break;
                                                case 'Cuajada':
                                                 echo " natural";
                                                break;
                                                case 'Gelatina sabores':
                                                 echo ".";
                                                break;
                                                case 'Natillas':
                                                 echo " vainilla";
                                                break;
                                                case 'Maiz dulce':
                                                 echo " lata";
                                                break;                                                
                                                case 'Guisantes muy finos':
                                                 echo " lata";
                                                break;
                                                case 'Guisantes finos':
                                                 echo " bote";
                                                break;
                                                case 'Guisantes medianos':
                                                 echo " lata";
                                                break;
                                                

                                    }?></a></h3>
                                        </div>
                                        <div class="col-4"><img src="..\imagenes\supermercados\iconos/<?php echo str_replace(' ', '', strtolower($fila["supermercado"])); ?>.png" style="max-width: 100%;"></div>
                                    </div>

                                    <div class="product-rating d-block d-sm-none d-md-none d-lg-none d-xl-none d-xxl-block"><a class="small-text" ><?php echo $fila["detalle"]; ?><?php echo ' '. $fila["supermercado"]; ?></a></div>
                                    <div class="row">
                                        <div class="col-12">
                                        <style>
                                        @media (min-width: 576px) and (max-width: 935px) {
                                            .product-description {
                                            padding-top: -30px;
                                            padding-bottom: 80px;
                                            }
                                        }
                                        </style>
                                            <p class="product-description pt-0 pt-sm-1 pt-xl-0" style="height: 40px;"><?php echo $fila["descripcion"]; ?></p>
                                            <div class="row">
                                                <div class="col-6 col-sm-8"><a href="<?php echo $fila["enlace"]; ?>" target="_blank" rel="noreferrer"><button class="btn btn-light" type="button">Comprar ahora</button></a></div>
                                                <div class="col-6 col-sm-4"><p class="product-price ModalTrigger" style="cursor: pointer;"><?php echo $fila["precio"]; ?>€</p></div>
                                            </div>
                                        </div>
                                        <?php 
                                        if ($_COOKIE["FormularioCookies"] === 'Si') {
                                        ?>
                                        <div class="col-12 pt-1">

                                        <style>
                                            @media (min-width: 0px) and (max-width: 575px) {
                                                .anadirLista {
                                                width: 136px;
                                                }
                                            }
                                            @media (min-width: 1200px) and (max-width: 2160px) {
                                                .anadirLista {
                                                width: 136px;
                                                }
                                            }
                                            </style>


                                        <div class="row">
                                            <div class="col-6 col-sm-8">
                                                <button id="tttest" class="btn btn-light anadirLista" onclick="showAddedToCart()" type="submit">Añadir a lista</button>
                                            </div>
                                            <div class="col-6 col-sm-4 d-flex justify-content-end">
                                                <button class="btn btn-light ModalTrigger" id="botonModal" type="button"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clock-history" viewBox="0 0 16 16">
  <path d="M8.515 1.019A7 7 0 0 0 8 1V0a8 8 0 0 1 .589.022zm2.004.45a7 7 0 0 0-.985-.299l.219-.976q.576.129 1.126.342zm1.37.71a7 7 0 0 0-.439-.27l.493-.87a8 8 0 0 1 .979.654l-.615.789a7 7 0 0 0-.418-.302zm1.834 1.79a7 7 0 0 0-.653-.796l.724-.69q.406.429.747.91zm.744 1.352a7 7 0 0 0-.214-.468l.893-.45a8 8 0 0 1 .45 1.088l-.95.313a7 7 0 0 0-.179-.483m.53 2.507a7 7 0 0 0-.1-1.025l.985-.17q.1.58.116 1.17zm-.131 1.538q.05-.254.081-.51l.993.123a8 8 0 0 1-.23 1.155l-.964-.267q.069-.247.12-.501m-.952 2.379q.276-.436.486-.908l.914.405q-.24.54-.555 1.038zm-.964 1.205q.183-.183.35-.378l.758.653a8 8 0 0 1-.401.432z"/>
  <path d="M8 1a7 7 0 1 0 4.95 11.95l.707.707A8.001 8.001 0 1 1 8 0z"/>
  <path d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5"/>
</svg></button>
                                                <!--<p class="product-price ModalTrigger" style="cursor: pointer;">Historial</p>-->
                                            </div>
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
                                        //echo str_replace(' ', '-', substr($fila["producto"], 0, 15));
                                        //echo ($fila["producto"] === "Aceite oliva virgen 1L") ? "AOV1L" : str_replace(' ', '-', substr($fila["producto"], 0, 15));
                                        echo ($fila["producto"] === "Aceite oliva virgen 1L") ? "AOV1L Aceite-oliva-1l" :
                                        (($fila["producto"] === "Aceite oliva virgen 3L") ? "AOV3L Aceite-oliva-5l" :
                                        (($fila["producto"] === "Aceite oliva virgen 5L") ? "AOV5L Aceite-oliva-5l" :
                                        (($fila["producto"] === "Aceite oliva virgen extra 1L") ? "AOVE1L Aceite-oliva-1l" :
                                        (($fila["producto"] === "Aceite oliva virgen extra 3L") ? "AOVE3L Aceite-oliva-5l" :
                                        (($fila["producto"] === "Aceite oliva virgen extra 5L") ? "AOVE5L Aceite-oliva-5l" :
                                        str_replace(' ', '-', substr($fila["producto"], 0, 15)))))));
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
                                        <div class="col-md-12"><a class="product-image" ><img src="<?php echo $fila["imagen"]; ?>"></a></div>
                                    </div>
                                    <div class="row">
                                        <div class="col-8">
                                        <style>
                                        @media (min-width: 0px) and (max-width: 575px) {
                                            #nombreeProductoH3{
                                            height: 30px;
                                            }
                                        }
                                        @media (min-width: 768px) and (max-width: 1199px) {
                                            #nombreeProductoH3{
                                            height: 70px;
                                            }
                                        }
                                        @media (min-width: 1200px) and (max-width: 2160px) {
                                            #nombreeProductoH3{
                                            height: 30px;
                                            }
                                        }
                                        </style>
                                            <h3 id="nombreeProductoH3" style ="font-size: 18px; font-weight: 800;" ><a class="ModalTrigger" id="nombreeProducto"
                                            style="cursor: pointer; color: inherit; text-decoration: none;"><?php echo $fila["producto"];?><?php switch                                                   ($fila["producto"]){ 
                                                case 'Aceite oliva 1l 1':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva 3l 1':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva 5l 1':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva 1l 0,4':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva 3l 0,4':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva 5l 0,4':
                                                 echo "°";
                                                break;
                                                case 'Aceite oliva virgen 1L':
                                                 echo ".";
                                                break;
                                                case 'Aceite oliva virgen 3L':
                                                 echo ".";
                                                break;
                                                case 'Aceite oliva virgen 5L':
                                                 echo ".";
                                                break;
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
                                                case 'Cafe molido tostado':
                                                 echo ".";
                                                break;
                                                case 'Cafe soluble':
                                                 echo ".";
                                                break;
                                                case 'Atun claro':
                                                 echo ".";
                                                break;                                                
                                                case 'Tortilla patata':
                                                 echo " sin cebolla";
                                                break;
                                                case 'Cuajada':
                                                 echo " natural";
                                                break;
                                                case 'Gelatina sabores':
                                                 echo ".";
                                                break;
                                                case 'Natillas':
                                                 echo " vainilla";
                                                break;
                                                case 'Maiz dulce':
                                                 echo " lata";
                                                break;                                                
                                                case 'Guisantes muy finos':
                                                 echo " lata";
                                                break;
                                                case 'Guisantes finos':
                                                 echo " bote";
                                                break;
                                                case 'Guisantes medianos':
                                                 echo " lata";
                                                break;
                                                

                                    }?></a></h3>
                                        </div>
                                        <div class="col-4"><img src="..\imagenes\supermercados\iconos/<?php echo str_replace(' ', '', strtolower($fila["supermercado"])); ?>.png" style="max-width: 100%;"></div>
                                    </div>

                                    <div class="product-rating d-block d-sm-none d-md-none d-lg-none d-xl-none d-xxl-block"><a class="small-text" ><?php echo $fila["detalle"]; ?><?php echo ' '. $fila["supermercado"]; ?></a></div>
                                    <div class="row">
                                        <div class="col-12">
                                        <style>
                                        @media (min-width: 576px) and (max-width: 935px) {
                                            .product-description {
                                            padding-top: -30px;
                                            padding-bottom: 80px;
                                            }
                                        }
                                        </style>
                                            <p class="product-description pt-0 pt-sm-1 pt-xl-0" style="height: 40px;"><?php echo $fila["descripcion"]; ?></p>
                                            <div class="row">
                                                <div class="col-6 col-sm-8"><a href="<?php echo $fila["enlace"]; ?>" target="_blank" rel="noreferrer"><button class="btn btn-light" type="button">Comprar ahora</button></a></div>
                                                <div class="col-6 col-sm-4"><p class="product-price" style="cursor: pointer;"><?php echo $fila["precio"]; ?>€</p></div>
                                            </div>
                                        </div>
                                        <?php 
                                        if ($_COOKIE["FormularioCookies"] === 'Si') {
                                        ?>
                                        <div class="col-12 pt-1">

                                        <style>
                                            @media (min-width: 0px) and (max-width: 575px) {
                                                .anadirLista {
                                                width: 136px;
                                                }
                                            }
                                            @media (min-width: 1200px) and (max-width: 2160px) {
                                                .anadirLista {
                                                width: 136px;
                                                }
                                            }
                                            </style>


                                        <div class="row">
                                            <div class="col-6 col-sm-8">
                                                <button id="tttest" class="btn btn-light anadirLista" onclick="showAddedToCart()" type="submit">Añadir a lista</button>
                                            </div>
                                            <div class="col-6 col-sm-4 d-flex justify-content-end">
                                                <button class="btn btn-light ModalTrigger" id="botonModal" type="button"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clock-history" viewBox="0 0 16 16">
  <path d="M8.515 1.019A7 7 0 0 0 8 1V0a8 8 0 0 1 .589.022zm2.004.45a7 7 0 0 0-.985-.299l.219-.976q.576.129 1.126.342zm1.37.71a7 7 0 0 0-.439-.27l.493-.87a8 8 0 0 1 .979.654l-.615.789a7 7 0 0 0-.418-.302zm1.834 1.79a7 7 0 0 0-.653-.796l.724-.69q.406.429.747.91zm.744 1.352a7 7 0 0 0-.214-.468l.893-.45a8 8 0 0 1 .45 1.088l-.95.313a7 7 0 0 0-.179-.483m.53 2.507a7 7 0 0 0-.1-1.025l.985-.17q.1.58.116 1.17zm-.131 1.538q.05-.254.081-.51l.993.123a8 8 0 0 1-.23 1.155l-.964-.267q.069-.247.12-.501m-.952 2.379q.276-.436.486-.908l.914.405q-.24.54-.555 1.038zm-.964 1.205q.183-.183.35-.378l.758.653a8 8 0 0 1-.401.432z"/>
  <path d="M8 1a7 7 0 1 0 4.95 11.95l.707.707A8.001 8.001 0 1 1 8 0z"/>
  <path d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5"/>
</svg></button>
                                                <!--<p class="product-price ModalTrigger" style="cursor: pointer;">Historial</p>-->
                                            </div>
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

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
var elementosOcultadosPorFormato = [];    
var elementosOcultadosPorClase = [];
var elementosOcultos = [];
var divElementosMostrados = document.getElementById("elementosMostrados");
var elementos = Array.from(divElementosMostrados.children);

function ocultarElementosPorClase(clase) {
    console.log(clase);
    var id;
    switch (clase) {
        case 'Ahorra Mas':
            id = "ahorramascb";
            break;
        case 'Alcampo':
            id = "alcampocb";
            break;
        case 'Carrefour':
            id = "carrefourcb";
            break;
        case 'Dia':
            id = "diacb";
            break;
        case 'Eroski':
            id = "eroskicb";
            break;
        case 'Mercadona':
            id = "mercadonacb";
            break;
        default:
            console.error("Clase no reconocida:", clase);
            return;
    }

    console.log(id);

    var checkbox = document.getElementById(id);
    console.log(checkbox);

    var elementos = document.getElementsByClassName(clase);

    for (var i = 0; i < elementos.length; i++) {
        if (checkbox.checked) {
            // Muestra el elemento si está oculto
            //elementos[i].style.display = "block";

            // Elimina el elemento de la lista de elementos ocultados
            var index = elementosOcultadosPorClase.indexOf(elementos[i]);
            if (index > -1) {
                elementosOcultadosPorClase.splice(index, 1);
            }
        } else {
            //elementos[i].style.display = "none";
            elementosOcultadosPorClase.push(elementos[i]);
        }
    }
    elementosOcultos = elementosNoDuplicados(elementosOcultadosPorClase, elementosOcultadosPorFormato);
    ocultar(elementosOcultos);
}

    function ocultarPorFormato(textoBuscado) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h3 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado)) {
        // Verifica si el elemento está en la lista de elementos ocultados por clase
        if (elementosOcultadosPorClase.includes(productItem)) {
            // No hagas nada si ya está oculto
        } else {
            // Verifica si el elemento está oculto
            if (productItem.style.display === "none") {
            // Muestra el elemento
            //productItem.style.display = "block";
            
            var index = elementosOcultadosPorFormato.indexOf(productItem);
            if (index > -1) {
                elementosOcultadosPorFormato.splice(index, 1);
            }

            } else {
            // Oculta el elemento si no está oculto
            //productItem.style.display = "none";
            elementosOcultadosPorFormato.push(productItem);
            }
        }
        }
    });
    elementosOcultos = elementosNoDuplicados(elementosOcultadosPorClase, elementosOcultadosPorFormato);
    ocultar(elementosOcultos);
    }

function ocultarPorFormatoMultiple(textoBuscado1, textoBuscado2) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen el texto buscado
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h3 a");
        var texto = h2.textContent;
        if (texto.includes(textoBuscado1) || texto.includes(textoBuscado2)) {
            // Verifica si el elemento está en la lista de elementos ocultados por clase
            if (elementosOcultadosPorClase.includes(productItem)) {
                // No hagas nada si ya está oculto
            } else {
                // Verifica si el elemento está oculto
                if (productItem.style.display === "none") {
                    // Muestra el elemento
                    // productItem.style.display = "block";

                    var index = elementosOcultadosPorFormato.indexOf(productItem);
                    if (index > -1) {
                        elementosOcultadosPorFormato.splice(index, 1);
                    }

                } else {
                    // Oculta el elemento si no está oculto
                    // productItem.style.display = "none";
                    elementosOcultadosPorFormato.push(productItem);
                }
            }
        }
    });

    elementosOcultos = elementosNoDuplicados(elementosOcultadosPorClase, elementosOcultadosPorFormato);
    ocultar(elementosOcultos);
}

function elementosNoDuplicados(array1, array2) {
  // Combina los dos arrays en uno nuevo
  var combinedArray = array1.concat(array2);

  // Filtra los elementos únicos del array combinado
  var resultado = combinedArray.filter(function (elemento, index, array) {
    return array.indexOf(elemento) === index;
  });

  return resultado;
}

function ocultar(arrayDeElementos) {
    elementos.forEach(function (elemento){
        elemento.style.display = "block";
    });
    arrayDeElementos.forEach(function (elemento) {
        elemento.style.display = "none";
    });
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
    function ocultarGarrafa3L (){
    var elementos1L = document.getElementsByClassName("Aceite-oliva-3l");
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

function ocultarAceiteOV() {<!--Necesita arreglar-->
    ocultarPorFormatoMultiple('Aceite oliva virgen 5L.', 'Aceite oliva virgen 1L.');
    ocultarAceiteOV2();
}

function ocultarAceiteOV2() {<!--Necesita arreglar-->
    ocultarPorFormatoMultiple('Aceite oliva virgen 3L.', 'RAYNERCODE');
}

function ocultarAceiteOVE() {<!--Necesita arreglar-->
    ocultarPorFormatoMultiple('Aceite oliva virgen extra 1L', 'Aceite oliva virgen extra 3L', 'Aceite oliva virgen extra 5L');
    ocultarAceiteOVE2();
}

function ocultarAceiteOVE2() {<!--Necesita arreglar-->
    ocultarPorFormatoMultiple('Aceite oliva virgen extra 5L', 'RAYNERCODE');
}

function ocultarAceite04() {
    ocultarPorFormatoMultiple('Aceite oliva 1l 0,4', 'Aceite oliva 5l 0,4');
}

function ocultarAceite1() {
    ocultarPorFormatoMultiple('Aceite oliva 1l 1', 'Aceite oliva 5l 1');
}

     <?php break; ?>
    <?php
        case 'Aceite girasol':?>

    function ocultarBotella1L() {
    ocultarPorFormato('Aceite girasol 1L');
    }
    function ocultarGarrafa5L() {
    ocultarPorFormato('Aceite girasol 5L');
    }
    <?php
        break;
     case 'Batido de chocolate':?>
    function ocultarBotella1L (){
        ocultarPorFormato('Batido chocolate 1l');
}
    function ocultarPack6 (){
        ocultarPorFormato('Batido chocolate pack');
}
     <?php
             break;
     case 'Batido de fresa':?>
    function ocultarBotella1L (){
        ocultarPorFormato('Batido fresa 1l');
}
    function ocultarPack6 (){
        ocultarPorFormato('Batido fresa pack');
}
    <?php
        break;
     case 'Batido de vainilla':?>    
    function ocultarBotella1L (){
        ocultarPorFormato('Batido vainilla 1l');
}
    function ocultarPack6 (){
        ocultarPorFormato('Batido vainilla pack');
} 
    <?php
        break;     
        case 'Cafe molido tostado':?>    
    function ocultarCafeTostadoNormal(){
        ocultarPorFormato('Cafe molido tostado.');
}
    function ocultarCafeTostadoDescafeinado(){
        ocultarPorFormato('Cafe molido tostado descafeinado');
}     
    <?php
        break;
        case 'Cafe soluble':?>    

    function ocultarCafeSolubleNormal(){
        ocultarPorFormato('Cafe soluble.');
}
    function ocultarCafeSolubleDescafeinado(){
        ocultarPorFormato('Cafe soluble descafeinado');
}    
    <?php
        break;        
        case 'Muesli':?>    
var elementosOcultadosPorClase = [];


function ocultarMuesliNormal() {
  ocultarPorFormato('Muesli solo');
}

function ocultarMuesliFruta() {
  ocultarPorFormato('Muesli con frutas');
}

function ocultarMuesliFrutosSecos() {
  ocultarPorFormato('Muesli con frutos secos');
}

function ocultarMuesliChocolate() {
  ocultarPorFormato('Muesli con chocolate');
}
 
    <?php
        break;        
        case 'Copos de arroz y trigo':?>    

function ocultarCoposArrozNormal() {
    ocultarPorFormato('Copos de arroz y trigo solo');
}

function ocultarCoposArrozFrutosRojos() {
    ocultarPorFormato('Copos de arroz y trigo integral con frutos rojos');
} 
    <?php
        break;        
    case 'Galleta estilo oreo':?>    

    function ocultarOreoNormal() {
    ocultarPorFormato('Galleta oreo.');
    }

    function ocultarOreoChocoBlanco() {
    ocultarPorFormato('Galleta oreo cubierta de chocolate blanco');
    } 
    <?php
        break;      
        case 'Harina de trigo':?>    


    function ocultarHarinaTrigoNormal() {
    ocultarPorFormato('Harina de trigo.');
    }

    function ocultarHarinaTrigoIntegral() {
    ocultarPorFormato('Harina de trigo integral');
    } 
    <?php
        break;        
    case 'Conos':?>    

    function ocultarNataFresa() {
    ocultarPorFormato('Cono nata y fresa');
    }
    function ocultarNataTrufa() {
    ocultarPorFormato('Cono nata y trufa');
    }
    function ocultarNataTurron() {
    ocultarPorFormato('Cono nata y turron');
    }    
    function ocultarTartaQueso() {
    ocultarPorFormato('Cono tarta de queso');
    }
   function ocultarVainillaChocolate() {
    ocultarPorFormato('Cono vainilla y chocolate');
    } 
    <?php
        break;    
    case 'Bombon':?>    

    function ocultarBombonAlmendra() {
    ocultarPorFormato('Helado bombon almendra');
    }
    function ocultarBombonAvellana() {
    ocultarPorFormato('Helado bombon avellanas');
    }
    function ocultarBombonChocolateBlanco() {
    ocultarPorFormato('Helado bombon chocolate blanco');
    }    
    function ocultarBombonChocolateNata() {
    ocultarPorFormato('Helado bombon chocolate y nata');
    }
   function ocultarBombonChocolateTriple() {
    ocultarPorFormato('Helado bombon 3 chocolates');
    } 
    <?php
        break;     
    case 'Tarrinas':?>    

    function ocultarTarrinaChocolate() {
    ocultarPorFormato('Tarrina chocolate y trozos');
    }
    function ocultarTarrinaChocolateTriple() {
    ocultarPorFormato('Tarrina tres chocolates');
    }
    function ocultarTarrinaFrutasBosque() {
    ocultarPorFormato('Tarrina frutas del bosque');
    }    
    function ocultarTarrinaLimon() {
    ocultarPorFormato('Tarrina sorbete limon');
    }
    function ocultarTarrinaNataNueces() {
    ocultarPorFormato('Tarrina nata y nueces');
    }
    function ocultarTarrinaStracciatella() {
    ocultarPorFormato('Tarrina helado stracciatella');
    }
    function ocultarTarrinaTurron() {
    ocultarPorFormato('Tarrina helado turron');
    }
    function ocultarTarrinaVainilla() {
    ocultarPorFormato('Tarrina helado vainilla');
    } 
    <?php
        break;    
    case 'Docena Huevo':?>    


    function ocultarDocenaL() {
    ocultarPorFormato('Docena huevo l');
    }
    function ocultarDocenaM() {
    ocultarPorFormato('Docena huevo m');
    }
    function ocultarDocenaXL() {
    ocultarPorFormato('Docena huevo xl');
    }     
    <?php
        break;     
    case 'Leche':?>    

    function ocultarLecheDesnatada() {
    ocultarPorFormato('Leche desnatada.');
    }
    function ocultarLecheDesnatadaSL() {
    ocultarPorFormato('Leche desnatada sin lactosa');
    }
    function ocultarLecheEntera() {
    ocultarPorFormato('Leche entera.');
    }    
    function ocultarLecheEnteraSL() {
    ocultarPorFormato('Leche entera sin lactosa');
    }
    function ocultarLecheSemidesnatada() {
    ocultarPorFormato('Leche semidesnatada.');
    } 
    function ocultarLecheSemidesnatadaSL() {
    ocultarPorFormato('Leche semidesnatada sin lactosa');
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
    var h2 = productItem.querySelector("h3 a");
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
    var h2 = productItem.querySelector("h3 a");
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
        var h2 = productItem.querySelector("h3 a");
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

    function ocultarGarbanzoCocido() {
    ocultarPorFormato('Garbanzo cocido');
    }
    function ocultarGarbanzoCrudo() {
    ocultarPorFormato('Garbanzo crudo');
    }  
    <?php
        break;    
    case 'Alubias':?>    
function ocultarAlubias(textosBuscados) {
    // Selecciona todos los elementos con la clase "product-item"
    var elementosProductItem = document.querySelectorAll(".product-item");

    // Recorre los elementos "product-item" y verifica si contienen alguno de los textos buscados
    elementosProductItem.forEach(function (productItem) {
        var h2 = productItem.querySelector("h3 a");
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

function ocultarLentejaCocida() {
    ocultarPorFormato(['Lenteja cocida']);
}

function ocultarLentejaCrudo() {
    ocultarPorFormato(['Lenteja cruda 1kg']);
}

    <?php
        break;     
    case 'Miel':?> 


function ocultarMielAzahar() {
    ocultarPorFormato(['Miel de azahar']);
}

function ocultarMielFlores() {
    ocultarPorFormato(['Miel de flores 1kg']);
}

    <?php
        break;    
    case 'Pan molde':?>    

    function ocultarMoldeIntegral() {
    ocultarPorFormato('Pan de molde integral.');
    }
    function ocultarMoldeBlancoSinCorteza() {
    ocultarPorFormato('Pan de molde blanco sin corteza');
    }
    function ocultarMoldeBlancoFamiliar() {
    ocultarPorFormato('Pan de molde blanco familiar');
    }    
    function ocultarMoldeIntegralSinCorteza() {
    ocultarPorFormato('Pan de molde integral sin corteza');
    }

    <?php
        break;     
    case 'Macarron espiral':?>    

    function ocultarEspiralBlanco() {
    ocultarPorFormato('Macarron espiral.');
    }
    function ocultarEspiralVegetales() {
    ocultarPorFormato('Macarron espiral vegetal');
    }

    <?php
        break; 
    case 'Atun':?>    

    function ocultarAtunClaro() {
    ocultarPorFormato('Atun claro.');
    }
    function ocultarAtunAceiteOliva() {
    ocultarPorFormato('Atun claro aceite oliva');
    }    
    function ocultarAtunAceiteGirasol() {
    ocultarPorFormato('Atun claro aceite girasol');
    }
    function ocultarAtunEscabeche() {
    ocultarPorFormato('Atun claro en escabeche');
    }

    <?php
        break;
    case 'Bonito':?>    

    function ocultarBonitoAceiteOliva() {
    ocultarPorFormato('Bonito del norte en aceite de oliva');
    }
    function ocultarBonitoEscabeche() {
    ocultarPorFormato('Bonito del norte en escabeche');
    }    

    <?php
        break;

    case 'Mejillones':?>

    function ocultarMejillon() {
    ocultarPorFormato('Mejillones al natural');
    }
    function ocultarMejillonSalsa() {
    ocultarPorFormato('Mejillones salsa vieira');
    }    

    <?php
        break;
    case 'Sardinas':?>

    function ocultarSardinasAceiteOliva() {
    ocultarPorFormato('Sardinas en aceite de oliva');
    }
    function ocultarSardinasEnTomate() {
    ocultarPorFormato('Sardinas en tomate');
    }    
    function ocultarSardinasEscabeche() {
    ocultarPorFormato('Sardinas en escabeche');
    }
    function ocultarSardinasLimon() {
    ocultarPorFormato('Sardinas con limon');
    }
    function ocultarSardinasPicantonas() {
    ocultarPorFormato('Sardinas picantonas');
    }     

    <?php
        break;
    case 'Tortilla patata':?>

    function ocultarTortillaSinCebolla() {
    ocultarPorFormato('Tortilla patata sin cebolla');
    }
    function ocultarTortillaConCebolla() {
    ocultarPorFormato('Tortilla patata cebolla');
    }      

    <?php
        break;
    case 'Pizzas':?>

    function ocultarPizza4Quesos() {
    ocultarPorFormato('Pizza cuatro quesos');
    }
    function ocultarPizzaBarbacoa() {
    ocultarPorFormato('Pizza barbacoa');
    }
    function ocultarPizzaJamonQueso() {
    ocultarPorFormato('Pizza jamon y queso');
    }
    function ocultarPizzaPolloyBacon() {
    ocultarPorFormato('Pizza pollo y bacon');
    }       

    <?php
        break;
    case 'Cuajada':?>

    function ocultarCuajada() {
    ocultarPorFormato('Cuajada natural');
    }
    function ocultarCuajadaAzucar() {
    ocultarPorFormato('Cuajada con azucar');
    }
      
    <?php
        break;
    case 'Flanes':?>

    function ocultarFlanVainilla() {
    ocultarPorFormato('Flan vainilla');
    }
    function ocultarFlanHuevo() {
    ocultarPorFormato('Flan huevo');
    }
      
    <?php
        break;
    case 'Gelatinas':?>

    function ocultarGelatinaSabores() {
    ocultarPorFormato('Gelatina sabores.');
    }
    function ocultarGelatinaSaboresLight() {
    ocultarPorFormato('Gelatina sabores light');
    }
    function ocultarGelatinaFresa() {
    ocultarPorFormato('Gelatina fresa');
    }
      
    <?php
        break;
    case 'Natillas':?>

    function ocultarNatillasChoco() {
    ocultarPorFormato('Natillas chocolate');
    }
    function ocultarNatillasVainilla() {
    ocultarPorFormato('Natillas vainilla');
    }
      
    <?php
        break;
    case 'Patatas fritas':?>

    function ocultarPatatasArtesanales() {
    ocultarPorFormato('Patatas fritas artesanales');
    }
    function ocultarPatatasChurreria() {
    ocultarPorFormato('Patatas fritas churreria');
    }
    function ocultarPatatasCongeladasFino() {
    ocultarPorFormato('Patatas fritas congeladas corte fino');
    }
    function ocultarPatatasCongeladasTradicional() {
    ocultarPorFormato('Patatas fritas congeladas corte tradicional');
    }
    function ocultarPatatasLisas() {
    ocultarPorFormato('Patatas fritas lisas');
    }
    function ocultarPatatasPaja() {
    ocultarPorFormato('Patatas fritas paja');
    }
      
    <?php
        break;
    case 'Aceitunas':?>

    function ocultarAceitunaNegraConHueso() {
    ocultarPorFormato('Aceitunas negra con hueso');
    }
    function ocultarAceitunaNegraSinHueso() {
    ocultarPorFormato('Aceitunas negra sin hueso');
    }
    function ocultarAceitunaVerdeConHueso() {
    ocultarPorFormato('Aceitunas verdes con hueso');
    }
    function ocultarAceitunaVerdeSinHueso() {
    ocultarPorFormato('Aceitunas verdes sin hueso');
    }

      
    <?php
        break;
    case 'Galletas saladas':?>

    function ocultarGalletaSaladaPaquete() {
    ocultarPorFormato('Galletas saladas paquete');
    }
    function ocultarGalletaSaladaBote() {
    ocultarPorFormato('Galletas saladas bote');
    }

    <?php
        break;
    case 'Palomitas':?>

    function ocultarPalomitasMantequilla() {
    ocultarPorFormato('Palomitas mantequilla pack');
    }
    function ocultarPalomitasMicroondasMantequilla() {
    ocultarPorFormato('Palomitas microondas mantequilla pack');
    }
    function ocultarPalomitasMicroondasSal() {
    ocultarPorFormato('Palomitas microondas sal pack');
    }
      
    <?php
        break;
    case 'Tomate':?>

    function ocultarTomateFritoBote() {
    ocultarPorFormato('Tomate frito bote');
    }
    function ocultarTomateFritoCaseroAceite() {
    ocultarPorFormato('Tomate frito casero aceite oliva');
    }
    function ocultarTomateFritoPack() {
    ocultarPorFormato('Tomate frito pack');
    }
    function ocultarTomateFritoSarten() {
    ocultarPorFormato('Tomate frito en sarten');
    }
    function ocultarTomateTriturado400g() {
    ocultarPorFormato('Tomate triturado 400g');
    }
    function ocultarTomateTriturado800g() {
    ocultarPorFormato('Tomate triturado 800g');
    }
      
    <?php
        break;
    case 'Judias verdes':?>

    function ocultarJudiasVerdesAnchasConserva() {
    ocultarPorFormato('Judias verdes anchas en conserva');
    }
    function ocultarJudiasVerdesRedondasConserva() {
    ocultarPorFormato('Judias verdes redondas en conserva');
    }
    function ocultarJudiasVerdesRedondasCongeladas() {
    ocultarPorFormato('Judias verdes redondas congeladas 1kg');
    }
    function ocultarJudiasVerdesAnchasCongeladas() {
    ocultarPorFormato('Judias verdes anchas congeladas 1kg');
    }
      
    <?php
        break; 
    case 'Pimientos':?>

    function ocultarPimientosPiquilloEnTiras() {
    ocultarPorFormato('Pimientos de piquillo en tiras');
    }
    function ocultarPimientosPiquilloEntero() {
    ocultarPorFormato('Pimientos de piquillo enteros');
    }
      
    <?php
        break;
    case 'Esparragos':?>

    function ocultarEsparragoVerde() {
    ocultarPorFormato('Esparragos verdes delgados');
    }
    function ocultarEsparragoBlanco() {
    ocultarPorFormato('Esparragos blancos gruesos');
    }
      
    <?php
        break;
    case 'Maiz':?>

    function ocultarMaizDulceCongelado() {
    ocultarPorFormato('Maiz dulce congelado');
    }
    function ocultarMaizDulceLata() {
    ocultarPorFormato('Maiz dulce lata');
    }
      
    <?php
        break;  
    case 'Champinones':?>

    function ocultarChampinonesLaminados() {
    ocultarPorFormato('Champinon laminado');
    }
    function ocultarChampinonesEnteros() {
    ocultarPorFormato('Champinon entero');
    }
      
    <?php
        break;
    case 'Guisantes':?>

    function ocultarGuisantesFinosLata() {
    ocultarPorFormato('Guisantes muy finos lata');
    }
    function ocultarGuisantesMuyFinosBote() {
    ocultarPorFormato('Guisantes muy finos bote');
    }
    function ocultarGuisantesMuyFinosCongelados() {
    ocultarPorFormato('Guisantes muy finos congelados');
    }
    function ocultarGuisantesFinosCongelados() {
    ocultarPorFormato('Guisantes finos congelados');
    }
    function ocultarGuisantesFinosBote() {
    ocultarPorFormato('Guisantes finos bote');
    }    
    function ocultarGuisantesMedianosLata() {
    ocultarPorFormato('Guisantes medianos lata');
    }
      
    <?php
        break;
    case 'Alcachofas':?>

    function ocultarAlcachofaNormal() {
    ocultarPorFormato('Alcachofa congelada');
    }
    function ocultarAlcachofaBaby() {
    ocultarPorFormato('Alcachofa baby congelada');
    }
      
    <?php
        break;   
    case 'Bicarbonato':?>
    function ocultarBotes (){
        ocultarPorFormato('Bicarbonato bote');
}
    function ocultarPaquete1kg (){
        ocultarPorFormato('Bicarbonato 1kg');
}  
    <?php
        break;
    }?>

    // Función para llamar al método showAddedToCartToast de la interfaz Android
    function showAddedToCart() {
        // Llamar al método showAddedToCartToast definido en la interfaz Android
        Android.showAddedToCartToast();
    }
    document.addEventListener('DOMContentLoaded', function () {
        const modalTriggers = document.getElementsByClassName('ModalTrigger');

        for (const modalTrigger of modalTriggers) {
            modalTrigger.addEventListener('click', function () {
                var myModal = new bootstrap.Modal(document.getElementById('ModalPrecio'));
                myModal.show();
            });
        }
    });
          $(document).ready(function () {
        $('.ModalTrigger').click(function () {
            // Encuentra el ancestro con el atributo id y obtén su valor
            var idProducto = $(this).closest('.product-item').attr('id');
                $.ajax({
                    url: "historialPrecio.php",
                    method: "POST",
                    data: { input: idProducto },
                    success: function(data) {
                        $(".modal-body").html(data);
                    }
                });
        });

        $("#botonModal").click(function(event) {
            event.preventDefault();
            var idProducto = $(this).closest('.product-item').attr('id');
            $.ajax({
                url: "historialPrecio.php",
                method: "POST",
                data: { input: idProducto },
                success: function(data) {
                    $(".modal-body").html(data);
                }
            });
        });
           

    });
    </script>

</body>
</html>
