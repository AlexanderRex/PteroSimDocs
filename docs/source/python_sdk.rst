Python SDK
==========

The PteroSim Python SDK provides gRPC-based programmatic control of the simulation. Commands are executed in a Python console or script.

**SDK location:** ``Plugins/PteroSimScripting/SDK/python/``

**Example script:** ``scripts/sim_control/test_sdk.py``

---

Simulation control
------------------

``sim.start()`` — Start simulation (physics running).

``sim.hold()`` — Pause simulation.

``sim.resume()`` — Resume simulation after hold.

``sim.step_once()`` — Advance simulation by one physics step.

``sim.stop()`` — Stop simulation.

---

Simulation status
-----------------

``sim.status()`` — Returns simulation run state, time scale, physics frequency, and aircraft count.

``sim.clock()`` — Returns clock state, sim time, step number, frequency, and time scale.

---

Simulation settings
-------------------

``sim.set_time_scale(2.0)`` — Sets simulation time multiplier (e.g. 2.0 = 2× real time).

``sim.set_physics_frequency(500.0)`` — Sets physics update rate in Hz.

``sim.set_mavlink_bind_address("127.0.0.1")`` — Sets MAVLink bind address for telemetry.

``sim.get_mavlink_bind_address()`` — Returns current MAVLink bind address.

---

Aircraft management
-------------------

``sim.list_aircraft_classes()`` — Returns available aircraft types (e.g. F450, DeltaQuad).

``sim.spawn("F450", x=0, y=0, z=200)`` — Spawns an aircraft of given class at specified coordinates.

``sim.aircraft_status()`` — Returns status of all spawned aircraft.

``drone.remove()`` — Removes the aircraft and returns remaining count.

---

Quick test
----------

Run all 15 RPCs with the test script:

.. code-block:: bash

   python scripts/sim_control/test_sdk.py
