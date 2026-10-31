External Forces
===============

External forces are forces or moments applied from outside the flight-dynamics
model. They are stored in the JSBSim ``external_reactions`` section and can
represent a tow, tether, tug, or an externally calculated thruster force. Each
reaction acts on the vehicle as one rigid body. It is not attached to a visual
part.

Each external force appears as a separate row in the vehicle tree. Selecting
one opens a section containing every external force and moment on that vehicle.
They are written together as one ``external_reactions`` list.

Due to a current editor limitation, this section may not appear even when the
vehicle already contains external reactions. This affects ZLT-NT and orca.

Manage external forces
----------------------

**+ Add external force** creates a force named ``external_<N>``. The remove
button on a force deletes it. Anything that still writes to the removed
force's properties then writes to an unused property.

Fields
------

**Called**
   Name used by JSBSim to identify the reaction and construct its properties.
   It must be non-empty and unique. Two reactions with the same name use the
   same magnitude property.

   A force publishes its magnitude as
   ``external_reactions/<name>/magnitude`` in pounds-force, its direction as
   ``/x``, ``/y``, and ``/z``, and its location as ``/location-x-in``,
   ``/location-y-in``, and ``/location-z-in``. A moment uses
   ``external_reactions/<name>/magnitude-lbsft`` in pound-feet and publishes
   its direction as ``/l``, ``/m``, and ``/n``. The editor does not convert
   these runtime JSBSim properties to SI units.

**A moment, not a force**
   Switches the reaction from a force to a moment. A force changes linear and
   angular motion according to its point of application. A moment directly
   changes angular motion. JSBSim does not read a location for a moment, so
   **Where, m** has no effect while this option is enabled.

**Given in**
   Coordinate frame used for **Which way**:

   * **BODY** rotates with the vehicle. Its axes are X forward, Y right, and Z
     down.
   * **LOCAL** is the local horizontal NED frame: north, east, and down.
   * **WIND** follows the current aerodynamic wind axes.
   * **INERTIAL** uses the inertial frame.

   The direction frame is independent of the structural frame used by
   **Where, m**. In particular, BODY direction uses Z down while structural
   location uses Z up.

**Where, m**
   Point where a force acts, in metres in the JSBSim structural frame: X aft,
   Y right, and Z up. It is measured from the structural origin, not from the
   current centre of mass. The offset between this point and the centre of
   mass determines the moment produced by the force. See **Coordinate
   systems** in :doc:`Build Your Own Vehicle <index>`.

**Which way**
   Direction vector in the frame selected by **Given in**. Only the ratio
   between its components matters when the model is loaded because JSBSim
   normalizes the vector once at that time. If a script changes the force's
   ``/x``, ``/y``, or ``/z`` properties during a run, JSBSim does not normalize
   the new vector; its length then also scales the applied force.

Set the magnitude
-----------------

The External Forces section has no magnitude field. A force or moment must get
its magnitude through one of these methods:

* Add a binding in :doc:`Inputs <inputs>` and select the magnitude property as
  its destination. The selected autopilot channel, or an SDK control supplied
  through ``set_controls``, then drives the property. The SDK cannot write an
  arbitrary JSBSim property directly; ``aircraft.properties([...])`` only
  reads properties.
* Publish the magnitude property from a block in :doc:`Logic Graphs
  <logic_graphs>`.
* Put a ``function`` inside the force or moment in the aircraft XML. The
  editor preserves this function but does not display or edit it. When a
  function supplies the magnitude, JSBSim does not create the corresponding
  magnitude property, so an input binding or logic-graph block aimed at that
  property has no effect.

Orca NOTAR force
----------------

Orca uses the external force ``notar_jet`` for its direct-jet anti-torque
thruster. The force is defined in BODY axes, points along positive Y, and acts
at the end of the tail boom. Its embedded function reads
``fcs/notar/jet-force-lbs``; the External Forces panel preserves that function
without showing it.
