Python API Reference
====================

This reference contains all the details of the PteroSim Python API.

pterosim.PteroSim
-----------------

Client for PteroSim flight simulator. Manages the connection to the simulation server and provides methods to control simulation state, spawn aircraft, and query status.

**Constructor:**

.. py:class:: PteroSim(address="localhost:50051")

   :param address: gRPC server address.
   :type address: str

**Methods:**

Simulation control
^^^^^^^^^^^^^^^^^^

.. py:method:: start()

   Start simulation (physics running).

.. py:method:: stop()

   Stop simulation.

.. py:method:: hold()

   Pause simulation.

.. py:method:: resume()

   Resume simulation after hold.

.. py:method:: step_once()

   Execute a single simulation step then hold. Simulation must be started.

Simulation status
^^^^^^^^^^^^^^^^^

.. py:method:: status()

   Returns simulation status.

   :return: Simulation state information.
   :rtype: SimStatus

.. py:method:: clock()

   Get simulation clock state.

   :return: Clock information.
   :rtype: ClockInfo

Simulation settings
^^^^^^^^^^^^^^^^^^^

.. py:method:: set_time_scale(scale)

   Sets simulation time multiplier (e.g. 2.0 = 2× real time).

   :param scale: Time scale factor.
   :type scale: float

.. py:method:: set_physics_frequency(hz)

   Sets physics update rate in Hz.

   :param hz: Frequency in Hz.
   :type hz: float

.. py:method:: set_mavlink_bind_address(address)

   Set MAVLink bind address for telemetry. Simulation must not be running.

   :param address: Bind address (e.g. "127.0.0.1").
   :type address: str

.. py:method:: get_mavlink_bind_address()

   Returns current MAVLink bind address.

   :return: Bind address.
   :rtype: str

Aircraft management
^^^^^^^^^^^^^^^^^^^

.. py:method:: list_aircraft_classes()

   Returns available aircraft types.

   :return: List of aircraft classes.
   :rtype: list[AircraftClass]

.. py:method:: spawn(aircraft_class, *, lat=None, lon=None, alt=None, x=None, y=None, z=None, yaw=0.0)

   Spawn an aircraft. Use ``lat/lon/alt`` for geographic coordinates or ``x/y/z`` for Unreal Engine coordinates.

   :param aircraft_class: Aircraft type name (e.g. "F450", "DeltaQuad").
   :type aircraft_class: str
   :param lat: Latitude in degrees.
   :type lat: float
   :param lon: Longitude in degrees.
   :type lon: float
   :param alt: Altitude in meters.
   :type alt: float
   :param x: X coordinate in UE units.
   :type x: float
   :param y: Y coordinate in UE units.
   :type y: float
   :param z: Z coordinate in UE units.
   :type z: float
   :param yaw: Yaw rotation in degrees (default 0.0).
   :type yaw: float
   :return: Handle to the spawned aircraft.
   :rtype: Aircraft

.. py:method:: aircraft_status()

   Get status of all spawned aircraft.

   :return: List of aircraft statuses.
   :rtype: list[AircraftStatus]

Connection management
^^^^^^^^^^^^^^^^^^^^^

.. py:method:: close()

   Close the gRPC channel.

**Context manager support:**

.. code-block:: python

   with PteroSim("localhost:50051") as sim:
       sim.start()
       # ...

pterosim.Aircraft
-----------------

Handle to a spawned aircraft in PteroSim. Returned by ``PteroSim.spawn()``.

**Instance Variables:**

* **instance_id** (*int*) — Unique identifier of the aircraft instance.
* **mavlink_port** (*int*) — MAVLink TCP port (4560 + instance_id).

**Methods:**

.. py:method:: remove()

   Destroy this aircraft.

   :return: Remaining aircraft count.
   :rtype: int

pterosim.SimStatus
------------------

Simulation status information. Returned by ``PteroSim.status()``.

**Instance Variables:**

* **is_running** (*bool*) — Whether the simulation is currently running.
* **time_scale** (*float*) — Current time scale multiplier.
* **physics_frequency_hz** (*float*) — Physics update rate in Hz.
* **aircraft_count** (*int*) — Number of spawned aircraft.

pterosim.ClockInfo
------------------

Simulation clock information. Returned by ``PteroSim.clock()``.

**Instance Variables:**

* **simulation_time** (*float*) — Current simulation time in seconds.
* **step_number** (*int*) — Current simulation step number.
* **target_frequency_hz** (*float*) — Target physics frequency.
* **actual_frequency_hz** (*float*) — Actual achieved frequency.
* **clock_state** (*str*) — Clock state: "holding", "running", or "step_once".
* **time_scale** (*float*) — Current time scale.

pterosim.AircraftClass
----------------------

Aircraft class information. Returned by ``PteroSim.list_aircraft_classes()``.

**Instance Variables:**

* **name** (*str*) — Aircraft class name (e.g. "F450", "DeltaQuad").
* **description** (*str*) — Human-readable description.

pterosim.AircraftStatus
-----------------------

Status of a spawned aircraft. Returned by ``PteroSim.aircraft_status()``.

**Instance Variables:**

* **instance_id** (*int*) — Unique identifier of the aircraft.
* **aircraft_name** (*str*) — Aircraft class name.
* **run_state** (*str*) — Run state: "running", "holding", or "step_once".
* **actual_frequency_hz** (*float*) — Actual physics frequency.
* **target_frequency_hz** (*float*) — Target physics frequency.
* **step_count** (*int*) — Number of simulation steps executed.
* **crashed** (*bool*) — Whether the aircraft has crashed.
* **time_scale** (*float*) — Current time scale.
* **mavlink_port** (*int*) — MAVLink TCP port.
