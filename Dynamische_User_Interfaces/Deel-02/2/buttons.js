var button1 = document.getElementById("button1");
var button2 = document.getElementById("button2");
var button3 = document.getElementById("button3");
var container = document.getElementById("container");
var image = document.getElementById("image");
var image1 = document.getElementById("image1");
let a = 1;
let reverse = false;
// A function that changes the background image of the container and the image in the HTML
function changeBackgroundAndImage(url) {
  
  if (reverse == true) {
    if (a == 1) {
      reverse = false;
    }
    else {

      a -= 1;
      image.src = "images/bg" + a + ".jpg";
      image1.src = "images/" + a + ".jpg";
    }
  }
  else {
    if (a == 3) {
      reverse = true;
      image.src = "images/bg" + a + ".jpg";
      image1.src = "images/" + a + ".jpg";
    }
    else{
      image.src = "images/bg" + a + ".jpg";
      image1.src = "images/" + a + ".jpg";
      a += 1;
    }
  }

  console.log(a);
  }

function changecolors(a) {
button1.style.backgroundColor="green";
button2.style.backgroundColor="green";
button3.style.backgroundColor="green";
button1.disabled = false;
button2.disabled = false;
button3.disabled = false;
if (a == 1) {
  button1.style.backgroundColor="red";
  button1.disabled = true;
}
else if (a == 2) {
  button2.style.backgroundColor="red";
  button2.disabled = true;
}
else if (a == 3) {
  button3.style.backgroundColor="red";
  button3.disabled = true;
}

}
// A function that increases the value of a button by one
function increaseValue(button) {
  var value = parseInt(button.innerHTML);
  if (value == 1) {
    value--;
  }
  else {
    value++;
  }
  
  button.innerHTML = value;
}

// Add event listeners to each button to increase their value on click
button1.addEventListener("click", function() {
  increaseValue(button1);
  changeBackgroundAndImage(a);
  changecolors(1);
});
button2.addEventListener("click", function() {
  increaseValue(button2);
  changeBackgroundAndImage(a);
  changecolors(2);
});
button3.addEventListener("click", function() {
  increaseValue(button3);
  changeBackgroundAndImage(a);
  changecolors(3);
});