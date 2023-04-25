---
layout: fancy
title: "fancy ui"
permalink: /fancy_UI/
author_profile: false
---

<!-- Include your CSS styles here -->
<style>
body, html {
  margin: 0;
  height: 100%;
  background-color: #000; /* Add this line to set the background color to black */
}

.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.progress-percentage {
  font-size: 24px;
  font-weight: bold;
  fill: #0CFFFD;
}
</style>


<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Moving Circle Segment</title>
</head>
<body>
  <div class="container">
    <div class="progress">
      <svg class="progress-circle" width="400" height="200">
        <circle cx="100" cy="100" r="80" stroke="#0CFFFD" stroke-width="1" fill="None"></circle>
        <circle cx="100" cy="100" r="75" stroke="#0CFFFD" stroke-width="3.5" fill="None"></circle>
        <circle cx="100" cy="100" r="68" stroke="#0CFFFD" stroke-width="2.5" fill="None"></circle>
        <circle cx="100" cy="100" r="63.5" stroke="#047F86" stroke-width="2" fill="None"></circle>
        <path id="arc" d="" stroke="#0CFFFD" stroke-width="3" fill="none"></path> // fixed thin
        <path id="arc1" d="" stroke="#0CFFFD" stroke-width="3" fill="none"></path> // mid fix
        <path id="arc2" d="" stroke="#0CFFFD" stroke-width="3" fill="none"></path> //moving mid
        <path id="arc3" d="" stroke="#0CFFFD" stroke-width="3" fill="none"></path> //thin fix
        <path id="arc4" d="" stroke="#047F86" stroke-width="2.5" fill="none"></path>
        <path id="arc5" d="" stroke="#047F86" stroke-width="2.5" fill="none"></path>
        <path id="arc6" d="" stroke="#047F86" stroke-width="2.5" fill="none"></path>
        <path id="arc7" d="" stroke="#047F86" stroke-width="2.5" fill="none"></path>
        <path id="arc8" d="" stroke="#0CFFFD" stroke-width="1" fill="none"></path>
        <path id="arc9" d="" stroke="#0CFFFD" stroke-width="1" fill="none"></path>
        <path id="arc10" d="" stroke="#0CFFFD" stroke-width="1" fill="none"></path>
        <path id="arc11" d="" stroke="#0CFFFD" stroke-width="1" fill="none"></path>
        <g id="arcs"></g>
        <text class="progress-percentage" x=77 y=100 dy=".3em" id="progress-percentage">0%</text>
        <text x=180 y=70 dy=".3em" fill="#0CFFFD" font-size="18px" font-weight="bold"> LOADING ... </text>
        <rect x = 180 y = 80 width="200" height="40" fill="White"></rect>
        <rect x = 180 y = 80 id="sword-progress" width="200" height="40" fill="#0CFFFD"></rect>
        <path d="M 146.64,35 L 250,35 L 265,40 L 152.92, 40" stroke="#378089" fill="none" stroke-width="1"/>
        <path d="M 152.92,40 L 305,40 L 330,65 L 365, 65 L 380, 80 L 380 120 L 372, 128 L310 ,128 L 295, 143 L167.47, 143" stroke="#0CFFFD" fill="none" stroke-width="2"/>
        <path d="M 158.09,45 L 300,45 L 325,70 L360,70 L365,75 L320, 75 L300, 55 L 166.14, 55" stroke="#0CFFFD" fill="#0CFFFD" stroke-width="1"/>
        <path d="M 176.32,124 L 370,124" stroke="#0CFFFD" fill="none" stroke-width="3"/>
        <path d="M 190, 124 L 201,135 L 290,135 L301, 124" stroke="#0CFFFD" fill="none" stroke-width="5"/>
      </svg>
<!--      <svg class="progress-sword" viewBox="-100 -100 300 40" preserveAspectRatio="none"> &lt;!&ndash; Update this line &ndash;&gt;-->
<!--        <rect width="200" height="40" fill="White"></rect> &lt;!&ndash; Replace the polygon with a rectangle element &ndash;&gt;-->
<!--        <rect id="sword-progress" width="200" height="40" fill="#0CFFFD"></rect> &lt;!&ndash; Replace the polygon with a rectangle element &ndash;&gt;-->
<!--      </svg>-->
    </div>
  </div>
</body>
</html>

<script>
const arc = document.getElementById('arc');
const arc1 = document.getElementById('arc1');
const arc2 = document.getElementById('arc2');
const arc3 = document.getElementById('arc3');
const arc4 = document.getElementById('arc4');
const arc5 = document.getElementById('arc5');
const arc6 = document.getElementById('arc6');
const arc7 = document.getElementById('arc7');

const arc8 = document.getElementById('arc8');
const arc9 = document.getElementById('arc9');
const arc10 = document.getElementById('arc10');
const arc11 = document.getElementById('arc11');

const progressPercentage = document.getElementById('progress-percentage');

const arcs = document.getElementById('arcs');


