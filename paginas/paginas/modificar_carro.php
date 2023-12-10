<?php

function modificarCantidad($idProducto, $accion) {
    $carro = isset($_COOKIE["carro"]) ? json_decode($_COOKIE["carro"], true) : [];

    foreach ($carro as &$producto) {
        if ($producto["idProducto"] == $idProducto) {
            // Verificar si la acción es "sumar" y la cantidad no es 1
            if ($accion == "sumar") {
                $producto["cantidad"] += 1;
            }
            // Verificar si la acción es "restar" y la cantidad no es 1
            elseif ($accion == "restar" && $producto["cantidad"] != 1) {
                $producto["cantidad"] -= 1;
            }
            // No hacer nada si la cantidad es 1 y se quiere restar
            // (o cualquier otro caso que no sea sumar y cantidad no es 1)
        }
    }

    // Actualizar la cookie con el nuevo arreglo de productos
    setcookie("carro", json_encode($carro));
}

// Uso de la función (suponiendo que tienes $_POST["idproducto"] y $_POST["accion"])
$idProducto = $_POST["idproducto"];
$accion = $_POST["accion"];
modificarCantidad($idProducto, $accion);

// Redirigir después de modificar la cantidad
header("Location: carro.php");
?>
