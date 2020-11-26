<html>
<head>
<title>A B C</title>
<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>

</head>
<body>
<?php
$conn = mysqli_init();
mysqli_real_connect($conn, 'geedy.mysql.database.azure.com', 'geedy@geedy', 'PuiFai2023', 'exam', 3306);
if (mysqli_connect_errno($conn))
{
    die('Failed to connect to MySQL: '.mysqli_connect_error());
}
$res = mysqli_query($conn, 'SELECT * FROM guestbook');
?>
<div class="container">
    <div class="form">
        <p class="ex1"><h1><center>A B C</center></h1></p>
    </div>
  <table width="900" border="1" class="table table-hover table-striped" class="center" >
    <thead class="thead-pink">
    <tr bgcolor="pink" class="active">
      <th width="300"> <div align="center">A</div></th>
      <th width="300"> <div align="center">B</div></th>
      <th width="300"> <div align="center">C</div></th>
    </tr>
     </thead>
  <?php
while($Result = mysqli_fetch_array($res))
{
    $sum = 0
?>
  <tr>
    <td><center><?php echo $Result['A'];?></center></td>
    <td><center><?php echo $Result['B'];?></center></td>
    <td><center><?php echo $sum = $Result['A'] + $Result['B'];?></center></td>
  </tr>
<?php
}
?>
</table>
<a href="abc_insert.html"><input type="submit" value="ADD" class="btn-default btn-sm"></a>
<?php
mysqli_close($conn);
?>
</body>
</html>