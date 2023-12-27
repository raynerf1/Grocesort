<table class="table">
    <thead>
        <tr>
            <th scope="col">Fecha</th>
            <th scope="col">Precio</th>
        </tr>
    </thead>
    <tbody>
        <?php
        // historialPrecio.php

        // Verifica si se recibió un valor POST
        if (isset($_POST['input'])) {
            // Obtiene el valor del parámetro 'input'
            $idProducto = $_POST['input'];

            // Realiza las operaciones necesarias con $idProducto
            // ...
            require_once('../../config.php'); # Cambiar en InfinityFree
            $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME . ';charset=' . DB_CHARSET, DB_USER, DB_PASSWORD);
            $sql = 'SELECT fecha, precio FROM `precios` where id = :idProducto order by fecha desc limit 10';

            $stmt = $pdo->prepare($sql);
            $stmt->bindParam(':idProducto', $idProducto, PDO::PARAM_STR);
            $stmt->execute();

            if ($stmt->rowCount() > 0) {
                while ($fila = $stmt->fetch(PDO::FETCH_ASSOC)) {
                    ?>
                    <tr>
                        <th scope="row"><?php echo $fila["fecha"]; ?></th>
                        <td><?php echo $fila["precio"]; ?></td>
                    </tr>
                    <?php
                }
            }
        } else {
            // Si no se recibió el valor esperado, devuelve un mensaje de error
            echo "Error: No se recibió el valor esperado";
        }
        ?>
    </tbody>
</table>