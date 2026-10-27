Propulsion
==========

Propulsion defines the units that generate force in the JSBSim flight model.
Each unit is one engine and one thruster. The engine produces shaft power or
thrust, and the thruster converts that output into forces and moments.

.. image:: ../Images/editor_propulsion.png
   :alt: Propulsion component with the engine and thruster edit buttons highlighted
   :class: no-float-left

Use **+ Add** > **Motor** to add a propulsion unit. A new unit uses the first
available ``Motor_N`` label, the ``DJI_E305`` engine, the ``DJI_9450``
thruster, the structural origin, 90 degrees of pitch, and ``+1`` sense. These
are initial values, not values calculated from the aircraft.

The number in the component header and the number under :doc:`inputs` use
different bases. The first component is ``#1`` in Propulsion and ``Motor 0``
in Inputs. Component order is the JSBSim engine index. Removing a component
renumbers every component after it and therefore changes its corresponding
Motor number under Inputs.

A Propulsion component does not add mass or create a visible mesh. Include
installed propulsion mass under :doc:`mass_balance` and add visible parts
under :doc:`parts`.

The fields below use the c172p's engine as an example.

Fields
------

**Label**
   The case-sensitive name used by a propeller in :doc:`parts` to find the
   motor that spins it. Renaming a motor does not update that reference. If
   the names no longer match, the visual propeller is not shown. The label
   does not identify the engine inside JSBSim; the engine index does.

**Engine**
   Selects the engine definition by filename without ``.xml``. The list
   contains definitions stored with this aircraft and retains the currently
   selected name. It does not list the complete shared catalogue.

   The line below the selector reports the definition type, whether the file
   belongs to this aircraft or the read-only catalogue, and whether the
   engine outputs power or thrust. **+** creates a new definition and the
   pencil edits the selected one; see `Definitions`_.

**Thruster**
   Selects the thruster definition the same way. The list contains only
   thrusters that accept the selected engine's output: ``propeller`` and
   ``rotor`` accept shaft power, ``direct`` and ``nozzle`` accept thrust. The
   line below the selector reports the type, the file location, and whether
   the thruster fits the engine.

   **Apply to FDM** is refused if a selected engine or thruster name cannot be
   resolved to a definition file, or if an existing pair has mismatched
   output types.

**Location (m)**
   The point where JSBSim applies the thruster force. The three boxes are X,
   Y, and Z in the structural frame: X points aft, Y right, and Z up. The
   offset from the centre of gravity determines the moments produced by the
   force. A visual propeller linked to this motor also uses this point as its
   shaft position.

**Orient: roll/pitch/yaw (deg)**
   Rotates the thruster from the aircraft body axes. With all three values at
   zero, thrust points forward along body +X. Positive pitch rotates thrust
   upward; 90 degrees points it vertically upward. Positive yaw rotates thrust
   to the aircraft's right.

   Roll is rotation about the thrust axis. It does not change a propeller's
   force, torque, or gyroscopic-moment direction. The rotor model uses roll as
   part of its rotor orientation.

**Sense**
   Sets the direction of rotation and the sign of the reaction torque. Its
   convention depends on the thruster type:

   * For a propeller, ``+1`` is clockwise when viewed from the cockpit side,
     looking forward along the thrust axis. ``-1`` is the opposite direction.
     For an upward-pointing multirotor propeller, ``+1`` therefore appears
     counter-clockwise when viewed from above.
   * For a rotor viewed from above, ``+1`` is counter-clockwise and ``-1`` is
     clockwise. ``0`` represents a coaxial pair with no reaction torque.
   * Direct thrusters and nozzles do not read Sense; the control is disabled
     for those types.

**P-factor**
   Appears only for a propeller. It moves the effective thrust application
   point in proportion to the angle between the shaft and the incoming
   airflow. Angle of attack produces a yawing moment and sideslip a pitching
   moment; their direction depends on **Sense**. Zero disables the effect.

