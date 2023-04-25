---
layout: single
title: "fancy ui"
permalink: /fancy_UI/
---

<!-- Include your CSS styles here -->
<style>
body {
  font-family: Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 100vh;
  margin: 0;
}

.progress-bar-container {
  width: 100%;
  max-width: 400px;
  height: 30px;
  background-color: #f3f3f3;
  border-radius: 5px;
}

.progress-bar {
  height: 100%;
  width: 0;
  background-color: #4CAF50;
  border-radius: 5px;
  transition: width 0.4s ease-in-out;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Progress Bar</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="progress-bar-container">
    <div class="progress-bar" id="progressBar"></div>
  </div>
  <button onclick="updateProgress()">Update Progress</button>
  <script src="script.js"></script>
</body>
</html>

<script>
let progress = 0;

function updateProgress() {
  const progressBar = document.getElementById('progressBar');

  progress += 10;
  if (progress > 100) {
    progress = 0;
  }
  progressBar.style.width = progress + '%';
}
</script>