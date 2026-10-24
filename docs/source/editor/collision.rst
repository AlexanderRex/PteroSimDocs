Collision
=========

Collision is the generated physical shape used for contacts with terrain,
objects, other aircraft, and propellers.

In the editor
-------------

Select **Collision** to see a summary of the generated shape. Enable
**Draw this part** together with the outliner's **Show debug draw** to inspect
the hulls in the viewport. The shape is built when the simulation starts, so
stop and start again after changing visual geometry.

Stored in
---------

PteroSim derives collision from meshes and propeller geometry in
``Visual.xml``. There is no collision file to edit.

Checks
------

Meshes must contain usable three-dimensional geometry. Propeller parts must
refer to a valid motor and thruster.