**Feeds from tank**
   Each checkbox selects a tank by its zero-based index under :doc:`tanks`.
   A fuel-burning engine draws only from the selected tanks. With no selected
   tank it receives no fuel and cannot start. Electric and brushless motors do
   not read fuel feeds and can run without a tank.

The red × removes the propulsion unit. Recheck the Motor destinations under
:doc:`inputs` after removal because all later engine indices change.

Definitions
-----------

An engine or thruster definition is an XML file in JSBSim's format. The
catalogue holds read-only definitions shared by all aircraft; an aircraft's
own definitions are stored in its ``Engines`` directory.

**+**
   Creates a definition in the aircraft's own ``Engines`` directory and
   selects it for this component. For an engine, the available types are
   those the editor can create without missing required tables or functions:
   ``turbine_engine`` and ``turboprop_engine`` are not among them, so copy one
   from the catalogue instead. For a thruster, the types are filtered by the
   selected engine's output.

**Pencil**
   Opens the selected definition. A definition already stored with the
   aircraft is edited in place. A read-only catalogue definition is copied
   into the aircraft first; the catalogue file is not modified.

   The pencil refuses a file that the form cannot save back unchanged, and
   the status line names the reason: an element written in a unit other than
   the one the form writes, an element or table written twice, a value that
   is not a number, or root attributes that differ from the form's. The
   c172p's own ``prop_75in2f`` is refused for the last reason: it has no
   ``version="1.1"``, which the form always writes and which reverses the
   sign of the propeller's gyroscopic moment.

The form follows the same rules for every type:

* **Type** selects the JSBSim model in a new definition and determines which
  fields are shown. In an existing definition it identifies the model already
  stored in the file.
* **Name** is both the definition's filename and the ``name`` attribute
  inside it. Saving also selects this name for the current Propulsion
  component.
* A field marked ``*`` is required and has no checkbox.
* For any other field, a selected checkbox writes the value to the file. A
  cleared checkbox omits the element and JSBSim uses its built-in default.
* A field with a **derive** checkbox works the other way round. Selected, it
  omits the element and JSBSim calculates the value from other fields;
  cleared, it writes the value in the box.
* An on/off field has a second checkbox after the first: the first writes
  the element, the second is its value.

Saving rewrites the definition and does not preserve XML comments. Elements
and tables the form has no field for are kept as written.

Engine definitions
------------------

The engine definition determines how a control input becomes shaft power or
thrust, and which starting procedure, fuel consumption, and engine state are
available to JSBSim. ``brushless_dc_motor``, ``electric_engine``,
``piston_engine``, and ``turboprop_engine`` produce shaft power.
``turbine_engine`` and ``rocket_engine`` produce thrust.

Brushless DC motor
^^^^^^^^^^^^^^^^^^

``brushless_dc_motor`` is the motor of most multirotors. The throttle sets
the voltage, the voltage and RPM set the current, and the current sets the
torque. There is no current limit. All four fields are required, and JSBSim
refuses to load the definition if one is missing.

**Max volts, V**
   Voltage at full throttle; the motor receives this value multiplied by the
   throttle. It scales thrust per throttle, so a wrong cell count looks like
   a wrong autopilot gain.

**Velocity constant, rpm/V**
   The motor's Kv: RPM per volt of back-EMF, and torque per ampere through
   its inverse. A value off by a factor of ten either starves thrust or
   overspeeds the propeller.

**Coil resistance, ohm**
   Winding resistance. It sets how steeply torque falls as RPM rises, and
   therefore how fast the motor responds to a throttle change.

**No-load current, A**
   Current needed to overcome the motor's internal friction. It produces no
   torque and mostly matters near idle. Zero is allowed.

Electric engine
^^^^^^^^^^^^^^^

``electric_engine`` delivers its power multiplied by the throttle, regardless
of RPM.

**Power, W**
   Shaft power at full throttle. Omitting it gives exactly one horsepower.

Piston engine
^^^^^^^^^^^^^

All ``piston_engine`` fields are optional; JSBSim does not refuse a piston
definition for a missing element.

.. image:: ../Images/editor_propulsion_engine_piston_1.png
   :alt: Upper half of the piston engine definition form
   :class: no-float-left

