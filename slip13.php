
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>hellowwww mf</title>
    <style>
        td{
            width:50px;
            height: 50px;
        }
        .light{ 
            background-color : #f1f1f1;
        }
        .dark { 
            background-color: #333;
        }
    </style>
</head>
<body>
    <table>
    <?php
/**
 *  Write a PHP script to create a chess board using CSS on table cells
 */
    for($row=1; $row<=8; $row++){ 
        echo "<tr>";
            for($col=1; $col<=8; $col++){ 
                $classname = ($row+$col) %2 == 0 ? "light" : "dark";
                echo "<td class=$classname></td>";
            }
        echo "</tr>";
    }


?>
    </table>
</body>
</html>





