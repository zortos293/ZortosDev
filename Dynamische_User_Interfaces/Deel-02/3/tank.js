var image = document.getElementById("image");

document.onkeydown = checkKey;
image.style.transform = "rotate(90deg)"
let animations = [164, 332, 500, 668, 836, 1004, 1172, 1340];
let shootingAnimation  = [332,420,500,580];
let animationNr = 0;
image.style.left = 0 + "px";
image.style.top = 0 + "px";
function playShootAnimation(){
    let i = 0;
    let shootAnimationInterval = setInterval(() => {
         image.style.backgroundPosition = shootingAnimation[i] + `px 500px`;
        i++;
        if(i == shootingAnimation.length){
             clearInterval(shootAnimationInterval);
            image.style.backgroundPosition = '0px 0px';
        }
    }, 200);
}
function checkKey(e) {
	console.log("key nr = " + e.keyCode);
    e = e || window.event;
// keycode for space
    if (e.keyCode == 32) {
        console.log("space");
        // make the tank shoot
        playShootAnimation();

    } 
    else if (e.keyCode == 38) { // up arrow
		console.log("up arrow");
		image.style.transform = "rotate(0deg)";
        image.style.backgroundPosition = animations[animationNr] + `px 0px`;
		image.style.top = (parseInt(image.style.top) - 10) + "px";
        if (animationNr >= animations.length - 1) {
			animationNr = 0;
		} else {
			animationNr++;
		}
	} else if (e.keyCode == 40) { // down arrow
		console.log("down arrow");
		image.style.transform = "rotate(180deg)";
		image.style.top = (parseInt(image.style.top) + 10) + "px";
        image.style.backgroundPosition = animations[animationNr] + `px 0px`;
        if (animationNr >= animations.length - 1) {
			animationNr = 0;
		} else {
			animationNr++;
		}
	} else if (e.keyCode == 37) { // left arrow
		console.log("left arrow");
		image.style.transform = "rotate(-90deg)";
		image.style.backgroundPosition = animations[animationNr] + `px 0px`;
		image.style.left = (parseInt(image.style.left) - 10) + "px";
		if (animationNr >= animations.length - 1) {
			animationNr = 0;
		} else {
			animationNr++;
		}
	} else if (e.keyCode == 39) { // right arrow
		console.log("right arrow");
		image.style.transform = "rotate(90deg)";
		image.style.backgroundPosition = animations[animationNr] + `px 0px`;
		image.style.left = (parseInt(image.style.left) + 10) + "px";
		if (animationNr >= animations.length - 1) {
			animationNr = 0;
		} else {
			animationNr++;
		}
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