.. image:: ../Images/editor_propulsion_engine_piston_2.png
   :alt: Lower half of the piston engine definition form
   :class: no-float-left

Core
~~~~

**Max power, hp**
   Nominal power at **Max RPM**. JSBSim calculates **BSFC** from it when BSFC
   is derived, and **Starter torque** when that is derived. Otherwise it only
   scales the engine's reported percentage of power: with BSFC written, as in
   the example, power comes from fuel flow and BSFC, and changing Max power
   does not change it.

**Displacement, cu in**
   Total swept cylinder volume. It determines air mass flow and fuel flow, so
   it affects power production and engine cooling.

**Idle RPM**
   Reference idle speed used to shape the low-throttle response. The engine
   starts running after reaching 80 percent of this speed and stops if it
   falls below that threshold.

**Max RPM**
   Reference speed at which **Max power** is specified. JSBSim also uses it to
   calculate intake resistance, derived BSFC, and oil pressure.

**Cycles**
   Crankshaft revolutions per power cycle. JSBSim models only four-stroke
   engines: air and fuel flow always assume four strokes, and this value
   divides only the friction and pumping losses. Leave it at 4.

**Cylinders**
   Number of cylinders. It scales the total cylinder-head thermal mass used by
   the temperature model.

**Stroke, in**
   Piston travel from top to bottom dead centre. Together with RPM it sets
   mean piston speed, which reduces manifold pressure at high RPM.

**Compression ratio**
   Ratio of maximum to minimum cylinder volume. JSBSim lowers volumetric
   efficiency when manifold pressure is below ambient pressure, at part
   throttle, and raises it when boost puts manifold pressure above ambient;
   the compression ratio sets how strongly. The form takes values from 2.

**Volumetric eff.**
   Nominal ratio between the inducted air volume and the engine displacement.
   It directly affects air flow, fuel flow, and power; boosted engines may use
   a value greater than one.

Manifold & intake
~~~~~~~~~~~~~~~~~

**MAP at idle, inHg**
   Nominal sea-level manifold absolute pressure at idle without boost. With
   **Idle RPM**, it defines the low end of the throttle-to-manifold-pressure
   response.

**MAP max, inHg**
   Nominal sea-level manifold absolute pressure at maximum throttle without
   boost. JSBSim clamps the ordinary manifold path to 29.9 inHg, but the
   unclamped value still affects derived BSFC and can therefore represent a
   boosted power rating.

**MAP lag, s**
   Time constant of the manifold-pressure lag. A larger value makes manifold
   pressure, and with it power, follow a throttle movement more slowly.

**Peak piston speed, ft/s**
   Mean piston speed that sets the engine's intake impedance. Manifold
   pressure falls gradually as piston speed rises, with no threshold; a lower
   value makes it fall sooner.

**Ram air factor**
   Multiplier for the dynamic-pressure contribution to manifold pressure.
   Zero disables ram-air recovery; larger values increase manifold pressure
   with airspeed.

**Intake impedance**
   Pressure-loss factor of the intake upstream of the throttle. Increasing it
   reduces available manifold pressure. With **derive** selected, JSBSim
   calculates it from **Peak piston speed**, **Max RPM**, **Stroke**, and
   **MAP max**.

Fuel & friction
~~~~~~~~~~~~~~~

**BSFC, lb/hp.h**
   Brake-specific fuel consumption. JSBSim sets fuel flow from air flow and
   mixture, then divides it by BSFC to get power, so increasing BSFC lowers
   power at the same fuel flow. With **derive** selected, JSBSim calculates it
   from MAP, volumetric efficiency, friction, RPM, and **Max power**.

**Static friction, hp**
   Constant power required to turn an engine that is not producing power. It
   slows a windmilling engine and propeller and is subtracted from generated
   power.

**Dynamic FMEP, Pa**
   Speed-dependent friction mean effective pressure. JSBSim combines this
   coefficient with mean piston speed to calculate the part of internal
   friction that rises with RPM.

**Static FMEP, Pa**
   Constant friction mean effective pressure: the part of internal friction
   that does not scale with piston speed.

