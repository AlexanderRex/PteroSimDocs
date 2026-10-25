Build Your Own Vehicle
======================

A PteroSim vehicle is a directory under ``PteroSimAircrafts``. The directory
and its JSBSim manifest must have the same name: ``<Name>/<Name>.xml``.

Open the vehicle editor
-----------------------

With the simulation stopped, select a vehicle in **Scene**. Its components
appear in the aircraft tree. Select a component to open its editor section.

Apply changes
-------------

**Apply to FDM** writes the changes and reloads the flight-dynamics model. If
validation fails, PteroSim reports the problem and does not reload the model.

Coordinate systems
------------------

Locations use metres, with Y right and Z up. X points aft in the **Metrics**,
**Mass Balance**, **Gear**, **Propulsion**, **Tanks**, **External Forces**, and
**Buoyancy** sections, but forward in ``Visual.xml`` and ``Sensors.xml``.
Orientations in those files are roll, pitch, and yaw in degrees. A component
attached to a gimbal or nacelle uses its parent's frame.

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
