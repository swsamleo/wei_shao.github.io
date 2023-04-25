let progress = 0;

function updateProgress() {
  const progressBar = document.getElementById('progressBar');

  progress += 10;
  if (progress > 100) {
    progress = 0;
  }
  progressBar.style.width = progress + '%';
}
