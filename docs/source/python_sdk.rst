Python SDK Commands (15 RPCs)
=============================

These commands are executed in a Python console or script using the PteroSim SDK
(``scripts/sim_control/test_sdk.py``, ``Plugins/PteroSimScripting/SDK/python/``).

.. list-table:: Available RPC Commands
   :header-rows: 1
   :widths: 5 20 30 45

   * - #
     - RPC
     - Python usage
     - Description
   * - 1
     - GetStatus
     - ``sim.status()``
     - Returns simulation run state, time scale, physics frequency, and aircraft count.
   * - 2
     - SetTimeScale
     - ``sim.set_time_scale(2.0)``
     - Sets simulation time multiplier (e.g. 2.0 = 2× real time).
   * - 3
     - SetPhysicsFrequency
     - ``sim.set_physics_frequency(500.0)``
     - Sets physics update rate in Hz.
   * - 4
     - SetMavlinkBindAddress
     - ``sim.set_mavlink_bind_address("127.0.0.1")``
     - Sets MAVLink bind address for telemetry.
   * - 5
     - GetMavlinkBindAddress
     - ``sim.get_mavlink_bind_address()``
     - Returns current MAVLink bind address.
   * - 6
     - GetSimulationClock
     - ``sim.clock()``
     - Returns clock state, sim time, step number, frequency, and time scale.
   * - 7
     - ListAircraftClasses
     - ``sim.list_aircraft_classes()``
     - Returns available aircraft types (e.g. F450, DeltaQuad).
   * - 8
     - SpawnAircraft
     - ``drone = sim.spawn("F450", x=0, y=0, z=200)``
     - Spawns an aircraft of given class at x, y, z.
   * - 9
     - GetAircraftStatus
     - ``sim.aircraft_status()``
     - Returns status of all spawned aircraft.
   * - 10
     - Start
     - ``sim.start()``
     - Starts simulation (physics running).
   * - 11
     - Hold
     - ``sim.hold()``
     - Pauses simulation.
   * - 12
     - StepOnce
     - ``sim.step_once()``
     - Advances simulation by one physics step.
   * - 13
     - Resume
     - ``sim.resume()``
     - Resumes simulation after hold.
   * - 14
     - RemoveAircraft
     - ``drone.remove()``
     - Removes the aircraft and returns remaining count.
   * - 15
     - Stop
     - ``sim.stop()``
     - Stops simulation.

Example
-------

Run all 15 RPCs:

.. code-block:: bash

   python scripts/sim_control/test_sdk.py
