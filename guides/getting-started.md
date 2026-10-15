# Getting started

## Choose your first path

**No hardware:** start with Python, a simulated controller, and ROS 2 turtlesim. Work through phases 0–3 before deciding what to buy.

**Ready for an arm:** begin the same foundations, then read the SO-101 project and hardware planning guide. You can learn ROS 2 separately.

## First session: make something reproducible

Install Git, an editor, and a supported Python version from their official sources. For a standalone fundamentals workspace:

```bash
python3 --version
git --version
python3 -m venv .venv
source .venv/bin/activate
python -c "print('My first robotics learning session')"
```

These activation commands are for macOS/Linux. On Windows PowerShell, use `.venv\Scripts\Activate.ps1`. The environment above is for exercises; use the current [LeRobot installation guide](https://huggingface.co/docs/lerobot/installation) when setting up LeRobot, including its own Python and system dependency requirements.

Copy `templates/journal-entry.md` to `journal/YYYY-MM-DD-topic.md`. Write your starting skill level, available equipment, one goal, and what actually happened. Add the entry to `journal/README.md`.

## First five sessions

1. Run the commands above and create an entry.
2. Write a function that computes `target - measured_position` and test it with three inputs.
3. Calculate and plot the endpoint of a two-link arm using the roadmap formulas.
4. Simulate a feedback controller and compare gains.
5. Read the SO-101 guide or begin ROS 2 turtlesim; write down one question the exercise should answer.

## Match tools to your machine

Python fundamentals can begin on your existing laptop. ROS 2 installation depends on the selected distribution and supported platform; use its official installation matrix before choosing native installation, a VM, or another machine. USB access, cameras, graphics, and containers can require extra setup.

Separate robot control from training requirements. Before renting compute or purchasing a GPU, inspect the selected policy's requirements and run a small test. Record GPU type, memory, cost limit, and elapsed time when using paid compute. Never assume the training backend supported on one machine works on another.

## If you get stuck

Save the exact command, full error, versions, and the smallest reproduction. Determine whether the failure is environment, connection, sensing, control, or learning. Change one thing and record the outcome. Do not commit credentials or private camera footage.
