Python API Reference
====================

This reference covers the PteroSim Python SDK.

.. contents:: Sections
   :local:
   :depth: 2

pterosim.PteroSim
-----------------

Client for PteroSim flight simulator. Manages the connection to the simulation server and provides methods to control simulation state, spawn aircraft, and query status.

.. py:class:: PteroSim(address="localhost:50051")

   :param address: gRPC server address.
   :type address: str

Connection
^^^^^^^^^^

.. py:method:: close()

   Close the gRPC channel.

**Context manager support:**

.. code-block:: python

   with PteroSim("localhost:50051") as sim:
       sim.start()
       # ...

Simulation lifecycle
^^^^^^^^^^^^^^^^^^^^

.. py:method:: start()

   Start simulation (physics running).

.. py:method:: hold()

   Pause simulation.

.. py:method:: resume()

   Resume simulation after hold.

.. py:method:: step_once()

   Execute a single simulation step then hold. Simulation must be started.

.. py:method:: stop()

   Stop simulation.

Simulation status
^^^^^^^^^^^^^^^^^

.. py:method:: status()

   Returns simulation status.

   :return: Simulation state information.
   :rtype: SimStatus

   ``SimStatus`` fields:

   * **is_running** (*bool*) — Whether the simulation is currently running.
   * **time_scale** (*float*) — Current time scale multiplier.
   * **physics_frequency_hz** (*float*) — Physics update rate in Hz.
   * **aircraft_count** (*int*) — Number of spawned aircraft.

.. py:method:: clock()

   Get simulation clock state.

   :return: Clock information.
   :rtype: ClockInfo

   ``ClockInfo`` fields:

   * **simulation_time** (*float*) — Current simulation time in seconds.
   * **step_number** (*int*) — Current simulation step number.
   * **target_frequency_hz** (*float*) — Target physics frequency.
   * **actual_frequency_hz** (*float*) — Actual achieved frequency.
   * **clock_state** (*str*) — Clock state: "holding", "running", or "step_once".
   * **time_scale** (*float*) — Current time scale.

Simulation settings
^^^^^^^^^^^^^^^^^^^

.. py:method:: set_time_scale(scale)

   Sets simulation time multiplier (e.g. 2.0 = 2x real time).

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

   ``AircraftClass`` fields:

   * **name** (*str*) — Aircraft class name (e.g. "F450", "DeltaQuad").
   * **description** (*str*) — Human-readable description.

.. py:method:: spawn(aircraft_class, *, lat=None, lon=None, alt=None, x=None, y=None, z=None, yaw=0.0, pitch=0.0, roll=0.0)

   Spawn an aircraft. Use ``lat/lon/alt`` for geographic coordinates or ``x/y/z`` for Unreal Engine coordinates.
   Returns an ``Aircraft`` handle with ``instance_id``, ``mavlink_port``, ``remove()`` and ``camera()`` methods.

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
   :param pitch: Pitch rotation in degrees (default 0.0).
   :type pitch: float
   :param roll: Roll rotation in degrees (default 0.0).
   :type roll: float
   :return: Handle to the spawned aircraft.
   :rtype: Aircraft

.. py:method:: remove()

   Destroy this aircraft. Called on the ``Aircraft`` handle returned by ``spawn()``.

   :return: Remaining aircraft count.
   :rtype: int

.. py:method:: camera(sensor_name="Camera", *, timeout=10.0)

   Capture a camera frame from this aircraft (on-demand, blocks until GPU readback completes).
   Called on the ``Aircraft`` handle returned by ``spawn()``.

   :param sensor_name: Name of the camera sensor component (default "Camera").
   :type sensor_name: str
   :param timeout: gRPC timeout in seconds (default 10.0).
   :type timeout: float
   :return: Camera frame with BGR image data.
   :rtype: CameraFrame

   ``CameraFrame`` fields:

   * **image** (*numpy.ndarray*) — BGR image array (H, W, 3), dtype=uint8. Directly usable with ``cv2.imshow()``.
   * **width** (*int*) — Frame width in pixels.
   * **height** (*int*) — Frame height in pixels.
   * **timestamp** (*float*) — SimClock time when frame was captured.
   * **sequence_number** (*int*) — Monotonically increasing frame counter.

.. py:method:: aircraft_status()

   Get status of all spawned aircraft.

   :return: List of aircraft statuses.
   :rtype: list[AircraftStatus]

   ``AircraftStatus`` fields:

   * **instance_id** (*int*) — Unique identifier of the aircraft.
   * **aircraft_name** (*str*) — Aircraft class name.
   * **run_state** (*str*) — Run state: "running", "holding", or "step_once".
   * **actual_frequency_hz** (*float*) — Actual physics frequency.
   * **target_frequency_hz** (*float*) — Target physics frequency.
   * **step_count** (*int*) — Number of simulation steps executed.
   * **crashed** (*bool*) — Whether the aircraft has crashed.
   * **time_scale** (*float*) — Current time scale.
   * **mavlink_port** (*int*) — MAVLink TCP port.

**Example — full aircraft lifecycle:**

.. code-block:: python

   drone = sim.spawn("F450", lat=55.0, lon=37.0, alt=100.0)
   print(drone.instance_id)    # 0
   print(drone.mavlink_port)   # 4560

   frame = drone.camera()      # capture camera image
   drone.remove()              # destroy aircraft
