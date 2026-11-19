SITL simulation with ArduPilot
==============================

The ``sim_vehicle.py`` commands below run in Ubuntu under WSL. They call
``sim_vehicle.py`` by name, which works once ArduPilot's
``Tools/autotest`` folder is on the PATH; ArduPilot's Ubuntu setup script,
``Tools/environment_install/install-prereqs-ubuntu.sh``, offers to add it.

SITL reaches PteroSim at the Windows address as WSL sees it. Set it in every
WSL terminal you start SITL from:

.. code-block:: bash

   # WSL with networkingMode=mirrored in .wslconfig
   WIN_HOST=127.0.0.1

   # WSL with the default NAT networking
   WIN_HOST=$(ip route | awk '/default/ {print $3; exit}')

With mirrored networking, also add ``--no-wsl2-network`` to each
``sim_vehicle.py`` command. Without it, MAVProxy sends its UDP output for
ground stations to your router instead of to Windows.

Single-instance launch
----------------------

1. **Start PteroSim** and spawn the F450 drone while the simulation is
   stopped.

2. In the control source panel choose **ArduPilot**:

   .. image:: Images/control_source_ardupilot.png
      :alt: Control Source panel with ArduPilot selected
      :class: no-float-left

3. Set Physics Hz to **1000** with the top slider, then press **Start** on
   the simulation panel.

4. Start ArduPilot SITL from the F450's folder. ``<release>`` is the release
   directory's path in WSL, such as ``/mnt/c/...`` for a folder on drive C:

   .. code-block:: bash

      cd <release>/PteroSim/PteroSimAircrafts/F450
      sim_vehicle.py -v ArduCopter -f quad --model "JSON:$WIN_HOST" \
        --add-param-file="$(pwd)/firmwares/ardupilot_F450.param" --no-rebuild -w

   For another vehicle, use its folder, its ``firmwares/ardupilot_<Name>.param``
   and the matching ``-v`` and ``-f``. ``--no-rebuild`` uses the SITL binary
   you have already built; leave it out the first time.

5. Launch **Mission Planner** and open the **Plan** tab in the top left of
   the screen:

   .. image:: Images/ardupilot_plan_top_tabs.png
      :alt: Mission Planner top tabs with Plan selected
      :align: left

6. Build a mission either from the bottom waypoint table or by right-clicking
   on the map. Click **Write** on the panel on the right to upload it:

   .. image:: Images/ardupilot_plan_map_context_menu.png
      :alt: Mission Planner map right-click mission menu
      :align: left

7. Go to the **Data** tab. Open **Actions** and click **Arm/Disarm**. Select
   **mission_start** and click **Do Action**.

   .. image:: Images/ardupilot_plan_write_panel.png
      :alt: Mission Planner write panel
      :align: left

Multi-instance launch
---------------------

Each aircraft gets its own SITL. Spawn all aircraft while the simulation is
stopped, set each one's flight stack to **ArduPilot**, set Physics Hz to
**1000**, then press **Start**. In a scene with no other aircraft, the first
one you spawn is instance 0, the next one instance 1, and so on.

``-I N`` connects a SITL to the aircraft with instance ID ``N`` by adding
``10*N`` to every SITL port:

.. list-table:: Ports for the first two aircraft
   :header-rows: 1

   * - Instance ID
     - Simulator JSON, UDP
     - MAVProxy, TCP
     - Other MAVLink clients, TCP
     - MAVProxy output, UDP
   * - 0
     - 9002
     - 5760
     - 5762
     - 14550
   * - 1
     - 9012
     - 5770
     - 5772
     - 14560

``-I`` does not change the MAVLink system ID: every SITL starts as system 1.
``--auto-sysid`` gives instance ``N`` the system ID ``N + 1``, so ground
stations see the aircraft as separate vehicles.

Start each command in its aircraft's folder. SITL keeps its parameters in
``eeprom.bin`` in the current directory, and two instances started in one
directory would share that file. To run faster than real time, add ``-S N``
to every command and set the same time scale in PteroSim.

Several aircraft of one type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One command starts them all. Spawn two x500, then run:

.. code-block:: bash

   cd <release>/PteroSim/PteroSimAircrafts/x500
   sim_vehicle.py -v ArduCopter -f quad --model "JSON:$WIN_HOST" \
     -n 2 --auto-sysid \
     --add-param-file="$(pwd)/firmwares/ardupilot_x500.param" --no-rebuild

This starts instances 0 and 1 with system IDs 1 and 2, in subfolders ``0/``
and ``1/``. One MAVProxy serves both.

Aircraft of different types
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ``sim_vehicle.py`` command runs one ArduPilot binary with one parameter file
for all its instances. Aircraft of different types, or with different
parameter files, each need their own command in their own terminal. Spawn an
x500 as instance 0 and a standard_vtol as instance 1, then run:

x500, instance 0:

.. code-block:: bash

   cd <release>/PteroSim/PteroSimAircrafts/x500
   sim_vehicle.py -v ArduCopter -f quad --model "JSON:$WIN_HOST" \
     -I0 --auto-sysid \
     --add-param-file="$(pwd)/firmwares/ardupilot_x500.param" --no-rebuild

standard_vtol, instance 1:

.. code-block:: bash

   cd <release>/PteroSim/PteroSimAircrafts/standard_vtol
   sim_vehicle.py -v ArduPlane --model "JSON:$WIN_HOST" \
     -I1 --auto-sysid \
     --add-param-file="$(pwd)/firmwares/ardupilot_standard_vtol.param" --no-rebuild

The two commands can start in either order. Each one runs its own MAVProxy.

Before arming
~~~~~~~~~~~~~

Check that:

- the PteroSim Output Log shows ``ArduPilot UDP transport listening on`` for
  ports 9002 and 9012;
- MAVProxy prints ``Detected vehicle 1:1`` and ``Detected vehicle 2:1``;
- each SITL prints ``EKF3 IMU0 is using GPS``.

A normal arm command then works.

If an aircraft does not connect, check its ``-I`` number, its flight stack,
``WIN_HOST`` and the Windows firewall. A SITL still running from an earlier
launch keeps sending to its port and takes over the next aircraft with that
instance ID, so close any leftover ``arducopter``, ``arduplane`` and
``mavproxy.py`` processes before you start again.
