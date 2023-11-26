<?php 

    $fp = fopen("student.dat", "r");
    
    $counter = -1;
    $data = array() ;
     /*
      {[1,dkjf, 90], []}
     */
    while(!feof($fp)){

        if($counter == -1)
            $str = fgets($fp);
        else { 
            $str = fgets($fp); 
            $ex = explode(" ", $str);
            // calculate per
            $ex = calculate($ex); 
            
            
            $data[$counter] = $ex;

        }

        $counter++;


    }   

    function calculate($data){ 
        $sum = 0; 
        for($i=2; $i<count($data); $i++){ 
            $sum += $data[$i];
        }
        $per  = $sum / 6; 
        

        array_push($data, $per);
        return $data;
    }



    // table 

    echo "<table border=1>"; 
        for($i=0; $i<count($data); $i++){
            echo "<tr>";
                for($j=0; $j<9; $j++){
                    echo "<td>".$data[$i][$j]. "</td>";
                }
            echo "</tr>";
        }
    echo "<table/>";

    //unlink
    // 
?>