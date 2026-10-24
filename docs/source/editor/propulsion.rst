Propulsion
==========

Propulsion defines the engines, thrusters, and the location and direction of
the thrust they produce. Each **Motor** row in the aircraft tree represents one
``<engine>`` entry.

In the editor
-------------

Select a motor to edit its name, engine definition, thruster definition,
location, orientation, and rotation sense. Add another motor with
**+ Add > Motor**. Motor order is significant; :doc:`inputs` maps autopilot
channels to zero-based motor indices in this order.

Rotation sense must match the physical propeller and its visual axis.

Stored in
---------

PteroSim writes motors to ``Propulsion.xml``. Engine and thruster definitions
are stored under ``Engines`` in the vehicle directory.

Checks
------

Engine and thruster definitions must resolve, required values must be
positive, and motor names referenced by propeller parts must exist.
