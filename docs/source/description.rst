Introduction
============

What is PteroSim?
-----------------

PteroSim is a high-fidelity UAV flight simulator built on Unreal Engine 5. It integrates JSBSim for accurate aircraft physics, Cesium for geospatial tile loading, and optionally PX4/MAVLink for autonomous missions and manual control.

The simulator provides a gRPC-based Python SDK for programmatic control, enabling scripted scenarios, automated testing, and integration with external tools.

Key features
------------

* **High-fidelity physics** — JSBSim integration for realistic flight dynamics.
* **Geospatial rendering** — Cesium plugin for real-world terrain and satellite imagery.
* **Autonomous flight** — Optional PX4 Autopilot integration for mission planning.
* **Python SDK** — gRPC API with 15 RPC commands for simulation control.
* **Modular architecture** — Separate plugins for core, sensors, scripting, and MAVLink.
