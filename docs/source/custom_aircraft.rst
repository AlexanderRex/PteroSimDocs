Add your own aircraft
=====================

The aircraft PteroSim flies are not compiled into it. Each one is a folder of plain
XML and glTF meshes that ships loose in the release, so you can open one and put your
own beside it.

The same folders are a public repository,
`PteroSimAircrafts <https://github.com/PteroLabsAI/PteroSimAircrafts>`_. Use them as
worked examples: every aircraft named on this page exists there in full.

You can do this on any license tier, Free included.

Where the aircraft live
-----------------------

``PteroSimAircrafts/`` sits next to ``Binaries`` and ``Content`` in an extracted
release, one folder per aircraft:

.. code-block:: text

   PteroSim-vX.Y.Z-Windows/
   └── PteroSim/
       ├── Binaries/
       ├── Content/
       ├── Plugins/
       └── PteroSimAircrafts/
           ├── F450/
           ├── x500/
           ├── standard_vtol/
           └── MyDrone/      <- yours

A folder becomes an aircraft once it holds the manifest JSBSim would load,
``MyDrone/MyDrone.xml``. The file name must match the folder name. A folder without
that manifest is ignored, so a working directory left in there places nothing.

The folder name is what the spawn panel lists and what the Python API takes:

.. code-block:: python

   sim.spawn("MyDrone", lat=47.397, lon=8.545, alt=5)

Start from an example
---------------------

Copy the aircraft closest to yours and rename both the folder and the manifest inside it:

.. code-block:: bash

   cd PteroSimAircrafts
   cp -r F450 MyDrone
   mv MyDrone/F450.xml MyDrone/MyDrone.xml

``F450`` is the smallest complete multirotor to start from. For a fixed wing start from
``advanced_plane``, and for a VTOL from ``standard_vtol``.

Restart PteroSim. ``MyDrone`` now appears in the spawn panel next to the stock aircraft
and flies exactly like the one you copied. The rest of this page is editing it.

What is in the folder
---------------------

.. list-table::
   :header-rows: 1
   :widths: 28 12 60

   * - File
     - Required
     - What it holds
   * - ``<Name>.xml``
     - Yes
     - The JSBSim manifest. Lists the files below and holds no numbers of its own.
   * - ``Metrics.xml``
     - Via manifest
     - Wing area, span, chord, and the reference points moments are taken about.
   * - ``Mass.xml``
     - Via manifest
     - Empty weight, centre of gravity, inertia tensor.
   * - ``Aero.xml``
     - Via manifest
     - Aerodynamic coefficients. A multirotor needs little more than drag.
   * - ``Propulsion.xml``
     - Via manifest
     - Each motor: where it sits, which way its thrust points, which way it spins.
   * - ``Engines/``
     - With propulsion
     - The motor and propeller definitions ``Propulsion.xml`` names.
   * - ``Gear.xml``
     - Via manifest
     - Landing gear and ground contact points.
   * - ``Visual.xml``
     - No
     - The meshes, and which of them spin or deflect.
   * - ``meshes/``
     - With Visual
     - glTF (``.glb``) meshes.
   * - ``Controls.xml``
     - No
     - Which autopilot channel drives which motor or surface.
   * - ``Sensors.xml``
     - No
     - IMU, GPS, barometer, airspeed, temperature, camera.
   * - ``Airframe.xml``
     - No
     - How the airframe rests on the ground and how its sensors are turned.
   * - ``firmwares/``
     - No
     - PX4 airframe script, ArduPilot parameter file.

The four files marked *No* are sidecars: PteroSim reads them and JSBSim does not.
Leaving one out is not an error. You get the empty state that every new aircraft starts
in, with no meshes or no sensors, and the aircraft still loads.

The flight model
----------------

The manifest and the files it names are ordinary JSBSim. An aircraft written for JSBSim
drops in as it is, and the `JSBSim Reference Manual
<https://jsbsim-team.github.io/jsbsim-reference-manual/>`_ is the authority on every tag
in them.

.. code-block:: xml

   <?xml version="1.0"?>
   <fdm_config name="MyDrone" version="2.0" release="ALPHA">
     <metrics          file="Metrics.xml"/>
     <mass_balance     file="Mass.xml"/>
     <aerodynamics     file="Aero.xml"/>
     <ground_reactions file="Gear.xml"/>
     <propulsion       file="Propulsion.xml"/>
     <fileheader/>
   </fdm_config>

JSBSim works in its structural frame: X aft, Y right, Z up, and the origin wherever you
choose, as long as every location in every file uses the same one. The F450 puts the
origin at the centre of gravity, which keeps its numbers symmetric.

Mass
~~~~

``Mass.xml`` is the shortest file that changes how the aircraft flies. Weigh the
airframe, put the CG where the mass balances, and give the three principal inertias:

.. code-block:: xml

   <mass_balance>
     <emptywt unit="KG"> 1.4 </emptywt>
     <location name="CG" unit="M">
       <x> 0 </x> <y> 0 </y> <z> 0 </z>
     </location>
     <ixx unit="KG*M2"> 0.019  </ixx>
     <iyy unit="KG*M2"> 0.019  </iyy>
     <izz unit="KG*M2"> 0.0252 </izz>
     <ixy unit="KG*M2"> 0 </ixy>
     <ixz unit="KG*M2"> 0 </ixz>
     <iyz unit="KG*M2"> 0 </iyz>
   </mass_balance>

