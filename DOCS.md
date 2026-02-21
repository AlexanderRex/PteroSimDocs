# PteroSim Documentation

High-fidelity UAV flight simulator — documentation plan and reference.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Description](#description)
- [Installation](#installation)
- [Python SDK Commands (15 RPCs)](#python-sdk-commands-15-rpcs)
- [Additional Sections](#additional-sections) *(planned)*

---

## Prerequisites

### Required

- [**Python 3.10+**](https://www.python.org/downloads/) (for PteroSim Python SDK)
- [**Visual Studio 2022**](https://aka.ms/vs/17/release/vs_community.exe)
- [**Unreal Engine 5.6**](https://www.unrealengine.com/en-US/unreal-engine-5)
- [**JSBSim**](https://github.com/JSBSim-Team/jsbsim) (provides aircraft physics simulation)
- [**CesiumGS**](https://github.com/CesiumGS/cesium-unreal) (handles geotile loading)

### Optional

- [**WSL Ubuntu**](https://documentation.ubuntu.com/wsl/stable/howto/install-ubuntu-wsl2/) (JSBSim.so for Linux cross-compilation)
- [**PX4 Autopilot**](https://github.com/PX4/PX4-Autopilot) (enables UAV autonomous missions and manual control)
- [**QGC**](https://qgroundcontrol.com/) (GUI for configuring and launching PX4 missions)

### Plugins

- [**PteroSimCore**](https://github.com/AlexanderRex/PteroSimCore) (base simulation classes)
- [**PteroSimSensors**](https://github.com/AlexanderRex/PteroSimSensors) (UAV sensors)
- [**PteroSimScripting**](https://github.com/AlexanderRex/PteroSimScripting) (gRPC API for programmatic simulation control)
- [**MavlinkUE**](https://github.com/AlexanderRex/MavlinkUE) (manages UAV data transmission)

---

## Description

PteroSim is a high-fidelity UAV flight simulator built on Unreal Engine 5, integrating JSBSim for physics, Cesium for geospatial tiles, and optional PX4/MavLink for autonomous missions.

---

## Installation

1. Clone repository with submodules:
   ```bash
   git clone --recursive git@github.com:AlexanderRex/PteroSim.git
   ```
   If already cloned without `--recursive`:
   ```bash
   git submodule update --init --recursive
   ```

2. Build JSBSim (run from `devops_data`, e.g. in PowerShell):
   ```bash
   cd devops_data
   ./build-jsbsim.bat
   cd ..
   ```

3. Right-click `PteroSim.uproject` → **Generate Visual Studio project files**

4. Open `PteroSim.sln` in Visual Studio 2022

5. Set build configuration to **Development Editor**

6. Build the solution (Ctrl+Shift+B)

7. Launch the editor from Visual Studio or double-click `PteroSim.uproject`

8. Install PteroSim Python SDK (optional, for gRPC scripting):
   ```bash
   cd Plugins/PteroSimScripting/SDK/python
   pip install -e .
   cd -
   ```

---

## Python SDK Commands (15 RPCs)

These commands are executed in a Python console or script using the PteroSim SDK (`scripts/sim_control/test_sdk.py`, `Plugins/PteroSimScripting/SDK/python/`).

| # | RPC | Python usage | Description |
|---|-----|--------------|-------------|
| 1 | GetStatus | `sim.status()` | Returns simulation run state, time scale, physics frequency, and aircraft count. |
| 2 | SetTimeScale | `sim.set_time_scale(2.0)` | Sets simulation time multiplier (e.g. 2.0 = 2× real time). |
| 3 | SetPhysicsFrequency | `sim.set_physics_frequency(500.0)` | Sets physics update rate in Hz. |
| 4 | SetMavlinkBindAddress | `sim.set_mavlink_bind_address("127.0.0.1")` | Sets MAVLink bind address for telemetry. |
| 5 | GetMavlinkBindAddress | `sim.get_mavlink_bind_address()` | Returns current MAVLink bind address. |
| 6 | GetSimulationClock | `sim.clock()` | Returns clock state, sim time, step number, frequency, and time scale. |
| 7 | ListAircraftClasses | `sim.list_aircraft_classes()` | Returns available aircraft types (e.g. F450, DeltaQuad). |
| 8 | SpawnAircraft | `drone = sim.spawn("F450", x=0, y=0, z=200)` | Spawns an aircraft of given class at x, y, z. |
| 9 | GetAircraftStatus | `sim.aircraft_status()` | Returns status of all spawned aircraft. |
| 10 | Start | `sim.start()` | Starts simulation (physics running). |
| 11 | Hold | `sim.hold()` | Pauses simulation. |
| 12 | StepOnce | `sim.step_once()` | Advances simulation by one physics step. |
| 13 | Resume | `sim.resume()` | Resumes simulation after hold. |
| 14 | RemoveAircraft | `drone.remove()` | Removes the aircraft and returns remaining count. |
| 15 | Stop | `sim.stop()` | Stops simulation. |

**Example (run all 15 RPCs):**

```bash
python scripts/sim_control/test_sdk.py
```

---

## Additional Sections

*(To be expanded as needed.)*

- API reference
- Usage examples
- Troubleshooting
- Contributing guidelines
