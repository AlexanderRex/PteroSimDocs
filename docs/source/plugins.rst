Plugins
=======

PteroSim uses a modular plugin architecture. Each plugin provides specific functionality and can be developed independently.

---

PteroSimCore
------------

`GitHub <https://github.com/AlexanderRex/PteroSimCore>`_

Base simulation classes and core functionality. Provides the foundation for aircraft spawning, physics integration, and simulation lifecycle management.

---

PteroSimSensors
---------------

`GitHub <https://github.com/AlexanderRex/PteroSimSensors>`_

UAV sensor implementations including cameras, LIDAR, GPS, IMU, and other onboard sensors. Handles data acquisition and streaming.

---

PteroSimScripting
-----------------

`GitHub <https://github.com/AlexanderRex/PteroSimScripting>`_

gRPC API for programmatic simulation control. Enables Python SDK integration and external tool connectivity. See :doc:`python_sdk` for available commands.

---

MavlinkUE
---------

`GitHub <https://github.com/AlexanderRex/MavlinkUE>`_

MAVLink protocol integration for UAV data transmission. Enables communication with PX4 Autopilot and ground control stations like QGroundControl.
