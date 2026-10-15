# Learning roadmap

Move on when you can demonstrate the milestone. Return to the maths as projects make it useful; you do not need to finish a textbook before touching a simulator.

## Phase 0 — Orientation and a reproducible workspace

**Learn:** the sense → decide → act → observe loop; terminal basics, Git, Python environments.

**Do:** follow [Getting started](guides/getting-started.md); write a script that reads a target value and prints an error. Record your OS, Python version, and command.

**Done when:** you can recreate the environment and explain the difference between a robot, its controller, and its policy.

## Phase 1 — Programming, geometry, and units

**Prerequisite:** phase 0. Learn functions, arrays, plotting, radians, vectors, coordinate frames, and matrix multiplication.

**Do:** calculate the endpoint of a planar arm: `x = L1*cos(q1) + L2*cos(q1+q2)` and `y = L1*sin(q1) + L2*sin(q1+q2)`. Use metres and radians. Check a straight arm and a folded arm by hand. Plot several poses.

**Done when:** you can predict how a joint change affects the gripper and distinguish joint space from task space. Study relevant [Modern Robotics](https://modernrobotics.northwestern.edu/) chapters as needed.

## Phase 2 — Sensing and feedback control

**Prerequisite:** phase 1. Learn position versus velocity, sampling rate, noise, saturation, and feedback.

**Do:** implement a simulated proportional controller; compare three gains using the same target and initial state. Add an actuator limit and log target, measured position, and error over time.

**Done when:** you can explain overshoot, settling, and why a controller must respect limits. See the [controller project](projects/README.md#1--simulated-feedback-controller).

## Phase 3 — Robot software and simulation

**Prerequisite:** phase 0; phase 2 helps. Learn ROS 2 nodes, topics, messages, services, parameters, and coordinate transforms.

**Do:** follow the official ROS 2 beginner tutorials for one supported distribution. Run turtlesim, inspect a topic, and write a small publisher/subscriber. Record the chosen OS/distribution pair. Separately, explore a simple MuJoCo model if manipulation interests you.

**Done when:** you can trace where a command originates and where a sensor observation goes. Simulation success is evidence about the simulation; test physical assumptions separately.

## Phase 4 — Hardware and teleoperation

**Prerequisite:** [hardware checklist](guides/hardware-and-safety.md); phase 3 is optional.

**Do:** follow the [SO-101 project](projects/so101/README.md) through assembly, calibration, and manual operation. Complete a simple task repeatedly before collecting training data.

**Done when:** the arm moves predictably, the camera sees the task, and you can stop motion promptly.

## Phase 5 — Data and imitation learning

**Prerequisite:** reliable phase 4 setup. Learn episodes, observations, actions, camera synchronization, dataset quality, and training versus evaluation.

**Do:** record a small pilot, replay every episode, fix collection problems, then expand. Train an ACT baseline following the version-matched official tutorial. Save dataset revision, split, seed, configuration, and checkpoint.

**Done when:** you can trace a model back to its demonstrations and run a supervised evaluation. Training loss alone is not task success.

## Phase 6 — Evaluation and broader physical AI

**Prerequisite:** phase 5. Learn distribution shift, generalization, vision-language-action models, and the distinction between imitation and reinforcement learning.

**Do:** define held-out starting positions before training. Compare one change (data coverage, camera placement, or policy) against the baseline under the same trial conditions. Log failures and interventions. Explore [physical AI](guides/physical-ai.md) after establishing a baseline.

**Done when:** you can state what worked, the tested conditions, the uncertainty, and the next experiment without relying on a highlight video.

## Progress tracker

- [ ] Phase 0: workspace and first entry
- [ ] Phase 1: arm geometry notebook or script
- [ ] Phase 2: controller comparison
- [ ] Phase 3: ROS 2 message flow
- [ ] Phase 4: repeatable SO-101 teleoperation
- [ ] Phase 5: inspected dataset and baseline
- [ ] Phase 6: evaluation report and improvement
