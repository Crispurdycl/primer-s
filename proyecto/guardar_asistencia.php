<?php
// Datos de conexión a la base de datos
$servername = "nombre_servidor";
$username = "nombre_usuario";
$password = "contraseña";
$dbname = "nombre_base_de_datos";

// Obtener los datos del formulario
$nombre = $_POST['nombre'];
$rut = $_POST['rut'];
$asignatura = $_POST['asignatura'];

// Crear la conexión a la base de datos
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar la conexión
if ($conn->connect_error) {
    die("Error en la conexión a la base de datos: " . $conn->connect_error);
}

// Preparar y ejecutar la consulta SQL para insertar los datos en la tabla correspondiente
$sql = "INSERT INTO asistencia (nombre, rut, asignatura) VALUES ('$nombre', '$rut', '$asignatura')";

if ($conn->query($sql) === TRUE) {
    echo "La asistencia se ha registrado correctamente.";
} else {
    echo "Error al registrar la asistencia: " . $conn->error;
}

// Cerrar la conexión a la base de datos
$conn->close();
?>
