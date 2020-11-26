<?php

$conn = mysqli_init();
mysqli_real_connect($conn, 'labwebdata.mysql.database.azure.com', 'kanakarn@labwebdata', 'Jaoo01062544', 'itflab', 3306);
if (mysqli_connect_errno($conn))
{
    die('Failed to connect to MySQL PLEASE TRY AGAIN: '.mysqli_connect_error());
}

$name = $_POST['name'];
$comment = $_POST['comment'];


$sql = "DELETE FROM guestbook WHERE Name='$name'";

if (mysqli_query($conn, $sql)) {
  header("Location: showdata.php");
  } else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
  }
  
mysqli_close($conn);
?>