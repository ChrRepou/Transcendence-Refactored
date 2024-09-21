console.log("login page");

const loginButton = document.querySelector("#login-btn");
console.log("login button:", loginButton);

let state = {
  email: "",
  password: "",
};

const emailInput = document.querySelector("#email");
const passwordInput = document.querySelector("#password");

const onEmailChange = (event) => {
  state.email = event.target.value;
  console.log("email:", state.email);
};

const onPasswordChange = (event) => {
  state.password = event.target.value;
  console.log("password:", state.password);
};

