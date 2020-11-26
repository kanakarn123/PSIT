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
mysqli_real_connect($conn, 'labwebdata.mysql.database.azure.com', 'kanakarn@labwebdata', 'Jaoo01062544', 'itflab', 3306);
if (mysqli_connect_errno($conn))
{
    die('Failed to connect to MySQL: '.mysqli_connect_error());
}
$res = mysqli_query($conn, 'SELECT * FROM guestbook');
?>
    
<div class="container">
    <div class="form">
        <p class="ex1"><h1><center>What kind of drink do you like</center></h1></p>
    </div>
<table width="600" border="1" class="table table-dark table-striped" class="center">
  <thead>
      <tr class="active">
          <th width="250"> <div align="center">Name</div></th>
          <th width="600"> <div align="center">Answer </div></th>
          <th width="250"> <div align="center">Action </div></th>
      </tr>
    </thead>
<?php
while($Result = mysqli_fetch_array($res))
{
?>
  <tr>
    <td><center><?php echo $Result['name'];?></center></td>
    <td><center><?php echo $Result['comment'];?></center></td>
    <td><center><a href="formindexdata.html"><input type="submit" value="Change" class="btn-default"></a>&nbsp;&nbsp;<a href="formdeletedata.html"><input type="submit" value="Delete"  class="btn-default"></a></center></td>
  </tr>
<?php
}
?>
</table>
<a href="forminsertdata.html"><input type="Submit" value="ADD" class="btn-default btn-sm"></a>
<?php
mysqli_close($conn);
?>
</div>
</body>
</html>