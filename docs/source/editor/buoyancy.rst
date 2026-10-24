Buoyancy
========

Buoyancy defines lifting-gas cells for balloons and airships. JSBSim derives
lift, gas mass, and gas inertia from each cell's shape and atmospheric state.

In the editor
-------------

Select a gas cell to choose its gas and edit its position, semi-axes or box
widths, initial fullness, relief pressure, and valve rate. Existing buoyant
vehicles can add and remove cells from this section.

Stored in
---------

PteroSim writes buoyant forces to ``BuoyantForces.xml``. Gas mass contributes
to the vehicle mass balance.

Checks
------

A cell must have a positive volume. Fullness must be between zero and one;
pressure and valve values cannot be negative.
