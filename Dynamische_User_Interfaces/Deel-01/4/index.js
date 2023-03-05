// create a question
let bestelling = new Object()

while (true) {
    let questionmain = prompt("wat wilt u bestellen? (stop om te stoppen)");
    if (questionmain == "stop") {
        break;
    }
    if (order(questionmain,bestelling) != true) {
        alert("U heeft een ongeldige invoer gedaan.");
    }
}
alert(print_bon);

for(var i in bestelling)
{
    alert(i + " = " + bestelling[i]);
}



function order(Vraag, bestellings) {
    if (Vraag == "fris") {
        var hoeveel = parseInt(prompt("Hoeveel wilt u er bestellen?"));
        bestellings["fris"] += hoeveel;
        return true;
    } else if (Vraag == "bier") {
        var hoeveel = prompt("Hoeveel wilt u er bestellen?");
        bestellings.bier = bestellings.bier + hoeveel;
        return true;
    } else if (Vraag == "wijn") {
        var hoeveel = prompt("Hoeveel wilt u er bestellen?");
        bestellings.wijn = bestellings.wijn + hoeveel;
        return true;
        
    } else {
        return false;
    }
    
}

function print_bon(dict) {
    var bon = "Bon:\n";
    for (var key in dict) {
        if (dict[key] > 0) {
            bon += key + ": " + dict[key] ;
    
        }
    }
    return bon;
}
