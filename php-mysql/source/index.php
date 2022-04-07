<?php
const HOSTNAME = 'mysql';
const DATABASE = 'php_db';
const USERNAME = 'phper';
const PASSWORD = 'password';

try {

  $pdo = new PDO('mysql:host=' . HOSTNAME . ';dbname=' . DATABASE, USERNAME, PASSWORD);
  $msg = 'MySQLに接続成功！';

} catch (PDOException $e) {

  $msg  = 'MySQLへの接続失敗...<br>' . $e->getMessage();

}

echo $msg;