const swordProgress = document.getElementById('sword-progress');

for (let i = 0; i < 100; i++) {
  const arcSegment = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  const startAngle = i * 3.6;
  const endAngle = startAngle + 3.6;
  const arcPath = describeArc(100, 100, 50, startAngle, endAngle);
  arcSegment.setAttribute('d', arcPath);
  arcSegment.setAttribute('stroke', '#00959B');
  arcSegment.setAttribute('stroke-width', '10');
  arcSegment.setAttribute('fill', 'none');
  arcSegment.style.display = 'none';
  arcs.appendChild(arcSegment);
}

function describeArc(x, y, radius, startAngle, endAngle) {
  const gapAngle = 1; // Add this line to define the gap angle between segments
  const start = polarToCartesian(x, y, radius, endAngle - gapAngle); // Update this line to subtract gapAngle
  const end = polarToCartesian(x, y, radius, startAngle + gapAngle); // Update this line to add gapAngle

  const largeArcFlag = endAngle - startAngle <= 180 ? '0' : '1';

  const d = [
    'M', start.x, start.y,
    'A', radius, radius, 0, largeArcFlag, 0, end.x, end.y,
  ].join(' ');

  return d;
}


function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
  const angleInRadians = (angleInDegrees - 90) * Math.PI / 180.0;
  return {
    x: centerX + radius * Math.cos(angleInRadians),
    y: centerY + radius * Math.sin(angleInRadians),
  };
}


let currentAngle_1 = 0;
let currentAngle_2 = 0;
let currentAngle_3 = 0;


function updateArc() {
  currentAngle_1 += 360 / (10 * 60); // 360 degrees / (5 seconds * 60 frames)
  currentAngle_2 += 360 / (6 * 60); // 360 degrees / (5 seconds * 60 frames)
  currentAngle_3 += 360 / (3.5 * 60); // 360 degrees / (5 seconds * 60 frames)

  if (currentAngle_1 >= 360) {
    currentAngle_1 = 0;
  }
   if (currentAngle_2 >= 360) {
    currentAngle_2 = 0;
  }
    if (currentAngle_3 >= 360) {
    currentAngle_3 = 0;
  }

  const arcPath = describeArc(100, 100, 70, currentAngle_1, currentAngle_1 + 45); // 30-degree arc segment
  const arcPath1 = describeArc(100, 100, 70, currentAngle_1+90, currentAngle_1 + 145); // 30-degree arc segment
  const arcPath2 = describeArc(100, 100, 70, currentAngle_1+180, currentAngle_1 + 235); // 30-degree arc segment
  const arcPath3 = describeArc(100, 100, 70, currentAngle_1+270, currentAngle_1 + 325); // 30-degree arc segment

  const arcPath4 = describeArc(100, 100, 61.5, currentAngle_2, currentAngle_2 + 35); // 30-degree arc segment
  const arcPath5 = describeArc(100, 100, 61.5, currentAngle_2+90, currentAngle_2 + 125); // 30-degree arc segment
  const arcPath6 = describeArc(100, 100, 61.5, currentAngle_2+180, currentAngle_2 + 215); // 30-degree arc segment
  const arcPath7 = describeArc(100, 100, 61.5, currentAngle_2+270, currentAngle_2 + 305); // 30-degree arc segment

  const arcPath8 = describeArc(100, 100, 58, currentAngle_3 + 20, currentAngle_3 + 65); // 30-degree arc segment
  const arcPath9 = describeArc(100, 100, 58, currentAngle_3+110, currentAngle_3 + 155); // 30-degree arc segment
  const arcPath10 = describeArc(100, 100, 58, currentAngle_3+200, currentAngle_3 + 245); // 30-degree arc segment
  const arcPath11 = describeArc(100, 100, 58, currentAngle_3+290, currentAngle_3 + 335); // 30-degree arc segment

  arc.setAttribute('d', arcPath);
  arc1.setAttribute('d', arcPath1);
  arc2.setAttribute('d', arcPath2);
  arc3.setAttribute('d', arcPath3);

  arc4.setAttribute('d',  arcPath4);
  arc5.setAttribute('d', arcPath5);
  arc6.setAttribute('d', arcPath6);
  arc7.setAttribute('d', arcPath7);

  arc8.setAttribute('d',  arcPath8);
  arc9.setAttribute('d', arcPath9);
  arc10.setAttribute('d', arcPath10);
  arc11.setAttribute('d', arcPath11);

  const progress = Math.round((currentAngle_1 / 360) * 100); // Calculate progress percentage
  progressPercentage.textContent = `${progress}%`; // Update the progress percentage text

  for (let i = 0; i < 100; i++) {
    if (progress >= (i + 1) * 1) {
      arcs.children[i].style.display = 'block';
    } else {
      arcs.children[i].style.display = 'none';
    }
  }

  swordProgress.setAttribute('width', `${progress * 2}`); // Update this line
  requestAnimationFrame(updateArc);
}

updateArc();

</script>