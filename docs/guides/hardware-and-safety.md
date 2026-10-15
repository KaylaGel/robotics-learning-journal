---
layout: default
title: "Hardware planning and first motion"
---

# Hardware planning and first motion

## Plan the whole workbench

Use the current [SO-101 hardware guide](https://huggingface.co/docs/lerobot/so101) and its linked bill of materials. Confirm the exact revision and kit contents before ordering; do not assume SO-100 and SO-101 parts or instructions are interchangeable.

| Item | What to confirm | Your choice / cost (AUD) |
| --- | --- | --- |
| Arm kit | Leader/follower contents, motor variants, assembly level | TBD |
| Printed parts | Included, printed locally, or outsourced | TBD |
| Power and control | Correct supply, adapters, cables, local plug | TBD |
| Mounting | Secure bases, stable desk, camera mounts | TBD |
| Cameras | Supported connection, clear task view | TBD |
| Tools and spares | Required tools, fasteners, spare cables | TBD |
| Compute | Control machine and separate training plan | TBD |
| Other | Shipping, tax, replacement parts, compute allowance | TBD |

Prices vary; this is a budget worksheet, not a vendor recommendation. You can complete the software phases before purchasing anything.

## Before applying power

- [ ] Read the kit's assembly and electrical instructions.
- [ ] Confirm supply voltage/polarity against the actual components.
- [ ] Secure the arm and inspect cables, fasteners, and clearance.
- [ ] Keep hands, hair, clothing, pets, and fragile objects outside the workspace.
- [ ] Identify how to stop software and disconnect motor power promptly.
- [ ] Support the arm as appropriate: removing power can let it drop.

## Before each motion session

- [ ] Verify calibration and joint direction before approaching limits.
- [ ] Use a clear workspace, conservative motion settings, and lightweight objects.
- [ ] Keep the power cutoff accessible; a software stop may fail.
- [ ] Inspect camera framing and ensure no bystander enters the work area.
- [ ] Supervise all experimental policy runs. Stop for unexpected movement, binding, heat, or cable strain.

Do not improvise electrical wiring or bypass a limit to resolve a software error. Follow the hardware vendor's procedure for wiring changes and power state.
