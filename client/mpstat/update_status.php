<?php

$mypass = 'xxxxxx';

$password = $_POST['password'];
$contents = $_POST['contents'];

if ($password == $mypass) {
    $file_handle = fopen("./current_status.txt", "w");
    fwrite($file_handle, $contents);
    fclose($file_handle);
    echo "mpstat status updated.";
} else {
    echo "Password ERROR!!";
}
