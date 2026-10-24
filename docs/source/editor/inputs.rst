Inputs
======

Inputs maps channels received from Manual control, PX4, ArduPilot, or
BetaFlight to motors, control surfaces, servos, gimbals, and the gripper.

In the editor
-------------

Select **Inputs** in the aircraft tree. Choose the flight stack and manual
pilot, then add one binding for every channel the selected controller sends.
A binding selects a channel number, target type, target index, input range,
output range, and optional inversion.

Motor order is owned by this page: ``index='0'`` means the first motor in the
aircraft tree and in ``Propulsion.xml``. Autopilots may number the same physical
motors differently, so use separate bindings with ``stack`` when required.

Stored in
---------

Bindings are stored in ``Controls.xml``. A binding without a flight stack
applies to every stack.

Checks
------

Channel numbers and input and output ranges must be valid. Target indices must
refer to existing components.
