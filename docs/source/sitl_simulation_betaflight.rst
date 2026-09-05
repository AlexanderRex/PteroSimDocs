SITL simulation with BetaFlight
===============================

.. note::

   This workflow is Linux only.

1. **Start PteroSim**, spawn the F450 drone while the simulation is stopped, then press **Start** on the simulation panel.

2. In the control source panel choose **BetaFlight**.

3. **Launch BetaFlight SITL** in a new terminal. PteroSim is on the same machine, so the default localhost address is correct and no ``--ip`` flag is needed:

   .. code-block:: bash

      cd ~/betaflight
      ./obj/main/betaflight_SITL.elf

   Leave it running.

4. **Launch websockify** in a new terminal. It bridges the BetaFlight SITL TCP interface (port 5761) to the WebSocket endpoint used by the App:

   .. code-block:: bash

      python3 -m websockify 127.0.0.1:6761 127.0.0.1:5761

   Leave it running.

5. **Launch the Betaflight App** and connect manually to ``ws://127.0.0.1:6761``.

6. **Launch the RC bridge** in a new terminal. It sends controller input to BetaFlight on UDP port 9004:

   .. code-block:: bash

      python3 ~/xbox_to_betaflight.py

7. **Fly.**