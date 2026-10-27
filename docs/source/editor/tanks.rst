Tanks
=====

Tanks store the fuel or oxidizer consumed by propulsion. Their mass and
position are included in the loaded aircraft's mass, centre of gravity, and
inertia, so these properties change as a tank drains.

A vehicle can have any number of tanks. They are numbered from zero in their
order in the aircraft file. An engine's **Feeds from tank** checkboxes refer to
these numbers.

Use **+ Add** |rarr| **Tank** to add another tank. A new tank is created as an
empty fuel tank with 1 kg capacity. The fields below are shown for **Tank 0**;
every additional tank has the same fields.

.. image:: ../Images/editor_tanks.png
   :alt: Tank 0 fields in the vehicle editor
   :class: no-float-left

**Holds**
   Selects what the tank contains. Clear **oxidiser, not fuel** for a fuel
   tank; select it for an oxidizer tank. Piston, turbine, and turboprop engines
   consume fuel tanks. Rocket engines handle their fuel and oxidizer feeds
   separately. JSBSim accepts only these two tank types.

**Where, m**
   Position of the tank contents in the structural frame. The three boxes are
   X, Y, and Z: X points aft, Y right, and Z up. JSBSim uses this position when
   combining the tank contents with the empty aircraft and other masses. A
   tank away from the aircraft's centre of gravity therefore moves the loaded
   centre of gravity and contributes to the aircraft's inertia.

**Holds, kg**
   Maximum mass the tank can contain. The value must be greater than zero and
   must not be lower than **Has now**. Capacity is not itself added to aircraft
   mass; the tank structure must already be included in **Empty mass** under
   :doc:`mass_balance`.

**Has now, kg**
   Mass of contents at the start of a simulation. It is the initial condition,
   not a live display of the amount remaining while the simulation runs.
   JSBSim begins draining from this value and resets the tank to it when the
   flight model is restarted. The value cannot exceed **Holds**.

**Radius, m**
   Equivalent radius used to calculate the contents' own moment of inertia.
   For a liquid tank, JSBSim treats the contents as a shrinking spherical mass,
   so this contribution falls as the tank drains. Zero means that the file
   supplies no tank shape and no local contents inertia is calculated. Radius
   does not change the tank's capacity.

**Feeding order**
   Controls which tanks an engine drains first. Priority ``1`` is highest;
   ``2`` is used after all usable fuel of priority ``1`` is exhausted, followed
   by larger numbers. If several tanks connected to the same engine have the
   same active priority, the engine divides its demand equally between them.
   Fuel and oxidizer priorities are evaluated separately.

   ``0`` means that no explicit priority is written. JSBSim then uses its
   default priority when the aircraft is loaded. A tank must also be selected
   under the engine's **Feeds from tank** field before that engine can use it.

**Fuel**
   Optional JSBSim name for the liquid, such as ``JET-A``, ``AVGAS``, or
   ``JP-5``. A recognized name selects JSBSim's built-in density for that fuel
   and overrides **Density** below. Leave it empty when the density is supplied
   directly. Names are case-sensitive; an unknown name logs an error and falls
   back to JSBSim's default density.

**Density, lb/gal**
   Density used to convert between the tank's mass and volume. It is also used
   for volume-based tank data retained from the aircraft file. The editor's
   **Holds** and **Has now** values are masses, so changing density does not
   recalculate either field. Zero omits the density from the file; JSBSim then
   uses its default unless **Fuel** selects a built-in value.

The red |times| in a tank header removes that tank. Tank numbers after it move
down by one. PteroSim removes the deleted number from every engine feed and
updates higher feed numbers to keep them attached to the same remaining tanks.

.. |rarr| unicode:: U+2192
.. |times| unicode:: U+00D7
