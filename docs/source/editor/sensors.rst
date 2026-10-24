Sensors
=======

Sensors provide simulated measurements to autopilots and to the Python API.
Each sensor has a unique name, type, pose, update rate, enable state, and
optional noise and logging settings.

Available types are IMU, GPS, barometer, airspeed, temperature, camera, and
depth camera.

In the editor
-------------

Open a vehicle and select **+ Add**, then choose a type under **Sensors**.
Select the new sensor to set its name, position, orientation, update rate, and
type-specific fields. A camera can ride a gimbal; physical sensors whose mount
is sampled only at setup must remain on the airframe.

Stored in
---------

Sensors are stored in ``Sensors.xml``.

Checks
------

Names must be unique. Types, numeric ranges, and parent gimbals must be valid.
Camera and depth-camera settings must also have valid image and stream values.
