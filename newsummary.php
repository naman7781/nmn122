<!DOCTYPE html>
<html>
<head>
	<title>Summary</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
	<link rel="stylesheet" href="styles.css">
</head>
<body>
	<div class="topnav" style="padding: 1% 0;">
		<h2 style="text-align: center;">BTP Project</h2>
		<h3 style="text-align: center;padding-bottom: 2%;">Web Scrapper and Text Summarization</h3>
	</div>
	<form method="post">
	<div class="jkl" style="margin: 3%">
		<h5>Summary :</h5>
		<?php
		$myfile = fopen("summary1.txt", "r") or die("Unable to open file!");
		echo fread($myfile,filesize("summary1.txt"));
		fclose($myfile);
		?>
		
	</div>

</form>
</body>
</html>
