Tanks
=====

Tanks hold fuel or oxidizer. Their contents change vehicle mass, centre of
gravity, and inertia during a run.

In the editor
-------------

Select a tank to edit its type, position, capacity, initial contents, density,
temperature, priority, and drain behaviour. Add another with
**+ Add > Tank**. Tank order is the JSBSim tank index used by engines.

Stored in
---------

PteroSim stores tanks in ``Propulsion.xml``.

Checks
------

Capacity must be above zero, contents cannot exceed capacity, and density and
temperature must be valid for the selected tank type.
