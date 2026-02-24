First Steps
===========

Open the Spawn panel
--------------------

After launching PteroSim, find the **Spawn** button in the lower-left corner of the screen.  
Clicking it opens the aircraft and payload spawn panel:

.. image:: Images/spawn_panel.png
   :alt: Aircraft and payload spawn panel
   :align: center

Aircraft grid
-------------

Each aircraft card has controls of the form ``1 x 1`` and a **Dist** field:

* **1 × 1** — how many aircraft to spawn along each side of a rectangular grid  
  (for example, ``3 x 2`` spawns 3 × 2 = 6 aircraft).
* **Dist** — side length of the grid in meters, i.e. spacing between neighboring spawn points.

Aircraft types
--------------

* **F450Aircraft** — quadcopter with four rotors (classic multirotor).\n
* **DeltaQuadAircraft** — VTOL with four vertical lift rotors and one rear-facing cruise propeller.\n
* **Cessna172Aircraft** — single-engine propeller airplane (fixed-wing).

Payloads
--------

* **BasePayload** spawns a cargo box with configurable **Mass (kg)**.  
  Aircraft equipped with a gripper can lift this box and use it as a payload in scenarios.

