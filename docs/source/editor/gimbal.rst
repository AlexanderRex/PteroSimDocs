Gimbal
======

A gimbal is an articulated mount for a camera, sensor, gripper, or visual mesh.
It exposes yaw, roll, and pitch stages that can be aimed by MAVLink or the
Python API.

In the editor
-------------

Add a mount with **+ Add > Gimbal**. Select it to edit its unique name, pose,
parent gimbal, control source, rate limits, and response time. Fixtures may
ride the complete mount or an individual ``.yaw``, ``.roll``, or ``.pitch``
stage. Sensors ride the mount head.

Stored in
---------

Gimbals are stored in ``Visual.xml`` before components that refer to them.

Checks
------

Names must be unique and cannot contain a stage suffix. A parent must name
another gimbal, and parent chains cannot form a cycle. Rates and ``tau`` cannot
be negative.
