<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title> usertop </title>
    <meta http-equiv="refresh" content="13">
  </head>
  <body style="color:#EEEEEE; background-color:#2D2D2D">
    <pre>
<?php
date_default_timezone_set('PRC');
$date_now = date('Y-m-d H:i:s',time());
echo "Refresh Time: " . $date_now . "\n";
echo file_get_contents('./current_status.txt');
?>
    </pre>
  </body>
</html>
