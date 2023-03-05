
let getal = prompt("Voer een getal in!");
// make a list and append

const numbers = [];



if (getal > 0) {
    for (var i = 1; i <= getal; i++) {
        if (i == 1) {
            numbers.push(i);
        }
        else {
            numbers.push(numbers[i - 2]+ "-" + i);
    
        }
        console.log(numbers);
    }
    
    for (var i = getal -1; i >= 1; i--) {
        if (i -1 == getal -1) {
    
        }
        else {
            numbers.push(numbers[i -1]);
        }
            
        console.log(numbers);
    }
    var elem = document.getElementById("antwoord");
    if(typeof elem !== 'undefined' && elem !== null) {
        console.log("De lijst is: " + numbers);
        for (var i = 0; i < numbers.length; i++) {
            elem.innerHTML += numbers[i] + "<br>";
        }
        
    }
    
}

