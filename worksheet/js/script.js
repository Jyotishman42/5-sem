function calculator(a, b, op) {
  if (op === '+') return a + b;
  if (op === '-') return a - b;
}

function addPara() {
  let p = document.createElement("p");
  p.innerText = "New paragraph added";
  document.getElementById("box").appendChild(p);
}

function randomNumber() {
  document.getElementById("rand").innerText = Math.floor(Math.random()*10)+1;
}

function validatePassword() {
  let p1 = document.getElementById("pass").value;
  let p2 = document.getElementById("cpass").value;
  if (p1 === p2) alert("Success");
  else alert("Passwords do not match");
}