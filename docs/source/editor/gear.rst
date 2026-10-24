Gear
====

Gear defines the contact points that support the vehicle on the ground and
produce suspension, friction, steering, and braking forces.

In the editor
-------------

Select a gear contact to edit its name, type, position, orientation, friction,
spring, damping, steering, brake group, and retractable state. Add a contact
with **+ Add > Gear contact**. The editor can draw contact points while debug
drawing is enabled.

Stored in
---------

PteroSim writes contacts to ``Gear.xml``.

Checks
------

The vehicle must have at least one contact. Names must be unique, and spring
and damping values must be positive.
