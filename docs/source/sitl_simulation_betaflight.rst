SITL simulation with BetaFlight
===============================

.. note::

   This workflow is Linux only.

1. **Start PteroSim**, spawn the F450 drone while the simulation is stopped, then press **Start** on the simulation panel.

2. In the control source panel choose **BetaFlight**.

3. **Launch BetaFlight SITL**:

   .. code-block:: bash

      cd ~/betaflight
      ./obj/main/betaflight_SITL.elf

   Leave it running.

4. **Launch websockify**:

   .. code-block:: bash

      python3 -m websockify 127.0.0.1:6761 127.0.0.1:5761

   Leave it running.

5. **Launch the Betaflight App** and connect to ``ws://127.0.0.1:6761``:

   .. image:: Images/betaflight_manual_connect.png
      :alt: Betaflight Configurator manual connection
      :align: left

   .. image:: Images/betaflight_manual_connect_2.png
      :alt: Betaflight Configurator manual connection
      :align: left

6. **Launch the RC bridge**:

   .. code-block:: bash

      python3 ~/xbox_to_betaflight.py

7. **Fly.**