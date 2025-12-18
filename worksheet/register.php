<?php include 'db/config.php'; ?>
<html>
<body>
<form method="POST">
  <input name="username" placeholder="Username" required><br>
  <input name="email" type="email" placeholder="Email" required><br>
  <input name="password" type="password" required><br>
  <button name="register">Register</button>
</form>

<?php
if (isset($_POST['register'])) {
  $u = $_POST['username'];
  $e = $_POST['email'];
  $p = password_hash($_POST['password'], PASSWORD_DEFAULT);

  $check = mysqli_query($conn, "SELECT * FROM users WHERE username='$u'");
  if (mysqli_num_rows($check) > 0) {
    echo "Username already exists";
  } else {
    mysqli_query($conn, "INSERT INTO users(username,email,password) VALUES('$u','$e','$p')");
    echo "Registration successful";
  }
}
?>
</body>
</html>