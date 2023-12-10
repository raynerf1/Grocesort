 <?php
// If the request is made from our space preview functionality then turn on PHP error reporting
/*
if (isset($_SERVER['HTTP_X_FORWARDED_URL']) && strpos($_SERVER['HTTP_X_FORWARDED_URL'], '.w3spaces-preview.com/') !== false) {
  ini_set('display_errors', 1);
  ini_set('display_startup_errors', 1);
  error_reporting(E_ALL);
}
*/
define('DB_HOST', 'HOSTDEBASEDEDATOS');
define('DB_NAME', 'NOMBREDEBASEDEDATOS');
define('DB_CHARSET', 'utf8');
define('DB_USER', 'USUARIODEBASEDEDATOS');
define('DB_PASSWORD', 'CONTRASENADEBASEDEDATOS');
?>