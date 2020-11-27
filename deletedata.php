<?php

$conn = mysqli_init();
mysqli_real_connect($conn, 'jaootest.mysql.database.azure.com', 'kanakarn@jaootest', 'Jaoo01062544', 'itflab', 3306);
if (mysqli_connect_errno($conn))
{
    die('Failed to connect to MySQL PLEASE TRY AGAIN: '.mysqli_connect_error());
}

$id = $_GET['id'];
$sql = "DELETE FROM guestbook WHERE id = '$id'";



if (mysqli_query($conn, $sql)) {
    echo "Success " . $sql . "<br>" . mysqli_error($conn);
  } else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
  }
  
mysqli_close($conn);
?>