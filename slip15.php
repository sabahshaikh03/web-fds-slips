<?php 
    $str = "i'm title case HEKKOOO"; 

    $title = ucwords(strtolower($str));
    echo $title. "\n";

    $pad = str_pad($str, strlen($str)+4, "*", STR_PAD_BOTH);
    echo $pad ."\n";

    $rev = strrev("$str"); 
    echo $rev. "\n";
?>