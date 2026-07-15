Python API Reference
====================

This reference covers the PteroSim Python SDK.

.. contents:: Sections
   :local:
   :depth: 2

pterosim.PteroSim
-----------------

.. autoclass:: pterosim.PteroSim
   :members: __init__
   :undoc-members:
   :exclude-members: close, shutdown, start, hold, resume, step_once, stop, status, clock, set_time_scale, set_physics_frequency, set_mavlink_bind_address, get_mavlink_bind_address, list_aircraft_classes, spawn, aircraft_status, get_imu, set_actuator_controls, get_actuator_configuration, set_attitude_command, go_to, cancel_go_to, set_track_gates, get_track_info, get_race_state, get_next_gate_pose, reset_race, reset_all_races, remove_track, _ACTUATOR_TYPES

Connection
^^^^^^^^^^

.. automethod:: pterosim.PteroSim.close

.. automethod:: pterosim.PteroSim.shutdown

Context manager support: ``__enter__`` / ``__exit__`` call ``close()``, not ``shutdown()``.

Simulation lifecycle
^^^^^^^^^^^^^^^^^^^^

.. automethod:: pterosim.PteroSim.start

.. automethod:: pterosim.PteroSim.hold

.. automethod:: pterosim.PteroSim.resume

.. automethod:: pterosim.PteroSim.step_once

.. automethod:: pterosim.PteroSim.stop

Simulation status
^^^^^^^^^^^^^^^^^

.. automethod:: pterosim.PteroSim.status

.. automethod:: pterosim.PteroSim.clock

Simulation settings
^^^^^^^^^^^^^^^^^^^

.. automethod:: pterosim.PteroSim.set_time_scale

.. automethod:: pterosim.PteroSim.set_physics_frequency

.. automethod:: pterosim.PteroSim.set_mavlink_bind_address

.. automethod:: pterosim.PteroSim.get_mavlink_bind_address

Aircraft management
^^^^^^^^^^^^^^^^^^^

.. automethod:: pterosim.PteroSim.list_aircraft_classes

.. automethod:: pterosim.PteroSim.spawn

.. automethod:: pterosim.Aircraft.remove

.. automethod:: pterosim.Aircraft.camera

.. automethod:: pterosim.PteroSim.aircraft_status

Sensors
^^^^^^^

.. automethod:: pterosim.PteroSim.get_imu

Actuator control
^^^^^^^^^^^^^^^^

.. automethod:: pterosim.PteroSim.set_actuator_controls

.. automethod:: pterosim.PteroSim.get_actuator_configuration

.. automethod:: pterosim.PteroSim.set_attitude_command

Navigation
^^^^^^^^^^

.. automethod:: pterosim.PteroSim.go_to

.. automethod:: pterosim.PteroSim.cancel_go_to

Racing
^^^^^^

Methods for drone racing: track configuration, gate queries, and per-aircraft race progress tracking. Requires an ``ARaceTrack`` actor in the level (created automatically by ``set_track_gates()`` if none exists).

.. automethod:: pterosim.PteroSim.set_track_gates

.. automethod:: pterosim.PteroSim.get_track_info

.. automethod:: pterosim.PteroSim.get_race_state

.. automethod:: pterosim.PteroSim.get_next_gate_pose

.. automethod:: pterosim.PteroSim.reset_race

.. automethod:: pterosim.PteroSim.reset_all_races

.. automethod:: pterosim.PteroSim.remove_track
