Multiple aircraft with PX4 or ArduPilot SITL
============================================

Run one SITL process for each aircraft. PteroSim pairs an aircraft's
``instance_id`` with the same SITL instance number. Spawn and configure all
aircraft while the simulation is stopped, then start the simulation. The
aircraft may be added in the UI or through the Python API; check their IDs and
link ports in the spawn output or ``aircraft_status()``. The flight stack for
each aircraft must match the autopilot you launch.

For a Windows PteroSim and SITL in WSL2, get the Windows host address from
inside WSL with:

.. code-block:: bash

   WIN_IP=$(ip route | awk '/default/ {print $3; exit}')
   echo "$WIN_IP"

SITL sends its simulator traffic to that address. PteroSim's simulator links
bind to ``0.0.0.0`` by default; permit the relevant TCP or UDP ports through
the Windows firewall if the SITL processes cannot connect.

.. list-table:: Simulator link ports
   :header-rows: 1

   * - PteroSim instance ID / SITL instance
     - PX4 simulator TCP
     - ArduPilot JSON simulator UDP
   * - 0
     - 4560
     - 9002
   * - 1
     - 4561
     - 9012
   * - N
     - ``4560 + N``
     - ``9002 + 10*N``

These are simulator links, not the MAVLink ports used by QGroundControl,
Mission Planner, or a control script. Do not connect a ground station to a
simulator link.

PX4
---

1. Spawn two aircraft with instance IDs 0 and 1, set both flight stacks to
   **PX4**, and start the PteroSim simulation. The existing
   :doc:`sitl_simulation_px4` page shows the control source panel. You can
   also use the ``spawn_pyramid_fleet.py --count 2`` example from
   PteroSimScripts on Windows; it selects PX4 and starts the simulation.

2. Build PX4 SITL in WSL, then run an instance in each of two WSL terminals.
   Give each process its own working directory so parameters and dataman
   files do not collide. Replace ``~/PX4-Autopilot`` with your checkout path.

   Terminal 1 (aircraft 0):

   .. code-block:: bash

      cd ~/PX4-Autopilot/build/px4_sitl_default
      WIN_IP=$(ip route | awk '/default/ {print $3; exit}')
      mkdir -p pterosim_0
      cd pterosim_0
      ln -sfn ../etc etc
      PX4_SYS_AUTOSTART=31000 PX4_SIM_MODEL=none_iris \
        PX4_SIM_HOSTNAME="$WIN_IP" PX4_LOCKSTEP=1 PX4_SIM_SPEED_FACTOR=1 \
        ../bin/px4 -i 0 -d etc

   Terminal 2 (aircraft 1):

   .. code-block:: bash

      cd ~/PX4-Autopilot/build/px4_sitl_default
      WIN_IP=$(ip route | awk '/default/ {print $3; exit}')
      mkdir -p pterosim_1
      cd pterosim_1
      ln -sfn ../etc etc
      PX4_SYS_AUTOSTART=31000 PX4_SIM_MODEL=none_iris \
        PX4_SIM_HOSTNAME="$WIN_IP" PX4_LOCKSTEP=1 PX4_SIM_SPEED_FACTOR=1 \
        ../bin/px4 -i 1 -d etc

   ``-i`` selects the matching PteroSim link (4560 or 4561). Use the PX4
   airframe appropriate to your aircraft; ``none_iris`` and autostart 31000
   are the x500/quad example used by the repository's launch scripts.

3. Wait for both PX4 processes to connect. Configure separate MAVLink GCS or
   API endpoints for each vehicle. The repository's formation setup sends
   instance 0 to Windows UDP 14550 and instance 1 to UDP 14551. Those
   endpoints depend on the PX4 ``px4-rc.mavlink`` configuration and must not
   be confused with TCP 4560 and 4561. Each process should have a distinct
   MAVLink system ID (normally instance number plus one).

ArduPilot
---------

1. Spawn two aircraft with instance IDs 0 and 1, set both flight stacks to
   **ArduPilot**, and start the PteroSim simulation. The existing
   :doc:`sitl_simulation_ardupilot` page shows the control source panel.
   For ArduPilot, set Physics Hz to 1000 as recommended there.

2. Build ArduCopter SITL in WSL. From the ArduPilot checkout, launch one
   ``sim_vehicle.py`` process in each of two WSL terminals. Use separate
   working directories and the parameter file appropriate to the aircraft.
   This x500 quad example uses the parameter file in PteroSimAircrafts:

   Terminal 1 (aircraft 0):

   .. code-block:: bash

      WIN_IP=$(ip route | awk '/default/ {print $3; exit}')
      mkdir -p ~/ardupilot-pterosim/instance_0
      cd ~/ardupilot-pterosim/instance_0
      python3 ~/ardupilot/Tools/autotest/sim_vehicle.py -v ArduCopter -f quad \
        --model "JSON:$WIN_IP" --no-rebuild -I 0 \
        --add-param-file /path/to/PteroSimAircrafts/x500/firmwares/ardupilot_x500.param

   Terminal 2 (aircraft 1):

   .. code-block:: bash

      WIN_IP=$(ip route | awk '/default/ {print $3; exit}')
      mkdir -p ~/ardupilot-pterosim/instance_1
      cd ~/ardupilot-pterosim/instance_1
      python3 ~/ardupilot/Tools/autotest/sim_vehicle.py -v ArduCopter -f quad \
        --model "JSON:$WIN_IP" --no-rebuild -I 1 \
        --add-param-file /path/to/PteroSimAircrafts/x500/firmwares/ardupilot_x500.param

   Replace the parameter path with its WSL path (a Windows ``C:`` path is
   typically under ``/mnt/c``). ``-I`` moves the JSON simulator link from
   UDP 9002 to 9012 for instance 1, along with ArduPilot's other instance
   ports.

3. Connect a ground station or control script to each process's **MAVLink**
   endpoint, separately from the JSON simulator links. ArduPilot's serial
   ports also move by ten per ``-I`` instance; for example its TCP MAVLink
   port starts at 5760 for instance 0 and 5770 for instance 1. Set distinct
   MAVLink system IDs when controlling multiple vehicles from one ground
   station; ``-I`` alone does not change ``SYSID_THISMAV`` in the configuration
   checked by PteroSim's connector.

If an instance does not connect, check its aircraft ID and flight stack,
the PteroSim Output Log for the listening port, the WSL host address, and
the Windows firewall. Start with two aircraft before increasing the count;
the same port formulas apply to later instances.
