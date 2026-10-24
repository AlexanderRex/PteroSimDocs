Chase Camera
============

The chase camera is the view used when the player possesses the vehicle. It is
separate from camera sensors and does not produce sensor frames.

In the editor
-------------

Select **Chase camera** to set its mount, direction, and arm length. The camera
looks back along the arm toward the vehicle. Use pitch to place more ground or
sky in the piloting view.

Stored in
---------

The chase camera is stored in ``Visual.xml``. It is only a player view; camera
sensor output is configured under :doc:`sensors`.

Checks
------

Arm length must be above zero. PteroSim rejects a second ``<chase>`` entry.
