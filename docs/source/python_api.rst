Python API Reference
====================

This reference covers the PteroSim Python SDK.

.. contents:: Sections
   :local:
   :depth: 2

pterosim.PteroSim
-----------------

Client for PteroSim flight simulator. Manages the connection to the simulation server and provides methods to control simulation state, spawn aircraft, and query status.

.. py:class:: PteroSim(address="localhost:10010")

   :param address: gRPC server address.
   :type address: str

Connection
^^^^^^^^^^

.. py:method:: close()

   Close the gRPC channel without shutting down the simulator.

.. py:method:: shutdown()

   Shut down the simulator application and close the connection.

Context manager support: ``__enter__`` / ``__exit__`` call ``close()``, not ``shutdown()``.

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

.. py:method:: camera(sensor_name="Camera", *, width=0, height=0, timeout=10.0)

   Capture a camera frame from this aircraft (on-demand, blocks until GPU readback completes).
   Called on the ``Aircraft`` handle returned by ``spawn()``.

   :param sensor_name: Name of the camera sensor component (default "Camera").
   :type sensor_name: str
   :param width: Requested width in pixels (0 = component default).
   :type width: int
   :param height: Requested height in pixels (0 = component default). Both ``width`` and ``height`` must be set, or both 0.
   :type height: int
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

Sensors
^^^^^^^

.. py:method:: get_imu(instance_id)

   Get IMU reading for an aircraft.

   :param instance_id: Aircraft instance ID.
   :type instance_id: int
   :return: IMU sample in body FRD frame.
   :rtype: IMUReading

   ``IMUReading`` fields:

   * **acceleration** (*tuple[float, float, float]*) — Specific force in m/s^2.
   * **angular_velocity** (*tuple[float, float, float]*) — Angular rates in rad/s.
   * **magnetic_field** (*tuple[float, float, float]*) — Magnetic field in uT.
   * **timestamp_simulation_s** (*float*) — Simulation timestamp in seconds.

Actuator control
^^^^^^^^^^^^^^^^

.. py:method:: set_actuator_controls(instance_id, controls, timestamp_usec=0)

   Send normalized actuator channel values directly to the aircraft.
   This bypasses autopilot control and is commonly used in RL motor-control loops.

   :param instance_id: Aircraft instance ID.
   :type instance_id: int
   :param controls: Actuator channel values (mapping depends on aircraft configuration).
   :type controls: list[float]
   :param timestamp_usec: Optional command timestamp in microseconds.
   :type timestamp_usec: int

.. py:method:: get_actuator_configuration(instance_id)

   Get actuator channel layout for an aircraft.

   :param instance_id: Aircraft instance ID.
   :type instance_id: int
   :return: Actuator mapping and channel count.
   :rtype: ActuatorConfiguration

   ``ActuatorConfiguration`` fields:

   * **instance_id** (*int*) — Aircraft instance ID.
   * **channel_count** (*int*) — Number of required control channels.
   * **mappings** (*list[ActuatorMapping]*) — Per-channel mapping descriptors.

   ``ActuatorMapping`` fields:

   * **channel** (*int*) — Channel index in controls array.
   * **type** (*str*) — Actuator type (for example ``motor``, ``elevator``, ``rudder``).
   * **component_index** (*int*) — Index within actuator type.
   * **input_min** (*float*) — Expected minimum input value.
   * **input_max** (*float*) — Expected maximum input value.
   * **name** (*str*) — Human-readable actuator name.

.. py:method:: set_attitude_command(instance_id, roll_rad=0.0, pitch_rad=0.0, yaw_rate_rad_sec=0.0, throttle=0.0, enabled=True)

   Send attitude command to the QuadX attitude controller running in C++ at physics rate.
   When enabled, this controller overrides motor throttles from ``set_actuator_controls()``.

   :param instance_id: Aircraft instance ID.
   :type instance_id: int
   :param roll_rad: Desired roll angle in radians.
   :type roll_rad: float
   :param pitch_rad: Desired pitch angle in radians.
   :type pitch_rad: float
   :param yaw_rate_rad_sec: Desired yaw rate in radians per second.
   :type yaw_rate_rad_sec: float
   :param throttle: Base thrust in range ``[0, 1]``.
   :type throttle: float
   :param enabled: Enable or disable the attitude controller.
   :type enabled: bool

