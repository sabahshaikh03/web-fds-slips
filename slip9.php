<?php 

/**
 * 
 * a. Split the string into separate words using the given separator.
 *b. Replace all the occurrences of separator in the given string with some other separator.
 * c. Find the last word in the given string.
 */
$str = $_POST['str1'];
$op = $_POST['op'];
$operator = $_POST['operator'];

switch ($op) {
    case 1:
        $sep = explode($operator, $str);
        print_r($sep[0]);
        break;
    
    case 2 : 
            if(strcmp($operator, "&") == 0)
                $replace = str_replace($operator, "#", $str);
            else 
                $replace = str_replace($operator, "&", $str);

            echo "$replace";

            break;
    case 3: 
        $sep = explode($operator, $str);
        $size = count($sep); 
        print( $sep[$size-1]);
        break;
    default:
        # code...
        break;
}


?>