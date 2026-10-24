Parts
=====

Parts describes the meshes that make up a vehicle and the pieces that move
during simulation. Visual parts do not add mass or aerodynamic forces by
themselves.

Part kinds
----------

* **Fixture** is a fixed mesh.
* **Propeller** spins with a motor from :doc:`propulsion`.
* **Surface** follows a reported control-surface position.
* **Nacelle** rotates a motor and any parts that ride it.

In the editor
-------------

Drop a ``.glb`` file onto the Parts section to copy it into the vehicle's
``meshes`` directory and create a part. Select its kind, position, rotation,
and optional parent. Moving parts also expose their axis, hinge, travel, and
driver. Use **Gizmo holds** to move either a mesh or its hinge in the viewport.

Stored in
---------

Visual parts are stored in ``Visual.xml``. Mesh paths are relative to the
vehicle directory.

Checks
------

Meshes must be readable ``.glb`` files in the vehicle directory. Parent,
motor, and source names must resolve. Moving parts need a non-zero axis.
