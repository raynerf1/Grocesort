<?php
include('../../config.php');

// Verifica si se ha enviado un formulario por POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Verifica si la variable idproducto está presente en $_POST
    if (isset($_POST['idproducto'])) {
        // Obtiene el valor de idproducto
        $idProducto = $_POST['idproducto'];

        $carro = isset($_COOKIE["carro"]) ? json_decode($_COOKIE["carro"], true) : [];

        // Verifica si la ID ya está presente en el carrito
        $productoExistente = false;
        foreach ($carro as &$producto) {
            if ($producto['idProducto'] == $idProducto) {
                // La ID ya existe, incrementa la cantidad
                $producto['cantidad'] += 1;
                $productoExistente = true;
                break;
            }
        }

        // Si la ID no está presente, agrega un nuevo elemento al carrito
        if (!$productoExistente) {
            try {
                $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=' . DB_CHARSET, DB_USER, DB_PASSWORD, array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET SESSION SQL_BIG_SELECTS=1'));
                $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                $consulta = "SELECT precios.producto, precios.precio, precios.supermercado, precios.detalle, productos.imagen, productos.enlace 
                            FROM `precios` 
                            LEFT JOIN productos ON precios.producto = productos.producto AND precios.supermercado = productos.supermercado
                            WHERE precios.id = :idproducto AND precios.fecha = (SELECT MAX(fecha) FROM precios);";
                $stmt = $pdo->prepare($consulta);
                $stmt->bindParam(':idproducto', $idProducto, PDO::PARAM_STR);
                $stmt->execute();

                if ($stmt->rowCount() > 0) {
                    while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)) {
                        $carro[] = array(
                            "idProducto" => $idProducto,
                            "cantidad" => 1,
                            "producto" => $fila['producto'],
                            "precio" => $fila['precio'],
                            "supermercado" => $fila['supermercado'],
                            "imagen" => $fila['imagen'],
                            "enlace" => $fila['enlace'],
                            "detalle" => $fila['detalle']
                        );
                        break;
                    }
                }
            } catch (PDOException $e) {
                echo 'Error al conectar a la base de datos: ' . $e->getMessage();
            }
        }

        setcookie("carro", json_encode($carro));

        // Redirige de nuevo a la página anterior

                session_start();
        $nombre_subseccion = $_SESSION['nombre_subseccion'];
        //echo "<script>window.history.back();</script>";
        header("Location: vistaPrecioTest.php?nombre_subseccion=$nombre_subseccion");
    } else {
        echo 'No se recibió el valor de idproducto en el formulario.';
    }
} else {
    echo 'No se ha enviado un formulario por POST.';
}
?>
