<html>
<head>
<title>ITF Lab</title>
<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
<?php
$conn = mysqli_init();
mysqli_real_connect($conn, 'puifai.mysql.database.azure.com', 'puifai@puifai', 'Aa12345678', 'ITFLab', 3306);
if (mysqli_connect_errno($conn))
{
    die('Failed to connect to MySQL: '.mysqli_connect_error());
}
$res = mysqli_query($conn, 'SELECT * FROM guestbook');
?>
<div class="container">
    <div class="form">
        <p class="ex1"><h1><center>How do you feel?</center></h1></p>
    </div>
  <table width="800" border="1" class="table table-pink table-hover table-striped" class="center" >
    <thead class="thead-pink">
    <tr bgcolor="pink" class="active">
      <th width="200"> <div align="center">Name</div></th>
      <th width="500"> <div align="center">Comment</div></th>
      <th width="100"> <div align="center">Action</div></th>
    </tr>
     </thead>
  <?php
while($Result = mysqli_fetch_array($res))
{
?>
  <tr>
    <td><center><?php echo $Result['Name'];?></center></td>
    <td><center><?php echo $Result['Comment'];?></center></td>
    <td><center><a href="index.html"><input type="submit" value="Edit" class="btn btn-warning"></a>&nbsp;&nbsp;<a href="delete.html"><input type="submit" value="Delete"  class="btn btn-danger"></a></center></td>  </tr>
<?php
}
?>
</table>
<a href="insert.html" class="btn btn-success mb-3">Add+</a>
<?php
mysqli_close($conn);
?>
</body>
</html>