<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
	<style>
		body {
			background-image: url("night.png");
			background-repeat: no-repeat;
			background-size: cover;
		}
		h1 {
			text-align: center;
			margin-top: 100px;
			font-size: 50px;
			color: white;
		}
	</style>
</head>
<body>
	<h1 id="greeting"></h1>
	<?php
		$hour = date("G");
		if ($hour < 6) {
			$greeting = "Goede nacht";
			echo '<style>body {background-image: url("night.png");}</style>';
		}
		else if ($hour < 12) {
			$greeting = "Goede morgen";
			echo '<style>body {background-image: url("morning.png");}</style>';
		}
		else if ($hour < 18) {
			$greeting = "Goede middag";
			echo '<style>body {background-image: url("afternoon.png");}</style>';
		}
		else {
			$greeting = "Goede avond";
			echo '<style>body {background-image: url("evening.png");}</style>';
		}
		echo '<script>document.getElementById("greeting").innerHTML = "'.$greeting.'";</script>';
	?>
</body>
</html>