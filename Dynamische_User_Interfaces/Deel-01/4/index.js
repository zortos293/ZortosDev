// create a question
let bestelling = new Object()
let producten = ["fris", "bier", "wijn"];
while (true) {
    let questionmain = prompt("wat wilt u bestellen? (stop om te stoppen)");
    if (questionmain == "stop") {
        break;
    }
    if (order(questionmain,bestelling,producten) != true) {
        alert("U heeft een ongeldige invoer gedaan.");
    }
}
alert(print_bon(bestelling));





function order(Vraag, bestellings,producten) {
    console.log(Vraag)
    if (producten.includes(Vraag)) {
        var hoeveel = parseInt(prompt("Hoeveel wilt u er bestellen?"));
        bestellings[Vraag] = hoeveel;
        return true;
    } else {
        return false;
    }
    
}

function print_bon(dict) {
    var bon = "Bon:\n";
    let a  = Object.keys(dict);
    a.forEach(element => {
        bon += element + ": " + dict[element] + "\n";
    });
    return bon;
}
