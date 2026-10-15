---
layout: default
title: "Starter projects"
---

# Starter projects

These are proposed exercises, not completed builds. Each should produce a short journal entry and evidence you can reproduce.

| Project | Needs | Learn | Completion evidence |
| --- | --- | --- | --- |
| Simulated feedback controller | Python | Feedback and limits | Error plot and gain comparison |
| ROS 2 turtlesim | Supported ROS 2 environment | Nodes and message flow | Small publisher/subscriber and run instructions |
| Camera observation notebook | Webcam or saved images | Frames, lighting, perception | Annotated frames and failure examples |
| [SO-101 pick-and-place](so101/index.html) | Arm workbench | Teleoperation → data → policy | Dataset audit and trial report |
| Simulated manipulation | MuJoCo environment | Contacts and sim assumptions | Repeatable scene and logged outcome |

## 1 — Simulated feedback controller

Model a position as `position_next = position + velocity * dt`. Set `velocity = clamp(Kp * (target - position), -limit, limit)`. Begin with a fixed timestep, state, and target. Plot error for three gains and describe the role of the actuator limit. This simplified velocity-controlled model is an exercise, not a physical motor model.

**Stretch:** add sensor noise or delay, changing one at a time. Record the parameters and seed. Pass when your results can be recreated and you can explain the limitations.

## 2 — ROS 2 turtlesim

Follow the [official tutorials](https://docs.ros.org/en/jazzy/Tutorials.html) for your selected distribution; the link is the Jazzy track, not a claim that it is the newest release. Run turtlesim, inspect velocity commands, and create a node that traces a small shape. Log topic names, message types, and the stop procedure.

**Stretch:** subscribe to pose and close the loop on a target. Pass when another session can reproduce the path from your notes.

## 3 — Camera observation notebook

Capture a few frames of an object against a plain background. Locate it with a simple colour threshold or manual annotation, then vary lighting and background. Describe occlusion and the difference between pixel coordinates and a robot coordinate frame. Do not command a real arm from uncalibrated pixel coordinates.

**Pass:** save representative success and failure frames with settings and explain what changed.

## 4 — Simulated manipulation

Use a small example from the [MuJoCo documentation](https://mujoco.readthedocs.io/en/stable/overview.html). Inspect its joints, actuators, timestep, and contact settings. Reproduce a simple movement and change one parameter.

**Pass:** explain which assumptions would need validation on physical hardware; keep the model/configuration reference with the result.