**Spark fail drop**
   Fraction of power lost when only one magneto is operating. Zero produces no
   loss; one removes all power during single-magneto operation.

**Max throttle**
   Upper end of the throttle range the JSBSim trimmer searches. The engine
   model does not clamp the live throttle to it.

**Min throttle**
   Lower end of the throttle range the JSBSim trimmer searches. The engine
   model does not clamp the live throttle to it either.

Starter
~~~~~~~

**Starter RPM**
   Maximum crankshaft speed reached by an unloaded starter. Propeller load and
   engine resistance reduce the actual cranking speed. With **derive**
   selected, JSBSim uses twice **Idle RPM**.

**Starter torque, lb.ft**
   Starter torque at zero RPM. Available torque decreases as the crankshaft
   approaches **Starter RPM**. With **derive** selected, JSBSim uses 0.4 times
   **Max power**.

Oil & cooling
~~~~~~~~~~~~~

**Oil relief valve, psi**
   Oil pressure at which the relief valve opens. Oil pressure rises with RPM
   up to this value; the viscosity correction is added after that limit, so
   oil colder than **Design oil temp** reads above it.

**Design oil temp, K**
   Oil temperature at which the viscosity correction to oil pressure is zero.
   Colder oil gives higher pressure, hotter oil lower. The editor writes the
   value without a unit attribute because JSBSim does not provide a
   conversion for this element.

**Oil press. RPM max**
   Engine speed at which the oil pump reaches the relief-valve pressure before
   viscosity correction. With **derive** selected, JSBSim uses three quarters
   of **Max RPM**.

**Oil viscosity index**
   How strongly oil pressure changes with the difference between the oil
   temperature and **Design oil temp**.

**Cyl. head mass, kg**
   Thermal mass of one cylinder head. JSBSim multiplies it by **Cylinders**;
   increasing it slows cylinder-head temperature changes.

**Cooling factor**
   Efficiency multiplier for the aircraft's engine-cooling airflow. Increasing
   it increases heat removal from the cylinder heads.

Supercharger
~~~~~~~~~~~~

**Boost speeds**
   Number of discrete supercharger ratios. Zero selects a naturally aspirated
   engine; one to three enables the corresponding boost stages. Checking this
   field makes the remaining supercharger fields available, while its value
   controls how many numbered stages JSBSim uses.

**Override**
   Enables the boost-regulator override when set to one. Without the override,
   manifold pressure is clipped to the rated wastegate limit.

**Manual**
   Selects manual boost-stage switching. When cleared, JSBSim changes stages
   automatically with altitude; when selected, the active stage follows the
   ``propulsion/engine[N]/boost-speed`` property, counted from zero.

**Take-off boost, psi**
   Boost above sea-level ambient pressure available while the throttle is
   above 0.98. JSBSim uses it only when it is greater than **Rated boost 1**.
   It changes the regulator target, not the supercharger ratio, so it adds
   power only below the rated altitude.

**Boost loss factor**
   Multiplier for the shaft power consumed while compressing intake air. Zero
   models boost without a power cost; a positive value subtracts compressor
   power from engine output.

**Rated boost 1/2/3, psi**
   Rated boost above sea-level ambient pressure for each enabled stage. Zero
   fails JSBSim's check of that stage; an engine with one stage then runs
   naturally aspirated.

**Rated power 1/2/3, hp**
   Rated power recorded for each boost stage. JSBSim checks that the value is
   nonzero when validating a stage but does not use it in the power
   calculation.

**Rated RPM 1/2/3**
   Engine speed at which the corresponding stage develops its rated boost.

**Rated altitude 1/2/3, ft**
   Highest altitude at which the corresponding stage can maintain rated
   boost. Above it, manifold pressure falls because the stage is already at
   its maximum unregulated pressure ratio. Zero leaves that stage
   unregulated.

Read, unused
~~~~~~~~~~~~

**Bore, in**
   Cylinder diameter. JSBSim reads and stores the value, but the piston-engine
   calculations do not use it.

