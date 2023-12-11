<!DOCTYPE html>
<!--Busqueda-->
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>RaynerGroceSort</title>
    <link rel="stylesheet" href="../assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="../assets/css/styles.min.css">
    <link rel="stylesheet" href="../assets/css/preloader.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.5/gsap.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>
<body>
<div id="div3">
    <nav class="mt-4">
    </nav>
    <nav class="mt-5">
    </nav>
    <section id="sectionSecciones" class="py-4 py-xl-5">

        <div class="d-flex justify-content-center mb-3"  >
            <u><h1 data-bs-toggle="tooltip1" data-bs-placement="top" title="Secciones encontradas según criterio de búsqueda"  class="pt-1">Secciones</h1></u>

        </div>
        <script>
            var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip1"]'));
            var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
                return new bootstrap.Tooltip(tooltipTriggerEl);
            });
        </script>
        <div class="container-fluid">
        <div class="row row-cols-2 row-cols-sm-2 row-cols-md-2 row-cols-lg-4 row-cols-xl-4 row-cols-xxl-4 justify-content-center" id="rows-1">
        <?php
        include('../../config.php'); // Asegúrate de que config.php contiene la configuración de la base de datos.

        $resultados = array(); 
        if (isset($_POST['input'])) {
            $input = $_POST['input'];

            try {
                $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=' . DB_CHARSET, DB_USER, DB_PASSWORD);
                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                $consulta = "SELECT * FROM secciones WHERE nombre LIKE :input order by nombre asc";
                $stmt = $pdo->prepare($consulta);
                $input = '%' . $input . '%';
                $stmt->bindParam(':input', $input, PDO::PARAM_STR);

                $stmt->execute();

                if ($stmt->rowCount() > 0) {
                    while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)) {
                        ?>
                        <div class="col justify-content-center d-flex align-items-center"
                        id="<?php echo str_replace(' ', '', strtolower(trim($fila["nombre"]))); ?>">

                            <form method="POST" action="vistaSecciones.php">
                                <input type="hidden" name="nombre_equipo" value="<?php echo $fila["nombre"]; ?>">
                                <input type="hidden" name="foto_slider" value="test<?php echo $fila["nombre"]; ?>">
                                <input type="hidden" name="foto_logo" value="test<?php echo $fila["nombre"]; ?>">
                                <a class="justify-content-center d-flex align-items-center columna"
                                   href="#"
                                   onclick="event.preventDefault(); this.closest('form').submit();">
                                    <div class="card" style="border-style: none;">
                                        <div class="card-body">
                                            <h1 class="text-start"><?php echo $fila["nombre"]; ?></h1>
                                            <img class="img-fluid order-4 coche"
                                                 src=<?php echo '../imagenes/secciones/' . str_replace(' ', '', strtolower(trim($fila["nombre"]))) . '.jpg' ?>
                                                 width="700px">
                                        </div>
                                    </div>
                                    <img class="logo"
                                         src=<?php echo '../imagenes/secciones/iconos/' . str_replace(' ', '', strtolower(trim($fila["nombre"]))) . '.png' ?>
                                         width="100px" style="position: absolute;">
                                </a>
                            </form>
                        </div>
                        <?php
                        
                    }
                } else { if($stmt->rowCount() == 0){ 
                    echo '<script>
                    document.getElementById("sectionSecciones").style.display = "none";
                    </script>';

                } else {}
                    echo 'No se encontraron secciones con el texto de búsqueda.';
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
    <nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav>
    </nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav>
    </nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav>'
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
    <br>
    <div id="div4">
    <nav class="mt-4">
    </nav>
    <nav class="mt-5">
    </nav>
    <hr class="featurette-divider">
    <section class="py-4 py-xl-5">

        <div class="d-flex justify-content-center mb-3" data-bs-toggle="tooltip2" data-bs-placement="top" title="Conjunto de productos dentro de cada sección. [Sección>Subsección]">
            <u><h1>Subsecciones</h1></u>
        </div>
        <script>
            var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip2"]'));
            var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
                return new bootstrap.Tooltip(tooltipTriggerEl);
            });
        </script>

        <div class="container-fluid">
        <div class="row row-cols-2 row-cols-sm-2 row-cols-md-2 row-cols-lg-4 row-cols-xl-4 row-cols-xxl-4 justify-content-center" id="row-2">
        <?php
        include('../../config.php'); // Asegúrate de que config.php contiene la configuración de la base de datos.

        $resultados = array(); 
        if (isset($_POST['input'])) {
            $input = $_POST['input'];

            try {
                $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=' . DB_CHARSET, DB_USER, DB_PASSWORD);
                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                $consulta = "SELECT * FROM subsecciones WHERE subseccion LIKE :input order by subseccion asc";
                $stmt = $pdo->prepare($consulta);
                $input = '%' . $input . '%';
                $stmt->bindParam(':input', $input, PDO::PARAM_STR);

                $stmt->execute();

                if ($stmt->rowCount() > 0) {
                    while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)) {
                        ?>
                        <div class="col justify-content-center d-flex align-items-center"
                        id="<?php echo str_replace(' ', '', strtolower(trim($fila["subseccion"]))); ?>">

                            <form method="POST" action="vistaPrecioTest.php">
                                <input type="hidden" name="nombre_subseccion" value="<?php echo $fila["subseccion"]; ?>">
                                <input type="hidden" name="foto_slider" value="test<?php echo $fila["subseccion"]; ?>">
                                <input type="hidden" name="foto_logo" value="test<?php echo $fila["subseccion"]; ?>">
                                <a class="justify-content-center d-flex align-items-center columna"
                                   href="#"
                                   onclick="event.preventDefault(); this.closest('form').submit();">
                                    <div class="card" style="border-style: none;">
                                        <div class="card-body">
                                            <h1 class="text-start"><?php echo $fila["subseccion"]; ?></h1>

                                                 <img class="img-fluid order-4 coche"
                                                 src="<?php echo $fila["imagen"]; ?>" width="700px">
                                        </div>
                                    </div>
                                    
                                </a>
                            </form>
                        </div>
                        <?php
                    }
                } else {  
                   echo '<p style="padding-left: 25%; white-space: nowrap;">No se encontraron subsecciones con el texto de búsqueda.</p>';
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
    <nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav>
    </nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav>
    </nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav><nav class="pb-5"></nav>'
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
    <nav class="pb-5">
    </nav>
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
    <nav class="pb-5">
    </nav>
</div>
</body>

</div>
</html>
