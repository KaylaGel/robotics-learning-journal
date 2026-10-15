---
layout: default
title: "Physical AI, explained through a first project"
---

# Physical AI, explained through a first project

Physical AI is a broad term for AI systems that use observations to act in the physical world. Robotics adds bodies, sensors, mechanics, feedback, and constraints to the learning problem.

For a tabletop task, the loop is: observe the scene and joint state, choose an action, execute a bounded movement, and observe again. Timing, camera placement, contact, and the reset procedure all affect the result.

## Distinguish the approaches

| Approach | Where the behaviour comes from | First exercise |
| --- | --- | --- |
| Classical control | An explicit model or feedback rule | Simulated target tracking |
| Teleoperation | A human commands the robot | Move a block manually |
| Imitation learning | Demonstrations of the desired behaviour | Train a small task-specific baseline |
| Reinforcement learning | Interaction guided by a reward | Explore in simulation after learning evaluation basics |
| Vision-language-action (VLA) | A learned model combines visual/language inputs to produce actions | Compare a suitable pretrained model after a baseline works |

Teleoperation supplies demonstrations; it does not by itself make the robot autonomous. A language instruction also does not guarantee safe or correct execution.

## A manageable first learning task

Choose one large, lightweight object and a wide target tray. Mark a small set of start positions. Define success as placing the object fully in the tray within a fixed time without human help. Keep the initial scene consistent, then deliberately test new positions separately.

Use [ACT](https://huggingface.co/docs/lerobot/act) as an initial imitation-learning policy to investigate. It predicts chunks of actions from observations. Later, [SmolVLA](https://huggingface.co/docs/lerobot/smolvla) provides a route to exploring vision-language-action models. Verify model-specific observation, action, hardware, and compute requirements before comparing them.

## What to measure

Record successes / attempts, time limit, resets, interventions, and failure types. Ten trials can reveal obvious failures but give an uncertain success-rate estimate; retain the individual outcomes and expand the evaluation before making strong claims. Keep held-out evaluation episodes out of training and model selection when reporting final performance.

A useful improvement is a repeatable gain under specified conditions. Report a failed reach or dropped object as evidence, then ask whether it came from perception, demonstration coverage, mechanics, latency, or control.
