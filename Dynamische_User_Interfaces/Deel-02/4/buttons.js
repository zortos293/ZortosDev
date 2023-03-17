const btnSize = "80px";
const containerBackgroundColor = "gray";
const container = document.getElementById("container");
let html = "";
const numbers = Array.from(Array(30), (_, i) => i + 1);
const colors = ["green", "red", "purple", "blue", "black"];

const numRows = Math.ceil(numbers.length / 5);
const numCols = 5;

for (let i = 0; i < numRows; i++) {
  const row = document.createElement("div");

  for (let j = 0; j < numCols; j++) {
    const index = i * numCols + j;
    if (index >= numbers.length) break;

    const button = document.createElement("button");
    button.style.backgroundColor = colors[0]; // Default color is green
    button.style.width = btnSize;
    button.style.height = btnSize;
    button.innerHTML = numbers[index];

    button.addEventListener("click", function () {
      // Find current color index and increment by 1
      const currColorIndex = parseInt(button.getAttribute("data-clicks"));
      
      // Update button style and data attribute
      button.style.backgroundColor = colors[currColorIndex];
      if (currColorIndex === 5) {
        button.remove();
      }
      button.setAttribute("data-clicks", currColorIndex +1);

      // Remove button after 5 clicks
      
    });

    // Set initial data click count attribute to 0
    button.setAttribute("data-clicks", 0);

    row.appendChild(button);
  }

  container.appendChild(row);
}

container.style.backgroundColor = containerBackgroundColor;
