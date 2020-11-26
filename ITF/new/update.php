<?php
$id=$_GET['ID'];
$conn = mysqli_init();
mysqli_real_connect($conn, 'phufarpsw.mysql.database.azure.com', 'phufarpsw@phufarpsw', 'EMLbmk28', 'itflab', 3306);
$name=$_POST['Name'];
$comment=$_POST['Comment'];
$link=$_POST['Link'];
$sql="UPDATE guestbook SET Name='$name',Comment='$comment',Link='$link' WHERE ID='$id'";
if (mysqli_query($conn, $sql)) {
    header("Location: show.php");
  } else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
  }
mysqli_close($conn);
?>