Navigation
^^^^^^^^^^

.. py:method:: go_to(instance_id, x, y, z, yaw=0.0, *, acceptance_radius_cm=0.0)

   Fly to a UE world position (cm) via pilot sticks and hold the given yaw.
   Also available on the ``Aircraft`` handle as ``drone.go_to(...)``.

   :param instance_id: Aircraft instance ID.
   :type instance_id: int
   :param x: Target X position in UE cm.
   :type x: float
   :param y: Target Y position in UE cm.
   :type y: float
   :param z: Target Z position in UE cm.
   :type z: float
   :param yaw: Desired yaw in degrees (default 0.0).
   :type yaw: float
   :param acceptance_radius_cm: Arrival radius in cm (0 = controller default).
   :type acceptance_radius_cm: float

.. py:method:: cancel_go_to(instance_id)

   Stop GoTo navigation and zero pilot sticks.
   Also available on the ``Aircraft`` handle as ``drone.cancel_go_to()``.

   :param instance_id: Aircraft instance ID.
   :type instance_id: int

Racing
^^^^^^

Methods for drone racing: track configuration, gate queries, and per-aircraft race progress tracking. Requires an ``ARaceTrack`` actor in the level (created automatically by ``set_track_gates()`` if none exists).

.. py:method:: set_track_gates(gates)

   Create or update a race track with the given gate definitions. If no ``ARaceTrack`` exists in the world, one is spawned automatically. After setting gates, all existing aircraft are registered with the track.

   Each gate is a dict with position keys (``x``, ``y``, ``z``) and optional rotation keys (``yaw``, ``pitch``, ``roll``, default 0).

   :param gates: List of gate definition dicts.
   :type gates: list[dict]
   :return: Resulting track info with actual gate center positions.
   :rtype: RaceTrackInfo

.. py:method:: get_track_info()

   Get the race track layout (gate positions and forward vectors).

   :return: Track information.
   :rtype: RaceTrackInfo

   ``RaceTrackInfo`` fields:

   * **gate_count** (*int*) — Number of gates on the track.
   * **gates** (*list[GatePose]*) — List of gate poses.

   ``GatePose`` fields:

   * **gate_index** (*int*) — Gate index in track sequence.
   * **x** (*float*) — Gate center X position (UE cm).
   * **y** (*float*) — Gate center Y position (UE cm).
   * **z** (*float*) — Gate center Z position (UE cm).
   * **forward_x** (*float*) — Gate forward vector X component.
   * **forward_y** (*float*) — Gate forward vector Y component.
   * **forward_z** (*float*) — Gate forward vector Z component.

.. py:method:: get_race_state(instance_id)

   Get race progress for a specific aircraft.

   :param instance_id: Aircraft instance ID.
   :type instance_id: int
   :return: Race progress state.
   :rtype: RaceState

   ``RaceState`` fields:

   * **instance_id** (*int*) — Aircraft instance ID.
   * **next_gate_index** (*int*) — Index of the next gate the aircraft should pass.
   * **gates_passed** (*int*) — Total number of gates passed.
   * **laps_completed** (*int*) — Number of complete laps.
   * **last_gate_passed_time** (*float*) — Simulation time (seconds) when the last gate was passed. 0.0 if no gate passed yet.

.. py:method:: get_next_gate_pose(instance_id)

   Get the pose of the next gate for an aircraft. Shortcut for RL observation — avoids separate ``get_track_info()`` + ``get_race_state()`` calls.

   :param instance_id: Aircraft instance ID.
   :type instance_id: int
   :return: Pose of the next gate.
   :rtype: GatePose

.. py:method:: reset_race(instance_id)

   Reset race tracking for one aircraft (next gate, gates passed, laps, timing). Use at the start of each RL episode.

   :param instance_id: Aircraft instance ID.
   :type instance_id: int

.. py:method:: reset_all_races()

   Reset race tracking for all registered aircraft. Useful for multi-agent RL episode resets.

.. py:method:: remove_track()

   Remove current race track and all configured gates from the world.
