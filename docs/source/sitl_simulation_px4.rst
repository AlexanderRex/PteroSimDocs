SITL simulation with PX4
========================


1. **Start PteroSim**, press **Start** on the simulation panel, and spawn the aircraft (e.g. F450). You may start PX4 before or after; lockstep engages once PX4 connects.

2. In the panel on the right, click the drone and select the corresponding control source.

3. **Run PX4 SITL** on Linux/WSL with lockstep and put your **Ubuntu IP address** in ``[IP-address]``:

   .. code-block:: bash

      PX4_SIM_HOSTNAME=[IP-address] PX4_LOCKSTEP=1 PX4_SIM_SPEED_FACTOR=1 make px4_sitl none_iris

4. Launch **QGroundControl** and open **Application Settings**:

   .. image:: Images/qgc_main_menu.png
      :alt: QGroundControl main menu and Application Settings
      :align: left

5. Add or edit a **Comm Link** to your PX4 instance (UDP to the machine where SITL runs, typically port **14550**):

   .. image:: Images/qgc_comm_link.png
      :alt: QGroundControl communication link configuration
      :align: left

   .. image:: Images/qgc_comm_link_edit.png
      :alt: QGroundControl comm link edit window with server address
      :align: left

6. Manually connect using the configured link:

   .. image:: Images/qgc_connect_link.png
      :alt: QGroundControl select link to connect
      :align: left

7. Head to **Plan Flight**:

   .. image:: Images/qgc_plan_flight.png
      :alt: QGroundControl main screen with Plan Flight highlighted
      :align: left

8. Create flight plan using options on the pannel on the left of the screen and press Upload button to upload the plan.

   .. image:: Images/qgc_plan_upload.png
      :alt: QGroundControl plan editor and Upload button
      :align: left

9. Exit planning mode and use the takeoff slider.

   .. image:: Images/qgc_takeoff_slider.png
      :alt: QGroundControl takeoff slider prompt
      :align: left
