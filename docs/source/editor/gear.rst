Gear
====

Gear defines the points where the aircraft touches the ground. Each contact has
its own position, suspension, and friction. Wheel contacts can also steer,
brake, retract, or caster.

Each contact is a separate Gear component. A tricycle aircraft normally has
nose, left-main, and right-main wheels; additional contacts can represent
skids, a tail bumper, or wingtip protection.

**+ Add** → **Gear contact** in the aircraft tree adds a **Bogey** contact
named ``Contact_1`` (the first free number) at the structural origin, with the
spring and damping of a small quadcopter. Set its **Location**, **Spring**, and
**Damping** before you apply.

The fields below use the **NOSE** contact as an example.

.. image:: ../Images/editor_gear_nose.png
   :alt: Nose-wheel Gear component in the vehicle editor
   :class: no-float-left

Contact
-------

**Name**
   A descriptive name shown in the aircraft tree, the contact header, and
   logs. It does not control steering or braking. The example contact is
   named ``NOSE``.

**Type**
   Selects how JSBSim treats the contact:

   * **Bogey** represents a wheel. It provides the wheel-specific fields for
     orientation, rolling friction, steering, brakes, retraction, and
     castering.
   * **Structure** represents a contact that does not roll, such as a skid or
     bumper. It still uses the location, friction, spring, and damping
     fields, but hides the wheel-specific fields.

**Location (m)**
   The point that touches the ground while the strut is fully extended: for a
   wheel, the bottom of the tyre. It is in the structural frame, and the three
   boxes are X, Y, and Z: X points aft, Y right, and Z up. The example nose
   wheel is 0.17272 m ahead of the structural origin, on the centreline, and
   0.4953 m below it.

   .. image:: ../Images/gear_location_orientation.svg
      :alt: Nose wheel Location measured from the structural origin, its strut axis, and the sense of positive pitch
      :class: no-float-left
      :width: 70%

Ground interaction
------------------

These fields apply to both **Bogey** and **Structure** contacts, except where
noted.

**Static friction**
   The friction coefficient that limits the force the ground can apply along
   its surface. A **Structure** contact uses it in every direction while it is
   not sliding. For a wheel, it is the tyre's peak sideways grip and its grip
   along the rolling direction under full brake.

**Dynamic friction**
   The friction coefficient of a **Structure** contact that is sliding. It is
   usually lower than static friction. Wheels do not use it.

**Spring (N/m)**
   The strut stiffness. JSBSim multiplies it by the strut compression to get
   the spring force. A larger value gives a stiffer contact; the value must be
   greater than zero. The contact compresses at rest by roughly the weight it
   carries divided by this value, so the 3000 N/m of a new contact suits only
   a small drone.

**Damping (N/m/s)**
   The damping applied while the strut compresses. It resists compression
   speed and reduces bouncing after touchdown. The value must be greater than
   zero.

**Damping, rebound (N/m/s)**
   The damping applied while the strut extends again. Zero leaves it out of
   ``Gear.xml``, and JSBSim then uses the compression damping for the rebound
   as well.

Wheel fields
------------

The following fields appear only when **Type** is **Bogey**.

**Orientation (deg)**
   The orientation of the strut as roll, pitch, and yaw. The angles are in
   JSBSim's body axes (X forward, Y right, Z down), not in the structural axes
   of **Location**, and they are not an Unreal Engine rotation. JSBSim
   measures the wheel's compression along the strut, and yaw turns the
   direction the wheel rolls. All zeros, as in the example, keep the strut
   along the Z axis with the wheel rolling along X. Positive pitch swings the
   bottom of the strut aft (see the figure under **Location**), and 90 points
   it straight aft, which a tailsitter standing on its tail needs. Positive
   roll swings it to the right. Positive yaw turns the rolling direction to
   the left.

**Rolling friction**
   The friction coefficient along the rolling direction while the brakes are
   off. It is normally much smaller than static friction; the example uses
   ``0.02``.

**Max steer (deg)**
   The wheel's angle at full steering command. The command is
   ``fcs/steer-cmd-norm``, from -1 to 1, and the field takes -90 to 90
   degrees. Zero makes the wheel non-steerable, and a negative value steers it
   the other way, as on a tail wheel. The example nose wheel steers up to 10
   degrees. A file that sets ``max_steer`` to 360 marks a castering wheel; the
   editor shows it as **Castered**.

**Brake group**
   Selects the brake command that acts on this wheel. **Left**, **Right**, and
   **Center** follow ``fcs/left-brake-cmd-norm``,
   ``fcs/right-brake-cmd-norm``, and ``fcs/center-brake-cmd-norm``, each from
   0 to 1. JSBSim treats **Nose** and **Tail** as **Center**, and **None**
   leaves the wheel unbraked. As the command goes from 0 to 1, the friction
   along the rolling direction grows linearly from **Rolling friction** to
   **Static friction**. Main wheels normally use **Left** and **Right**; the
   example nose wheel uses **None**.

   .. image:: ../Images/gear_steer_brake.svg
      :alt: Top view with the nose wheel's steering range and the brake groups of the main wheels
      :class: no-float-left
      :width: 100%

**Retractable**
   Makes the contact follow the gear position ``gear/gear-pos-norm``, where 1
   is down and 0 is up. Below 0.99 the contact produces no force. JSBSim does
   not move the position when the gear command ``gear/gear-cmd-norm``
   changes, so something in the flight control system, such as a logic graph,
   has to drive ``gear/gear-pos-norm``. Leave it cleared for fixed landing
   gear.

**Castered**
   Makes the wheel swivel freely like a trolley wheel and ignore steering
   commands. Leave it cleared for a nose wheel controlled by **Max steer**.

The × in a contact header removes that contact. PteroSim keeps at least one
contact in the model, so the last one cannot be removed.

The aircraft drawing is the Cessna 172 three-view by Marek Cel, CC0, from
Wikimedia Commons.
