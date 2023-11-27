<?php 

    // $str = $_POST['serial']; 

    // $serial = explode (" ", $str); 

    $serial = [1,2,3,4,5]; 
    $per = [99, 98, 97, 96, 38]; 
    $sub = ["maths", "maths", "maths", "maths", "maths"]; 





    echo "<table border=1>"; 

    echo "<tr>";
        for($i=0; $i<5; $i++){ 
            echo "<td>$serial[$i] </td>";
        }
    echo "</tr>";
    echo "<tr>";
        for($i=0; $i<5; $i++){ 
            echo "<td>$per[$i] </td>";
        }
    echo "</tr>";
    echo "<tr>";
        for($i=0; $i<5; $i++){ 
            echo "<td>$sub[$i] </td>";
        }
    echo "</tr>";
    echo "<tr>";
        for($i=0; $i<5; $i++){ 
            echo "<td>".grade($per[$i]). " </td>";
        }
    echo "</tr>";

    echo "</table>"; 

    // 0,1,2,3,4,5
    /// 5,2,1,0,4,3
    // result[5] = array[5];
    // result[2]

    /*
        $r =rand(0, count(arr)); 
        arr[$r];
        arr[$r];
        arr[$r];
        arr[$r];


        $neArr = array_filter($array, function ($value){
            return $alue%2 == 0;
        })
    */
    function grade($m){ 
        if($m>90)
            return "A"; 
        else
            return "B";
    }

?>