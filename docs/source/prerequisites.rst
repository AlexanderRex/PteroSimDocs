Prerequisites
=============

Required
--------

- `Python 3.10+ <https://www.python.org/downloads/>`_ (for PteroSim Python SDK)
- `Visual Studio 2022 <https://aka.ms/vs/17/release/vs_community.exe>`_
- `Unreal Engine 5.6 <https://www.unrealengine.com/en-US/unreal-engine-5>`_
- `JSBSim <https://github.com/JSBSim-Team/jsbsim>`_ (provides aircraft physics simulation)
- `CesiumGS <https://github.com/CesiumGS/cesium-unreal>`_ (handles geotile loading)

Optional
--------

- `WSL Ubuntu <https://documentation.ubuntu.com/wsl/stable/howto/install-ubuntu-wsl2/>`_ (JSBSim.so for Linux cross-compilation)
- `PX4 Autopilot <https://github.com/PX4/PX4-Autopilot>`_ (enables UAV autonomous missions and manual control)
- `QGC <https://qgroundcontrol.com/>`_ (GUI for configuring and launching PX4 missions)

Plugins
-------

- `PteroSimCore <https://github.com/AlexanderRex/PteroSimCore>`_ (base simulation classes)
- `PteroSimSensors <https://github.com/AlexanderRex/PteroSimSensors>`_ (UAV sensors)
- `PteroSimScripting <https://github.com/AlexanderRex/PteroSimScripting>`_ (gRPC API for programmatic simulation control)
- `MavlinkUE <https://github.com/AlexanderRex/MavlinkUE>`_ (manages UAV data transmission)
