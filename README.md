# Robotics Learning Journal

A practical, project-led path from first principles to physical AI: build small things, measure what happens, and document what you learn.

**Status:** learning scaffold; projects have not yet been completed or hardware-tested.  
**Flagship project:** a LeRobot SO-101 arm that learns a simple pick-and-place task.

## Start here

1. Read [Getting started](guides/getting-started.md) and choose a software-first or hardware path.
2. Work through the [learning roadmap](ROADMAP.md), using observable milestones instead of deadlines.
3. Choose a [project](projects/README.md). Start with a small simulation before buying hardware.
4. Copy a [journal entry](templates/journal-entry.md) for each session and an [experiment](templates/experiment.md) for each comparison.
5. Keep evidence in the [journal index](journal/README.md): results, failures, photos, and the next question.

## Learning phases

| Phase | Focus | Evidence of progress |
| --- | --- | --- |
| 0 | Orientation and setup | Reproducible Python environment and first journal entry |
| 1 | Programming and robotics maths | Two-link arm calculation with units and a diagram |
| 2 | Sensing, actuation, and control | A controller that reaches a target in simulation |
| 3 | Robot software and simulation | ROS 2 publisher/subscriber and recorded observations |
| 4 | Physical hardware and teleoperation | Repeatable manual task on an SO-101 |
| 5 | Demonstrations and imitation learning | Inspected dataset and first ACT baseline |
| 6 | Evaluation and physical AI | Held-out trials, failure analysis, and one controlled improvement |

See [ROADMAP.md](ROADMAP.md) for prerequisites, exercises, and completion checks. ROS 2 is a useful parallel track; it is not a prerequisite for the LeRobot arm project.

## Repository map

- [Beginner setup](guides/getting-started.md), [physical AI](guides/physical-ai.md), and [hardware planning](guides/hardware-and-safety.md)
- [SO-101 project](projects/so101/README.md) and [other starter projects](projects/README.md)
- [Glossary](resources/glossary.md) and [official learning resources](resources/README.md)
- [Learning journal](journal/README.md), [session template](templates/journal-entry.md), and [experiment template](templates/experiment.md)

## Working principles

Define success before a run. Keep failed trials. Change one variable at a time. Pin the software version used for each experiment. Keep datasets and model weights outside Git; commit their identifiers and provenance instead.

Upstream robotics APIs change quickly. Official installation and hardware instructions linked in each guide take precedence over old copied commands. Resources were reviewed on **15 October 2026**; this journal does not claim the hardware or training workflows were executed.
