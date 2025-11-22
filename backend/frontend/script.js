// Signup
async function signup() {
  const email = document.getElementById("signupEmail").value;
  const password = document.getElementById("signupPassword").value;

  const response = await fetch("http://127.0.0.1:8000/signup", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  if (response.ok) {
    const data = await response.json();
    alert("Signup successful for " + data.email);
    // Redirect to login page after signup
    window.location.href = "login.html";
  } else {
    const error = await response.json();
    alert("Signup failed: " + error.detail);
  }
}

// Login
async function login() {
  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  const response = await fetch("http://127.0.0.1:8000/login", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `username=${encodeURIComponent(email)}&password=${encodeURIComponent(password)}`
  });

  if (response.ok) {
    const data = await response.json();
    localStorage.setItem("token", data.access_token);
    localStorage.setItem("user_email", email);
    alert("Login successful!");
    window.location.href = "dashboard.html";
  } else {
    const error = await response.json();
    alert("Login failed: " + error.detail);
  }
}
