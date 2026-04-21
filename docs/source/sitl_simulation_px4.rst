SITL simulation with PX4
========================


1. **Start PteroSim**, press **Start** on the simulation panel, and spawn the aircraft (e.g. F450). You may start PX4 before or after; lockstep engages once PX4 connects.

2. **Run PX4 SITL** on Linux/WSL with lockstep and put your **Ubuntu IP address** in ``[IP-address]``:

   .. code-block:: bash

      PX4_SIM_HOSTNAME=[IP-address] PX4_LOCKSTEP=1 PX4_SIM_SPEED_FACTOR=1 make px4_sitl none_iris

   The PteroSim repo also ships helpers that set the same environment and launch ``px4`` with per-instance rootfs: ``scripts/px4_launch/run_instance.sh [instance] [model]`` and ``scripts/px4_launch/run_multiple_instances.sh`` (defaults: ``none_iris``, TCP **4560+N**, system id **N+1** - see script echo output).

3. Open **Application Settings**:

   .. image:: Images/qgc_main_menu.png
      :alt: QGroundControl main menu and Application Settings
      :align: left

4. Add or edit a **Comm Link** to your PX4 instance (UDP to the machine where SITL runs, typically port **14550**):

   .. image:: Images/qgc_comm_link.png
      :alt: QGroundControl communication link configuration
      :align: left

5. Manually connect using the configured link:

   .. image:: Images/qgc_connect_link.png
      :alt: QGroundControl select link to connect
      :align: left

   After the link is online, use **Plan** / **Fly** as with normal SITL.