Rocket engine
^^^^^^^^^^^^^

The form writes a liquid-propellant ``rocket_engine``. A solid motor is
defined by a thrust table, so copy one from the catalogue instead. Below
**Min throttle** the engine does not burn; above it, propellant flow is the
sea-level maximum multiplied by the throttle, and vacuum thrust is that flow
multiplied by **Specific impulse**.

**Specific impulse, s**
   Thrust per unit of propellant weight flow.

**SL fuel flow, lb/s**
   Fuel flow at full throttle. Without it the engine produces no thrust, so
   the form requires it.

**SL oxidiser flow, lb/s**
   Oxidiser flow at full throttle. Zero makes the engine a monopropellant.

**Min throttle**
   Throttle below which combustion stops. The trimmer also uses it as the
   lower end of its throttle range.

**Max throttle**
   Upper end of the throttle range the JSBSim trimmer searches.

Thruster definitions
--------------------

The thruster definition determines how engine output becomes force, reaction
torque, RPM, and gyroscopic effects.

Propeller
^^^^^^^^^

The ``propeller`` definition contains the propeller's dimensions, rotational
properties, governor limits, and the coefficient tables used to calculate its
thrust and shaft-power demand. The form below is the x500's propeller.

.. image:: ../Images/editor_propulsion_thruster_propeller.png
   :alt: Propeller definition fields of the x500 propeller
   :align: center

**Polar inertia, kg.m2**
   Propeller moment of inertia about its shaft. JSBSim uses it when integrating
   RPM from the difference between engine torque and aerodynamic load, and for
   the propeller's gyroscopic moment. A larger value makes RPM change more
   slowly. Values below ``1.36e-6`` kg.m2 are clamped when read.

**Diameter, in**
   Tip-to-tip propeller diameter. It directly scales both performance
   equations: thrust is proportional to diameter to the fourth power, while
   absorbed power is proportional to diameter to the fifth power. Values below
   ``0.012`` in are clamped when read.

**Constant speed**
   Turns the governor on. The governor moves the blade pitch between **Min
   blade pitch** and **Max blade pitch** to hold an RPM that the
   propeller-advance control selects between **Min RPM** and **Max RPM**. With
   the option off, the pitch follows the ``propulsion/engine[N]/blade-angle``
   property. A file that writes **Max RPM** without this element has the
   governor on, and the form shows it selected.

**Blades**
   Number of blades recorded in the XML file. JSBSim reads the value, but its
   propeller calculations do not use it.

**Gear ratio**
   Number of engine revolutions per propeller revolution. It converts engine
   RPM and torque to shaft RPM and torque. ``1`` is direct drive; JSBSim clamps
   values below ``0.001``.

**Min blade pitch, deg** and **Max blade pitch, deg**
   The blade-angle range available to the pitch command or the governor.
   Equal values define a fixed-pitch propeller. Different values make JSBSim
   look up both coefficient tables by advance ratio and blade angle, so the
   tables need a column for each blade angle; a table with only the ``J``
   column ignores the pitch, and the governor then changes nothing.

**Min RPM** and **Max RPM**
   The range of propeller RPM the governor can be commanded to hold.

**Reverse pitch, deg**
   Blade angle the governor moves toward when reverse thrust is commanded.

**Thrust scale**
   Multiplies every coefficient obtained from the **Thrust coefficient** table.
   It scales the complete thrust curve without changing each table row.

**Power scale**
   Multiplies every coefficient obtained from the **Power coefficient** table.
   It scales the complete shaft-power load curve without changing each table
   row.

Coefficient tables
~~~~~~~~~~~~~~~~~~

Both graphs plot a dimensionless coefficient against advance ratio ``J``. The
advance ratio is axial airspeed divided by propeller revolutions per second and
diameter: ``J = V / (n D)``. ``J = 0`` is the static condition. Increasing
``J`` means that the propeller advances farther through the air during each
revolution.

