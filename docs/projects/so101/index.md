---
layout: default
title: "LeRobot SO-101: first learned pick-and-place"
---

# LeRobot SO-101: first learned pick-and-place

**Status:** planned; no assembly, data collection, or training results yet.  
**Goal:** move a lightweight block into a tray, first by teleoperation and later with a learned policy.

SO-101 is the arm hardware; LeRobot is the software ecosystem used here. Use the [official SO-101 guide](https://huggingface.co/docs/lerobot/so101) and [hardware repository](https://github.com/TheRobotStudio/SO-ARM100) for revision-specific details.

## 1. Scope the task

Write down the object, workspace, initial positions, camera view, time limit, and success rule. Start with one object and one tray. Photograph the scene and reserve a set of starting positions for evaluation.

**Gate:** a clear task definition and completed [hardware checklist](../../guides/hardware-and-safety.html).

## 2. Prepare and assemble

Check kit contents against the linked bill of materials. Install the version of LeRobot you intend to use with its required motor dependencies. Follow upstream instructions for motor setup, assembly, and calibration; record the hardware revision and software commit. Keep leader and follower ports clearly labelled.

**Gate:** calibration is saved and checked; limited test movements are predictable and unobstructed. Do not collect training data to compensate for incorrect calibration.

## 3. Teleoperate before learning

Use the version-matched [imitation-learning tutorial](https://huggingface.co/docs/lerobot/il_robots) for teleoperation. Practise the entire task and resetting the scene. Check the gripper and object stay visible. Save a short session log with failures.

**Gate:** repeatable manual completion with a consistent reset. If manual operation fails, investigate the hardware, task, or camera before training.

## 4. Collect and inspect a pilot

Record a few demonstration episodes using the official workflow. Replay all of them before scaling collection. Check task completion, image visibility, state/action alignment, and abrupt or missing frames. Keep episode identifiers and rejection reasons.

**Gate:** an inspected pilot dataset; then collect broader coverage within the defined training conditions. There is no guaranteed demonstration count.

Keep raw recordings outside Git. A private GitHub repository does not make a Hugging Face dataset or model private: verify each Hub repository's visibility separately before any upload. Review camera footage for private information.

## 5. Train a baseline

Follow the [ACT guide](https://huggingface.co/docs/lerobot/act) using your installed version. Capture the complete command/configuration, dataset revision, training split, random seed, compute details, and checkpoint location in an [experiment record](../../templates/experiment.html). Check upstream defaults for publishing, tracking, and output destinations before running.

**Gate:** a loadable checkpoint and complete provenance. Inspect training curves, but evaluate the physical task separately.

## 6. Evaluate under supervision

Use the deployment procedure for the pinned LeRobot version; command names and flags can change. Recheck calibration, camera keys, action conventions, and the reachable stop before loading a policy. Perform an initial conservative supervised check, then run the predefined evaluation positions.

| Trial | Start condition | Success? | Time (s) | Intervention? | Failure / notes |
| --- | --- | --- | --- | --- | --- |
| 1 | TBD | Not run | — | — | — |

Count interventions separately and treat assisted completion as failure for an autonomous success metric. Keep the denominator and all failures.

**Gate:** a report of successes/attempts and tested conditions, not just a demonstration video.

## 7. Improve one thing

Choose a failure pattern. Add demonstration coverage, adjust camera placement (and recollect compatible data), or compare a suitable policy. Preserve the previous baseline and evaluation protocol. Try [SmolVLA](https://huggingface.co/docs/lerobot/smolvla) after you can explain the baseline's limits.

## Troubleshooting log prompts

| Symptom | First checks |
| --- | --- |
| Arm not detected | Correct port, power, data-capable USB cable, permissions |
| Unexpected movement | Stop; inspect calibration, hardware type, joint mapping, limits |
| Object disappears | Camera placement, occlusion, mounting stability |
| Low loss but poor task success | Data leakage, coverage, camera/config mismatch, timing |
| Model misses deadline | Measure full observation-to-action latency; inspect compute and camera pipeline |

Record exact errors and changes. This guide is a learning plan; the linked official instructions supply the current executable setup sequence.
