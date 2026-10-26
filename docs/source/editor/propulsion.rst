Propulsion
==========

Propulsion defines the units that generate force in the JSBSim flight model.
Each component combines one engine with the thruster it drives. The engine
produces power or thrust; the thruster turns that output into forces and
moments at the specified position and orientation.

An aircraft can have multiple Propulsion components. Their order is their
engine index: **Motor 0** under :doc:`inputs` controls the first component,
**Motor 1** controls the second, and so on. Removing a component renumbers all
components after it.

Propulsion does not add engine mass or create a visible propeller. Include the
engine mass under :doc:`mass_balance`, and add its mesh under :doc:`parts`.

.. image:: ../Images/editor_propulsion.png
   :alt: Propulsion component in the vehicle editor
   :class: no-float-left

Fields
------

**Label**
   The name shown in the component list. A propeller under :doc:`parts` also
   uses this label to identify the motor that spins it; a nacelle carrying that
   propeller then follows the same engine. JSBSim identifies the engine by its
   position in the Propulsion list, not by this label.

**Engine**
   Selects the engine definition. This file contains the engine type and its
   performance parameters. Depending on the type, the engine supplies either
   shaft power to a propeller or rotor, or thrust to a direct thruster or
   nozzle.

   The text below the selector shows the engine type, whether the definition
   belongs to this vehicle or the read-only catalogue, and whether it produces
   power or thrust.

**Thruster**
   Selects the definition that converts the engine output into forces and
   moments. Propellers and rotors accept power; direct thrusters and nozzles
   accept thrust. After an engine is selected, the editor limits this list to
   compatible definitions and refuses to apply a mismatched pair.

Use **+** beside either selector to create a definition for this vehicle. Use
the pencil button to edit an existing vehicle definition. Editing a catalogue
definition first copies it into the vehicle, leaving the catalogue file
unchanged.

Placement
---------

**Location (m)**
   The point where the thruster applies its force. The three boxes are X, Y,
   and Z in the structural frame: X points aft, Y right, and Z up. Moving a
   thruster away from the centre of gravity changes the roll, pitch, and yaw
   moments produced by its force.

   A visual propeller linked to this component also uses this point as its
   shaft position.

**Orient: roll/pitch/yaw (deg)**
   Rotates the thruster relative to the aircraft body axes. The three boxes
   are roll, pitch, and yaw in degrees. With all three at zero, thrust points
   along the aircraft's forward X axis. A pitch of 90 degrees points the
   thruster upward, as required by a conventional multirotor.

Rotation and fuel
-----------------

**Sense**
   Sets the thruster's direction and the sign of its reaction torque. Its
   meaning depends on the selected thruster type:

   * For a propeller, ``+1`` is clockwise and ``-1`` is counter-clockwise in
     the JSBSim convention.
   * For a rotor viewed from above, ``+1`` is counter-clockwise and ``-1`` is
     clockwise. ``0`` represents a coaxial pair with no reaction torque.
   * Direct thrusters and nozzles do not use this field.

**P-factor**
   Appears only for a propeller. It controls the asymmetric-thrust effect that
   pulls the aircraft's nose sideways. Zero disables the effect.

**Feeds from tank**
   Selects the fuel tanks available to this engine by their index in
   :doc:`tanks`. A fuel-burning engine can draw only from the selected tanks.
   This setting is not used by electric and brushless motors.

The red × in the component header removes that propulsion unit. Check the
motor assignments under :doc:`inputs` after removing a unit because every
later engine index changes.