Each row below a graph is one lookup point. The left column is ``J`` and the
right column is the corresponding coefficient; a variable-pitch table has one
coefficient column per blade angle. JSBSim interpolates between the rows and
clamps lookups outside the table to the nearest endpoint instead of
extrapolating. The form requires the first row at ``J = 0``, increasing ``J``
values, and at least two rows. The row count in the heading is only the
number currently stored in that definition.

**Thrust coefficient**

.. image:: ../Images/editor_propulsion_thruster_ct.png
   :alt: Propeller thrust coefficient graph and table
   :align: center

The ``C_THRUST`` curve supplies thrust coefficient ``Ct`` for the current
advance ratio. JSBSim calculates thrust from ``Ct``, air density, propeller RPM,
and diameter. The graph therefore defines how thrust changes as forward speed
and RPM change. A positive value produces thrust in the propeller's forward
direction; a negative value represents aerodynamic braking. **Thrust scale**
is applied after the table lookup.

**Power coefficient**

.. image:: ../Images/editor_propulsion_thruster_cp.png
   :alt: Propeller power coefficient graph and table
   :align: center

The ``C_POWER`` curve supplies power coefficient ``Cp`` for the current advance
ratio. JSBSim calculates the shaft power absorbed by the propeller from ``Cp``,
air density, RPM, and diameter. This load is converted to torque and balanced
against engine output when RPM is updated. A larger ``Cp`` means a larger power
demand at the same density, RPM, and diameter. **Power scale** is applied after
the table lookup.

Rotor
^^^^^

The ``rotor`` definition models a helicopter rotor. Six fields are required. Eight more are derived: JSBSim estimates
them from the others unless a value is written.

**Diameter, ft**
   Rotor diameter.

**Blades**
   Number of blades. Unlike a propeller's, it is used: solidity, thrust, and
   torque all scale with it.

**Blade chord, ft**
   Blade chord, which sets solidity together with **Blades** and
   **Diameter**.

**Gear ratio**
   Engine RPM divided by rotor RPM.

**Nominal RPM**
   Design rotor speed. JSBSim derives **Max RPM** and the inflow-lag estimate
   from it and scales ground effect by the ratio of actual to nominal RPM.
   Values below 2 are clamped.

**Inflow lag, s**
   Time constant with which the induced inflow follows a change in thrust.
   Values are clamped to 1e-6 to 2 seconds.

**Lift-curve slope, 1/rad**
   Blade section lift-curve slope.

**Blade twist, rad**
   Twist from root to tip; negative means the tip is at a lower angle.

**Tip loss factor**
   Fraction of the blade that produces lift. 1 models no tip loss.

**Min RPM**
   Lowest rotor RPM. JSBSim keeps the rotor RPM between **Min RPM** and
   **Max RPM**, and clamps Min RPM to at most **Nominal RPM** minus one.

**Max RPM**
   Highest rotor RPM. Derived as twice **Nominal RPM**.

**Hinge offset, ft**
   Distance of the flapping hinge from the hub. Derived as five percent of the
   radius.

**Flapping moment, slug.ft2**
   Moment of inertia of one blade about its flapping hinge. Derived from the
   chord and radius.

**Blade mass moment, slug.ft**
   First mass moment of one blade about the hinge. Derived from the flapping
   moment.

**Polar moment, slug.ft2**
   Moment of inertia of the whole rotor about its shaft, which sets how fast
   rotor RPM changes. Derived as 1.1 times the flapping moment times the
   number of blades.

**Max brake power, hp**
   Power the rotor brake absorbs at full ``propulsion/engine[N]/brake-ctrl-norm``.
   Derived from the rotor's size.

**Ground effect exponent**
   How quickly ground effect fades with height above ground. Zero switches
   ground effect off.

**Ground effect shift, ft**
   Height added to the height above ground before ground effect is
   calculated.

Nozzle and direct
^^^^^^^^^^^^^^^^^

A ``nozzle`` has one required field, **Exit area, sq ft**. JSBSim subtracts
ambient pressure times the exit area from the engine's vacuum thrust, so
thrust falls at low altitude.

A ``direct`` thruster has no fields of its own: it applies the engine's
thrust at the component's **Location** along its **Orient** direction.
