<?php

// a. Find whether the small string appears at the start of the large string.
// b. Find the position of the small string in the big string.
// c. Compare both the string for first n characters, also the comparison should not be case 

// hellothisisme
// hello
$str1 = $_POST['str1'];
$str2 = $_POST['str2']; 
$n = $_POST['n'];
$op = $_POST['op'];  // 


switch($op){ 
    case 1: 
        $size = strlen($str2);
        $sliced = substr($str1, 0, $size);
        if(strcmp($str2, $sliced) == 0)
            echo "String appears at first";
        else 
            echo "not appears";
        break;

    case 2: 
        $pos = strpos($str1, $str2); 
        if($pos)
        echo "Pos is $pos";
        else 
            echo "not found";
        break; 

    case 3: 
        $slice1 = substr($str1, 0, $n);
        $slice2 = substr($str2, 0, $n);

        if(strcasecmp($slice1, $slice2) == 0){ 
            echo "same";
        }
        else 
            echo "Not same";
        break;
        
}

?>