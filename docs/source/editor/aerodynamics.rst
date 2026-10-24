Aerodynamics
============

Aerodynamics defines the forces and moments produced by airflow. PteroSim
edits the JSBSim function trees that calculate lift, drag, side force, roll,
pitch, and yaw.

In the editor
-------------

Select **Aerodynamics** to declare local properties and edit coefficient
functions. A function can use values, properties, sums, products, differences,
tables, and the other operations offered by the formula editor. Assign each
force-producing function to its axis.

Stored in
---------

PteroSim writes this section to ``Aero.xml``. Its formulas use the reference
geometry from :doc:`metrics` and may read properties from :doc:`logic_graphs`.

Checks
------

Function names must be unique. Operators need all required operands, tables
must form valid grids, and referenced properties must exist when the model
loads.
