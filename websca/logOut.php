<?PHP //echo "<!-- Modified: Date       = 2014 Jan 22 -->\n"; ?>
<?PHP
#Close session
session_start();
session_destroy();
header('Location: http://localhost/sca/login.php');
?>
