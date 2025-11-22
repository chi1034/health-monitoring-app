const API_URL = "https://health-monitoring-backend.up.railway.app";

// Signup
async function signup() {
  const email = document.getElementById("signupEmail").value;
  const password = document.getElementById("signupPassword").value;

  const response = await fetch(`${API_URL}/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  if (response.ok) {
    const data = await response.json();
    alert("Signup successful for " + data.email);
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

  const response = await fetch(`${API_URL}/login`, {
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
