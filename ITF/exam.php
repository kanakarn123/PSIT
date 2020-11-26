<?php

$conn = mysqli_init();
mysqli_real_connect($conn, 'ihost.it.kmitl.ac.th', 'it63070015_it63070015', 'Jaoo01062544', 'it63070015_jaoo', 3306);
if (mysqli_connect_errno($conn))
{
    die('Failed to connect to MySQL: '.mysqli_connect_error());
}


$A = $_POST['A'];
$B = $_POST['B'];


$sql = "INSERT INTO guestbook (A , B) VALUES ('$A', '$B')";


if (mysqli_query($conn, $sql)) {
    header("Location: showexample.php");
  } else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
  }

mysqli_close($conn);
?>