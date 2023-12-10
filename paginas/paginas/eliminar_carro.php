<?php
 
$idproducto = $_POST["idproducto"];
 
$carro = isset($_COOKIE["carro"]) ? $_COOKIE["carro"] : "[]";
$carro = json_decode($carro);
 
$nuevo_carro = array();
foreach ($carro as $c)
{
    if ($c->idProducto != $idproducto)
    {
        array_push($nuevo_carro, $c);
    }
}
 
setcookie("carro", json_encode($nuevo_carro));
//echo $idproducto;
header("Location: carro.php");
 
?>