<?php

$nombre = $_POST['nombre'];
$email = $_POST['email'];
$mensaje = $_POST['mensaje'];
$para = 'fcoramirezz@gmail.com';
$titulo = 'Enviado desde vinculacionunach.cl';
$header = 'From: ' . $email;
$msjCorreo = "Nombre: $nombre\n E-Mail: $email\n Mensaje:\n $mensaje";


if (mail($para, $titulo, $msjCorreo, $header)) {
	echo "<script language='javascript'>
	alert('Mensaje enviado, muchas gracias.');
	window.location.href = 'http://www.google.cl';
	</script>";
} else {
	echo 'Falló el envio';
}

?>