Inertia is what the rate controller feels. Guess it low and the aircraft twitches; guess
it high and it wallows. For a quadrotor, summing ``mass × radius²`` over the motors and
the battery gets close enough to fly on.

Propulsion
~~~~~~~~~~

Each ``<engine>`` places one motor. ``<location>`` is its position in the structural
frame, ``<orient>`` turns its thrust axis, and ``<sense>`` is which way the propeller
turns, ``1`` one way and ``-1`` the other.

.. code-block:: xml

   <propulsion>
     <engine file="DJI_E305" name="front right">
       <thruster file="DJI_9450">
         <location unit="M">
           <x> -0.1651 </x> <y> 0.1651 </y> <z> 0.025 </z>
         </location>
         <orient unit="DEG">
           <roll> 0 </roll> <pitch> 90 </pitch> <yaw> 0 </yaw>
         </orient>
         <sense> 1 </sense>
       </thruster>
     </engine>
     <!-- ... one <engine> per motor ... -->
   </propulsion>

``pitch=90`` points a thrust axis straight up, which is where a multirotor rotor pushes.
The ``file`` attributes name ``Engines/DJI_E305.xml`` and ``Engines/DJI_9450.xml``.

.. note::

   Engine and propeller definitions must live in the ``Engines/`` subfolder. JSBSim
   searches there and in the shared catalogue, and it does **not** resolve a definition
   left loose in the aircraft folder.

Two things here are read outside this file. The order the engines are listed in is the
index ``Controls.xml`` counts with, and the geometry together with ``<sense>`` is what a
PX4 airframe or ArduPilot parameter file has to be told to match.

What it looks like
------------------

``Visual.xml`` attaches meshes. Meters and degrees, X forward, Y right, Z up, which is
the aircraft's own frame rather than JSBSim's structural one.

.. code-block:: xml

   <visual>
     <fixture file="meshes/body.glb" xyz="0 0 0" rpy="0 0 -90"/>

     <propeller file="meshes/prop.glb" xyz="0 0 0.0138" rpy="90 0 0"
                motor="front right" axis="0 0 1"/>
   </visual>

``fixture``
    A part that is seen and does not move, the airframe among them.

``propeller``
    A blade that turns with its motor. ``motor`` is the engine's ``name`` from
    ``Propulsion.xml``. ``axis`` is what it turns about, and the sign is the direction.

``surface``
    A control surface that deflects.

A propeller's hub is already the motor's position, so ``xyz`` on it is only the mesh's
offset from that hub. A mesh may be drawn facing any way. Turn it with ``rpy`` here
rather than editing the mesh.

Flying it from an autopilot
---------------------------

``Controls.xml`` says which channel from the autopilot drives what:

.. code-block:: xml

   <control_bindings stack="PX4">
     <binding stack="ArduPilot PX4" channel="0" type="Motor" index="0" label="front right"/>
     <binding stack="ArduPilot PX4" channel="1" type="Motor" index="1" label="aft left"/>
     <binding stack="ArduPilot PX4" channel="2" type="Motor" index="2" label="front left"/>
     <binding stack="ArduPilot PX4" channel="3" type="Motor" index="3" label="aft right"/>
   </control_bindings>

``index`` counts from zero in the order ``Propulsion.xml`` lists the engines. ``type`` is
what the channel drives: ``Motor``, ``Elevator``, ``Aileron``, ``Rudder``, ``Flaps``,
``Gripper`` or ``Servo``. A binding may name several stacks, and naming none means all of
them. Autopilots do not number motors alike, so give a stack that counts differently its
own rows.

The autopilot also has to be told the geometry it is flying, and ``firmwares/`` holds
that side: a PX4 airframe script (``px4_<name>``) or an ArduPilot parameter file
(``ardupilot_<name>.param``). The stock aircraft ship theirs, and they are the shortest
way to see which parameters matter. For PX4, the ``CA_ROTOR*`` block has to carry the
same positions and spin directions as ``Propulsion.xml``.

Sensors
-------

``Sensors.xml`` lists what the aircraft measures itself with:

.. code-block:: xml

   <sensors>
     <sensor type="imu"         name="imu"/>
     <sensor type="gps"         name="gps"/>
     <sensor type="barometer"   name="barometer"/>
     <sensor type="airspeed"    name="airspeed"/>
     <sensor type="temperature" name="temperature"/>
     <sensor type="camera"      name="camera"/>
   </sensors>

An autopilot expects an IMU, a GPS and a barometer, and a fixed wing wants an airspeed
sensor too. Cameras are what the :doc:`python_api` reads frames from.

Testing it
----------

1. Spawn it from the panel while the simulation is stopped, the way
   :doc:`first_steps` describes, and check that it appears and sits on its gear.
2. Press **Start** and take off on manual control. This catches mass, inertia and
   propulsion before an autopilot is in the way.
3. Connect PX4 or ArduPilot (:doc:`sitl_simulation_px4`,
   :doc:`sitl_simulation_ardupilot`) and hover. An aircraft that drifts in one axis
   usually has a motor order or a spin direction disagreeing between
   ``Propulsion.xml``, ``Controls.xml`` and the autopilot's own parameters.

Edit a file, then spawn the aircraft again and JSBSim reads the new definition. Restart
PteroSim if you added or renamed a folder.
