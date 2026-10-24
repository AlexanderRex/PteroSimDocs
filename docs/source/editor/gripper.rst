Gripper
=======

The gripper attaches and releases payload actors within a configured reach.
It is controlled by a Gripper actuator channel or by the Python API.

In the editor
-------------

Add the vehicle's gripper with **+ Add > Gripper**. Set its name, pose, reach,
and optional parent gimbal. Debug drawing shows the reach and current state.

Stored in
---------

The gripper is stored in ``Visual.xml``. It may attach to the airframe or a
gimbal, and :doc:`inputs` maps its actuator channel.

Checks
------

The name must be unique, reach must be positive, and the parent gimbal must
exist. A vehicle can have only one gripper.
