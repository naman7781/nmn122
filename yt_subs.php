<html>
<head>
<title>run my python files</title>
<?PHP
if(isset($_POST['search'])){
	$par = $_POST['disease_name'];
	//$ret_val = exec('python test.py 2>&1', $par);
	//echo $ret_val;
	echo shell_exec("python ytsubs.py $par");
	header("Location: yt_subs.php");
	return;
}
?>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
<link rel="stylesheet" href="styles.css">
</head>
<body>
	<div class="topnav" style="padding: 1% 0;">
		<h2 style="text-align: center;">BTP Project</h2>
		<h3 style="text-align: center;padding-bottom: 2%;">Web Scrapper and Text Summarization</h3>
	</div>
	<form method="post">
			<h4 style="text-align: center;margin-top: 6%">Write your query below. This will download all the video transcripts in your dekstop folder.</h4>
	<div class="jkl">
		<h5 style="display: inline-block;">Query :</h5>
		<input type="text" name="disease_name" value="">
		<input type="submit" name="search">
	</div>
</form>
</body>
