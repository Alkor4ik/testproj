<?
    //print_r($_POST);
//Сообщение для пользователя
    $to = $_POST['email'];
    $subject_for_user = 'Заказ в магазине';
    $from = 'sergey.opanasenko@gmail.com';    
    $message_for_user = "Вы сделали заказ в магазине!\r\nМенеджер свяжется с Вами в ближайшее время";   
    $headers = "From: $from\r\nReplay-to: $from\r\nContent-type:text/plain; charset:utf-8\r\n";
    mail($to, $subject_for_user, $message_for_user, $headers);

//Сообщение для администратора
	$admin_email = 'sergey.opanasenko@gmail.com';
	$name = $_POST['name'];
	$email_user = $_POST['email'];
	$message = $_POST['message'];
    $phone = $_POST['phone'];
	$subject_for_admin = 'Новый заказ';
	$message_for_admin = "Сформирован новый заказ!\r\n Имя: $name\r\n Телефон: $phone\r\n Почта: $email_user\r\nСообщение от пользователя:\r\n $message";
	$headers = "From: $from\r\nReplay-to: $from\r\nContent-type:text/plain; charset:utf-8\r\n";
	mail($admin_email, $subject_for_admin, $message_for_admin, $headers);

	echo "<!DOCTYPE html>
	<html>
	<head>
	<meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\">
	<title>Form_reguest</title>
	</head>
	<body>
		<center>
		<p>Ваш заказ оформлен!</p> 
		<a href='index.html'>Перейти на главную</a>
		</center>
	</body>
	</html>";
?>