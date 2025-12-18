<?php include 'db/config.php'; ?>
<html>
<body>
<h2>Notices</h2>
<form method="POST">
  <input name="title" placeholder="Title" required>
  <textarea name="message"></textarea>
  <button name="add">Add Notice</button>
</form>

<?php
if (isset($_POST['add'])) {
  mysqli_query($conn, "INSERT INTO notices(title,message) VALUES('$_POST[title]','$_POST[message]')");
}

$result = mysqli_query($conn, "SELECT * FROM notices");
while ($row = mysqli_fetch_assoc($result)) {
  echo "<div><h3>{$row['title']}</h3><p>{$row['message']}</p>
        <a href='delete_notice.php?id={$row['id']}'>Delete</a></div>";
}
?>
</body>
</html>