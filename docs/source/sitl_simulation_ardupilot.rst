SITL simulation with ArduPilot
==============================

1. **Start** PteroSim and spawn the F450 drone.
   For ArduPilot, it is recommended to set Physics Hz to **1000** with the top slider.

2. On Ubuntu/WSL, head to ArduPilot folder and launch ArduPilot SITL while putting your **Ubuntu IP address** in ``JSON:[IP-address]``:

   .. code-block:: bash

      python3 Tools/autotest/sim_vehicle.py -v ArduCopter -f quad --model JSON:[IP-address] --no-rebuild -w -P FRAME_TYPE=1

   This command is an **F450 quad example**. Other vehicle types use different ``sim_vehicle.py`` options (vehicle type, frame, and parameters).

3. Launch **Mission Planner** and open the **Plan** tab in the top left of the screen:

   .. image:: Images/ardupilot_plan_top_tabs.png
      :alt: Mission Planner top tabs with Plan selected
      :align: left

4. Build a mission either from the bottom waypoint table or by right-clicking on the map. Then click **Write** on the panel on the right side of the screen to upload the mission:

   .. image:: Images/ardupilot_plan_map_context_menu.png
      :alt: Mission Planner map right-click mission menu
      :align: left

5. Go to the **Data** tab. Open **Actions** and click **Arm/Disarm**. Select **mission_start** and click **Do Action**.
  
   .. image:: Images/ardupilot_plan_write_panel.png
      :alt: Mission Planner write panel
      :align: left