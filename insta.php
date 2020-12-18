<html>
<head>
<title>run my python files</title>
<?PHP
if(isset($_POST['search'])){
	$par = $_POST['disease_name'];
	//$ret_val = exec('python test.py 2>&1', $par);
	//echo $ret_val;
	echo shell_exec("python insta.py $par");
	header("Location: home.php");
	return;
}
?>
</head>
<body>
	<form method="post">
		<input type="text" name="disease_name" value="">
		<input type="submit" name="search">
	</form>
</body>