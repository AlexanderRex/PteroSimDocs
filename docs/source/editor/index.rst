Build Your Own Vehicle
======================

A PteroSim vehicle is a directory under ``PteroSimAircrafts``. The directory
and its JSBSim manifest must have the same name: ``<Name>/<Name>.xml``.

Create a vehicle
----------------

With the simulation stopped, open **Scene**, select **+ Add**, then select
**New vehicle**. PteroSim creates a vehicle with the minimum required sections
and opens it in the vehicle editor. You can also copy an existing vehicle
directory. Rename the directory, manifest, and ``fdm_config`` name.

Select a vehicle in the scene and open it to see its components. Selecting a
component opens the matching editor section. Changes are available only while
the simulation is stopped.

Apply changes
-------------

**Apply to FDM** writes the changes and reloads the flight-dynamics model. If
validation fails, PteroSim reports the problem and does not reload the model.

Coordinate systems
------------------

JSBSim structural locations use metres with X positive aft, Y positive right,
and Z positive up. The **Metrics**, **Mass Balance**, **Gear**, **Propulsion**,
**Tanks**, **External Forces**, and **Buoyancy** sections use this frame.

``Visual.xml`` and ``Sensors.xml`` use a vehicle frame with X forward, Y right,
and Z up. Orientations are roll, pitch, and yaw in degrees. A part attached to
a gimbal or nacelle uses its parent's frame instead of the airframe.

Spawn attitude
--------------

A vehicle is level when its manifest has no ``spawn`` element. Use its
``pitch`` attribute for a vehicle that must spawn at another attitude.

Check a vehicle
---------------

Check the pose, contact points, propellers, and control surfaces while stopped.
Then test manual flight before connecting an autopilot.

Components
----------

.. toctree::
   :maxdepth: 1

   metrics
   mass_balance
   aerodynamics
   gear
   propulsion
   tanks
   battery
   external_forces
   buoyancy
   inputs
   logic_graphs
   parts
   chase_camera
   gimbal
   gripper
   collision
   sensors
