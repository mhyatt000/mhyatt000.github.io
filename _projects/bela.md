---
layout: page
title: BELA
description: its my current work... cant tell you more than that right now ;)
img: https://github.com/mhyatt000/mhyatt000.github.io/releases/download/bela-v0.0.0/bela-cover.png
importance: 1
category: work
related_publications: true
---

# BEhavior is a foreign LAnguage for robots

### Autonomous Policy Execution

<div class="row" >
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include video.liquid loading="eager" path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/bela-v0.0.0/img_0528.mp4" title="example image" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include video.liquid loading="eager" path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/bela-v0.0.0/img_0542.mp4" title="example image" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
</div>

<div class="caption">
    Left: something was wrong with this model. I forget. Even so, the grasping of the broom is very hard since it is balanced on a point. So the gripper must be very precise to succeed. <br>
    Right: The model I trained can generalize to the task. With greater than 90% success rate. 
</div>

Please shoot an email if you have any beans that you need swept up or if you would like this system deployed in your home.

### Hand Teleoperation and 2D Tracking

<div class="row" >
    <div class="col-sm-5 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/bela-v0.0.0/hand-teleop.gif" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include video.liquid loading="eager" path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/bela-v0.0.0/hand-track-2d.mp4" title="example image" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
</div>
<div class="caption">
    Left: Hand teleoperation using RUKA hand. This was my first attempt so I had to do some tricks to get the tracking to translate well to the robot coordinate space. <br>
    Right: 3D tracking of hand keypoints using HAMER (displayed in 2D). This is used as input to the teleoperation system.
</div>


### RUKA

<div class="row mt-3">
    <div class="col-sm-3 mt-3 mt-md-0">
        {% include video.liquid path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/hand-v0.0.0/ruka.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/hand-v0.0.0/ruka-part0.png" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/hand-v0.0.0/ruka-part1.png" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/hand-v0.0.0/ruka-part2.png" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
</div>
<div class="caption">
    RUKA hand calibration. TODO cite (you can google it for now)
</div>

### APRIL

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="april/apriltags_30mm.png" title="april grid" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This is 30mm april grid.
</div>

{% cite sc25-shortcutmixup %}.

