<?php 
    /**
     * a. Find mod of the two numbers.
        b. Find the power of first number raised to the second.
        c. Find the sum of first n numbers (considering first number as n)
        d. Find the factorial of second number.
        
     */

    function mod($a, $b){
        return $a%$b;
    }

    function power($a, $b){ 
        return pow($a, $b);
    }

    function sum($n){ 
        $sum = 0; 
        for($i=1; $i<=$n; $i++){ 
            $sum += $i;
        }
        return $sum;
    }
    

    function fact($n){ 
        $fact = 1;
        for($i=1; $i<=$n; $i++){ 
            $fact *= $i;
        }
        return $fact;
    }


    echo ( mod(5,2) . "<br>");
    echo (power(4,2) . "<br>");
    echo (sum(4) . "<br>");
    echo (fact(5). "<br>");
 


?>