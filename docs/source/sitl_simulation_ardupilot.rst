SITL simulation with ArduPilot
==============================

Single-instance launch
----------------------

1. **Start PteroSim**, spawn the F450 drone while the simulation is stopped,
   then press **Start** on the simulation panel. For ArduPilot, set Physics Hz
   to **1000** with the top slider.

2. In the control source panel choose **ArduPilot**:

   .. image:: Images/control_source_ardupilot.png
      :alt: Control Source panel with ArduPilot selected
      :class: no-float-left

3. In Ubuntu/WSL, run ArduPilot SITL from the ArduPilot checkout. The JSON
   host is the Windows address as seen from WSL:

   .. code-block:: bash

      WIN_HOST=$(ip route | awk '/default/ {print $3; exit}')
      python3 Tools/autotest/sim_vehicle.py -v ArduCopter -f quad \
        --model "JSON:$WIN_HOST" --no-rebuild -w -P FRAME_TYPE=1

   This is an **F450 quad example**. Other vehicles need the appropriate
   vehicle type, frame, and parameters. If WSL is configured to forward
   Windows localhost, ``127.0.0.1`` may also work as the JSON host.

4. Launch **Mission Planner** and open the **Plan** tab in the top left of
   the screen:

   .. image:: Images/ardupilot_plan_top_tabs.png
      :alt: Mission Planner top tabs with Plan selected
      :align: left

5. Build a mission either from the bottom waypoint table or by right-clicking
   on the map. Click **Write** on the panel on the right to upload it:

   .. image:: Images/ardupilot_plan_map_context_menu.png
      :alt: Mission Planner map right-click mission menu
      :align: left

6. Go to the **Data** tab. Open **Actions** and click **Arm/Disarm**. Select
   **mission_start** and click **Do Action**.

   .. image:: Images/ardupilot_plan_write_panel.png
      :alt: Mission Planner write panel
      :align: left

Multi-instance launch
---------------------

Run one ArduPilot SITL instance for each aircraft in PteroSim. Spawn all
aircraft while the simulation is stopped, set each flight stack to
**ArduPilot**, set Physics Hz to **1000**, then start the simulation. The SITL
instance number ``-I N`` must match the aircraft's ``instance_id``.

.. list-table:: Ports for the first two aircraft
   :header-rows: 1

   * - Instance ID
     - JSON simulator UDP on Windows
     - MAVProxy TCP in WSL
     - Free TCP for another MAVLink client
     - MAVProxy UDP output
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

For later instances, the JSON port is ``9002 + 10*N`` and ArduPilot's TCP
ports advance by ten per instance. The JSON links carry simulator data;
ground stations and control scripts use the separate MAVLink ports. Give
each SITL a distinct MAVLink system ID: ``-I`` alone does not change it.

The commands below start in the PteroSim project root mounted in WSL.
Starting ``wsl`` from a Windows shell in that root opens its ``/mnt/c``
directory; use ``pwd`` to confirm. They use the WSL default gateway as the
Windows host address. In the live check it was ``172.26.48.1``. The tested
ArduPilot checkout was ``~/Documents/ardupilot`` at ``6dd6c4e1`` and
MAVProxy was in ``~/.local/bin``; adjust the checkout path if yours differs.
Build the needed SITL binaries before using ``-N`` below. ``-S 2`` sets SITL
speed to 2x; set PteroSim time scale to **2** as well. For normal speed,
remove ``-S 2`` and use PteroSim time scale 1.

Two identical x500 quadcopters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spawn two x500 aircraft with IDs 0 and 1. Run one command from the x500
aircraft directory:

.. code-block:: bash

   cd PteroSimAircrafts/x500
   export PATH="$HOME/.local/bin:$PATH"
   WIN_HOST=$(ip route | awk '/default/ {print $3; exit}')
   python3 ~/Documents/ardupilot/Tools/autotest/sim_vehicle.py \
     -v ArduCopter -f quad --model "JSON:$WIN_HOST" \
     -n 2 --auto-sysid \
     --add-param-file="$(pwd)/firmwares/ardupilot_x500.param" \
     -N -S 2

This starts instances 0 and 1 with system IDs 1 and 2. ``sim_vehicle.py``
creates separate ``0/`` and ``1/`` subdirectories containing their EEPROM,
logs, and terrain; one MAVProxy serves both aircraft. Use the absolute WSL
parameter path shown above. In the tested ``sim_vehicle.py``, a relative
``firmwares/ardupilot_x500.param`` was not resolved from the child
directories and both SITL processes exited.

Two different aircraft (x500 and standard_vtol)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Spawn x500 as instance 0 and standard_vtol as instance 1. Use two WSL
terminals, each starting in the PteroSim project root. Launch order does
not matter.

x500, instance 0:

.. code-block:: bash

   cd PteroSimAircrafts/x500
   export PATH="$HOME/.local/bin:$PATH"
   WIN_HOST=$(ip route | awk '/default/ {print $3; exit}')
   python3 ~/Documents/ardupilot/Tools/autotest/sim_vehicle.py \
     -v ArduCopter -f quad --model "JSON:$WIN_HOST" \
     -I0 --sysid 1 --add-param-file="$(pwd)/firmwares/ardupilot_x500.param" \
     -N -S 2

standard_vtol, instance 1:

.. code-block:: bash

   cd PteroSimAircrafts/standard_vtol
   export PATH="$HOME/.local/bin:$PATH"
   WIN_HOST=$(ip route | awk '/default/ {print $3; exit}')
   python3 ~/Documents/ardupilot/Tools/autotest/sim_vehicle.py \
     -v ArduPlane --model "JSON:$WIN_HOST" \
     -I1 --sysid 2 \
     --add-param-file="$(pwd)/firmwares/ardupilot_standard_vtol.param" \
     -N -S 2

Separate aircraft directories prevent the two single-instance launches
from sharing one ``eeprom.bin``. Each SITL has its own MAVProxy.

Check both connections
~~~~~~~~~~~~~~~~~~~~~~

Check that the PteroSim Output Log shows listeners on UDP 9002 and 9012,
that MAVLink reports system IDs 1 and 2, and that each SITL reports
``EKF3 IMU0 is using GPS`` before arming. Use a normal arm command; force
arming was not needed in the live check. The local SITL printed
``Arming checks disabled``, so that result did not verify active prearm
checks. Both x500 + x500 and x500 + standard_vtol connected and accepted
normal arm commands at Physics Hz 1000 and time scale 2. The mixed pair
also worked when instance 1 started before instance 0.

If an instance does not connect, verify its ``-I`` number, system ID,
flight stack, JSON host address, and Windows firewall. Under tmux, Ctrl+C
or ``tmux kill-session`` may leave SITL or MAVProxy processes running;
check and close them before restarting.
