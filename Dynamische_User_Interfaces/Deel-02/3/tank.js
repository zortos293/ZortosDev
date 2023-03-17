var image = document.getElementById("image");

document.onkeydown = checkKey;
image.style.transform = "rotate(90deg)"
let animations = [164, 332, 500, 668, 836, 1004, 1172, 1340];
let animationNr = 0;
function checkKey(e) {
	console.log("key nr = " + e.keyCode);
    e = e || window.event;
    if(e.keyCode == 32){
    	console.log("spacebar");
    } else if (e.keyCode == '38') {
          // up arrow
        console.log("Up arrow");
    } else if (e.keyCode == '40') { // down arrow
        console.log("down arrow");
    } else if (e.keyCode == '37') { // left arrow
    	console.log("left arrow");
    } else if (e.keyCode == '39') {   // right arrow
    	console.log("right arrow");
    	image.style.backgroundPosition = animations[animationNr] + `px 0px`; // check goed de rupsband
        
        if (animationNr == 7)
        {
            animationNr = 0;
        }
        console.log(animationNr);
        animationNr++;
    }
}
// animation + 168px 0px
// animation 0 = 164px 0px
// animation 1 = 332px 0px
// animation 2 = 500px 0px
// animation 3 = 668px 0px
// animation 4 = 836px 0px
// animation 5 = 1004px 0px
// animation 6 = 1172px 0px
// animation 7 = 1340px 0px
