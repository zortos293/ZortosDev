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
  changeBackgroundAndImage(a,reverse);
});
button2.addEventListener("click", function() {
  increaseValue(button2);
  changeBackgroundAndImage(a,reverse);
});
button3.addEventListener("click", function() {
  increaseValue(button3);
  changeBackgroundAndImage(a,reverse);
});