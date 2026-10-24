Mass Balance
============

Mass Balance defines empty mass, centre of gravity, inertia, and optional point
masses. JSBSim combines these values with tanks and buoyant gas during a run.

In the editor
-------------

Select **Mass Balance** to edit empty mass, CG, the six inertia terms, and point
masses. **Negate cross inertia** controls the sign convention for ``ixy``,
``ixz``, and ``iyz``. It is hidden while all three cross terms are zero.

Stored in
---------

PteroSim writes this section to ``Mass.xml``. Tanks and buoyant gas add their
mass during simulation.

Checks
------

Empty mass and principal inertia values must be positive. Point masses cannot
have negative mass. PteroSim rejects an invalid inertia tensor.
