Prerequisites
=============

Before building PteroSim, ensure you have the required software installed. Optional dependencies enable additional features like Linux cross-compilation and autonomous missions.

---

Required software
-----------------

`Python 3.10+ <https://www.python.org/downloads/>`_ — Required for the PteroSim Python SDK.

`Visual Studio 2022 <https://aka.ms/vs/17/release/vs_community.exe>`_ — C++ compiler for building the project.

`Unreal Engine 5.6 <https://www.unrealengine.com/en-US/unreal-engine-5>`_ — Game engine powering the simulator.

`JSBSim <https://github.com/JSBSim-Team/jsbsim>`_ — Flight dynamics model providing aircraft physics simulation.

`CesiumGS <https://github.com/CesiumGS/cesium-unreal>`_ — Plugin for loading geospatial tiles and terrain.

---

Optional software
-----------------

`WSL Ubuntu <https://documentation.ubuntu.com/wsl/stable/howto/install-ubuntu-wsl2/>`_ — Enables JSBSim.so compilation for Linux cross-builds.

`PX4 Autopilot <https://github.com/PX4/PX4-Autopilot>`_ — Enables autonomous UAV missions and manual control.

`QGroundControl <https://qgroundcontrol.com/>`_ — GUI for configuring and launching PX4 missions.

---

Plugins
-------

`PteroSimCore <https://github.com/AlexanderRex/PteroSimCore>`_ — Base simulation classes and core functionality.

`PteroSimSensors <https://github.com/AlexanderRex/PteroSimSensors>`_ — UAV sensor implementations.

`PteroSimScripting <https://github.com/AlexanderRex/PteroSimScripting>`_ — gRPC API for programmatic simulation control.

`MavlinkUE <https://github.com/AlexanderRex/MavlinkUE>`_ — MAVLink protocol integration for UAV data transmission.
