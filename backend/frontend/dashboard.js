function checkAuth() {
  if (localStorage.getItem("isLoggedIn") !== "true") {
    alert("Please login first.");
    window.location.href = "index.html";
  }
}

// Health readings
let readings = JSON.parse(localStorage.getItem("healthReadings")) || [];

const ctx = document.getElementById('healthChart').getContext('2d');
let healthChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: readings.map(r => r.date),
    datasets: [
      {
        label: 'Blood Sugar',
        data: readings.map(r => r.bloodSugar),
        borderColor: 'red',
        fill: false
      },
      {
        label: 'Blood Pressure',
        data: readings.map(r => r.bloodPressure),
        borderColor: 'blue',
        fill: false
      }
    ]
  }
});

function addReading() {
  const sugar = document.getElementById('bloodSugar').value;
  const pressure = document.getElementById('bloodPressure').value;
  const today = new Date().toISOString().split('T')[0];

  if (sugar && pressure) {
    readings.push({ date: today, bloodSugar: parseInt(sugar), bloodPressure: parseInt(pressure) });
    localStorage.setItem("healthReadings", JSON.stringify(readings));

    healthChart.data.labels.push(today);
    healthChart.data.datasets[0].data.push(parseInt(sugar));
    healthChart.data.datasets[1].data.push(parseInt(pressure));
    healthChart.update();
  }
}
