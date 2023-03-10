var button1 = document.getElementById("button1");
var button2 = document.getElementById("button2");
var button3 = document.getElementById("button3");
var container = document.getElementById("container");
var image = document.getElementById("image");
let a = 0;
// A function that changes the background image of the container and the image in the HTML
function changeBackgroundAndImage(url) {
if (a => 3) {
  image.src = "images/" + url + ".jpg";
  
}
image.src = "images/" + url + ".jpg";
a += 1;
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
});
button2.addEventListener("click", function() {
  increaseValue(button2);
  changeBackgroundAndImage(a);
});
button3.addEventListener("click", function() {
  increaseValue(button3);
  changeBackgroundAndImage(a);
});