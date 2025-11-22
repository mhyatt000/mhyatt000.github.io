---
layout: page
title: locomotion
description: its my current work... cant tell you more than that right now ;)
img: https://github.com/mhyatt000/mhyatt000.github.io/releases/download/tag-v0.0.0/go2-cover.png
importance: 2
category: work
related_publications: false
---

# GO Locomotion

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid loading="eager" path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/tag-v0.0.0/tag-random.mp4" title="tag-random" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid loading="eager" path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/tag-v0.0.0/terrain.mp4" title="terrain" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
</div>
<div class="caption">
    Left: Randomized movements on flat terrain. Right: Generated terrain patches.
</div>


<div class="row" >
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid loading="eager" path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/tag-v0.0.0/output.mp4" title="output" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid loading="eager" path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/tag-v0.0.0/joygo2.mp4" title="joygo2" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid loading="eager" path="https://github.com/mhyatt000/mhyatt000.github.io/releases/download/tag-v0.0.0/go2-collide.mp4" title="go2-collide" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}
    </div>
</div>

<div class="caption" style="text-align: left;">
    [A] PPO walking policy. it can walk in all directions. <br>
    [B] User controlling the robot with a joystick. <br>
    [C] Collision detection of joystick wraped PPO with a simple heuristic.
</div>

