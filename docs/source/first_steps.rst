First Steps
===========

Open the Spawn panel
--------------------

After launching PteroSim, find the **Spawn** button in the lower-left corner of the screen.  
Clicking it opens the aircraft and payload spawn panel:

.. image:: Images/spawn_panel.png
   :alt: Aircraft and payload spawn panel
   :align: center

Simulation controls
-------------------

* Use Start/Pause and Stop buttons to control the simulation state.
* Use Time Scale, Physics Hz, Weather, Wind kts and Dir windows to control phyiscal atributes of the simulation.


Aircraft grid
-------------

Each aircraft card has controls of the form ``1 x 1`` and a **Dist** field:

* **1 × 1** — how many aircraft to spawn along each side of the grid.
* **Dist** — side length of the grid in meters.

Aircraft types
--------------

* **F450Aircraft** — four rotor drone.

Payloads
--------

* **BasePayload** spawns a cargo box with configurable **Mass (kg)**.  
  Aircraft equipped with a gripper can lift this box and use it as a payload in scenarios.

Taking flight
-------------

Actuator commands are merged in ``UActuatorInputComponent``. **PX4** (MAVLink HIL over TCP) and **ArduPilot** (JSON SITL over UDP) are supported end-to-end in the simulator and companion repos. **Direct in-game stick/throttle control** (keyboard/gamepad without a flight stack or SDK) is **PLACEHOLDER** — not implemented in the current tree; use PX4, ArduPilot, or the Python SDK below.

Direct manual flight (not available yet)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**PLACEHOLDER** — default possessed-aircraft flight axes (RC-style) are not wired in the open C++ plugins; only camera / cycle / gripper shortcuts exist on the player controller. Until this ships, use **PX4**, **ArduPilot**, or the **Python SDK** (:doc:`python_api`: ``set_actuator_controls``, ``set_attitude_command``).

You can still **possess** an aircraft with **P** (**Esc** spectator, **Tab** FPV/third person, **G** gripper when present) for view and payload toggles.

PX4 + QGroundControl (MAVLink HIL, TCP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PteroSim listens for **MAVLink HIL over TCP** on **``4560 + InstanceID``** per spawned aircraft (``UPX4ServerComponent`` uses ``BasePort = 4560``). PX4’s **``MAV_SYS_ID``** must equal **``InstanceID + 1``** so HIL traffic matches the vehicle.

1. **Start PteroSim**, press **Start** on the simulation panel, and spawn the aircraft (e.g. F450). You may start PX4 before or after; lockstep engages once PX4 connects.

2. **Run PX4 SITL** on Linux/WSL with lockstep and put your **Ubuntu IP address** in `[IP-address]``:

   .. code-block:: bash

      PX4_SIM_HOSTNAME=[IP-address] PX4_LOCKSTEP=1 PX4_SIM_SPEED_FACTOR=1 make px4_sitl none_iris

   The PteroSim repo also ships helpers that set the same environment and launch ``px4`` with per-instance rootfs: ``scripts/px4_launch/run_instance.sh [instance] [model]`` and ``scripts/px4_launch/run_multiple_instances.sh`` (defaults: ``none_iris``, TCP **4560+N**, system id **N+1** — see script echo output).

3. **Connect QGroundControl**. Open **Application Settings**, add or edit a **Comm Link** to your PX4 instance (UDP to the machine where SITL runs, typically port **14550**), then connect:

   .. image:: Images/qgc_main_menu.png
      :alt: QGroundControl main menu and Application Settings
      :align: center

   .. image:: Images/qgc_comm_link.png
      :alt: QGroundControl communication link configuration
      :align: center

   .. image:: Images/qgc_connect_link.png
      :alt: QGroundControl select link to connect
      :align: center

   After the link is online, use **Plan** / **Fly** as with normal SITL.

ArduPilot (JSON + binary servo, UDP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Start** PteroSim and spawn the matching airframe.

2. On Ubuntu/WSL, launch ArduPilot SITL and put your **Ubuntu IP address** in ``JSON:[IP-address]``:

   .. code-block:: bash

      python3 Tools/autotest/sim_vehicle.py -v ArduCopter -f quad --model JSON:[IP-address] --no-rebuild -w -P FRAME_TYPE=1

   This command is an **F450 quad example**. Other vehicle types use different ``sim_vehicle.py`` options (vehicle type, frame, and parameters).

3. Launch **Mission Planner** and open the **Plan** tab:

   .. image:: Images/ardupilot_plan_top_tabs.png
      :alt: Mission Planner top tabs with Plan selected
      :align: center

4. Build a mission either from the bottom waypoint table or by right-clicking on the map:

   .. image:: Images/ardupilot_plan_waypoint_table.png
      :alt: Mission Planner waypoint table editor
      :align: center

   .. image:: Images/ardupilot_plan_map_context_menu.png
      :alt: Mission Planner map right-click mission menu
      :align: center

5. Click **Write** on the right panel to upload the mission:

   .. image:: Images/ardupilot_plan_write_panel.png
      :alt: Mission Planner write panel
      :align: center

6. Go to the **Data** tab. Open **Actions** and click **Arm/Disarm**. Select **mission_start** and click **Do Action**.
