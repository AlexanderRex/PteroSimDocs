Inputs
======

Inputs maps channels from an autopilot actuator frame to motors, control
surfaces, gimbals, grippers, and other writable vehicle properties. A vehicle
can have many bindings. Every numbered binding uses the same fields, and one
frame channel can be assigned to several destinations when one signal must
drive several parts.

.. image:: ../Images/editor_inputs.png
   :alt: Inputs section with motor and elevator channel bindings
   :class: no-float-left

Autopilot
---------

**Autopilot**
   Selects the flight stack whose actuator frame these bindings describe.
   Available choices come from the autopilots installed in PteroSim. Select
   **(none)** for a vehicle that does not receive an autopilot actuator frame.
   The selector is disabled while the simulation is running.

   A binding created in the panel applies to every flight stack. A
   ``Controls.xml`` file can also contain bindings with a ``stack`` attribute;
   the panel shows the ones for the selected flight stack and preserves the
   hidden bindings for other stacks. The panel cannot add or change a
   binding's ``stack`` attribute.

Bindings
--------

**Frame channel**
   The zero-based position of the value in the incoming actuator frame, from
   0 to 15. The numbering and meaning of the channels are defined by the
   selected autopilot. Several bindings may read the same channel; this fans
   one command out to several destinations.

**Destination**
   The vehicle input that receives the mapped value. The list includes each
   motor, externally driven inputs from the vehicle's logic graphs, an
   installed gripper, the axes of a single installed gimbal, and writable
   properties published by the loaded flight model. Of the model properties,
   the list contains properties declared by the vehicle and JSBSim command
   inputs. The list is searchable. Any other writable property path can be
   entered directly.

   Before the model has been loaded by **Apply to FDM**, its properties are
   not available to the panel. The menu then says **Apply once and this
   model's own properties are listed here**; paths can still be entered by
   hand.

   Selecting a motor or gripper resets both ranges to 0 to 1. Selecting a
   gimbal axis resets the input range to -1 to 1 and the output range to -90
   to 90 degrees. Selecting a property does not change either range. Set the
   ranges manually after redirecting a binding to a property; otherwise, for
   example, a 0-to-1 motor range left on a bidirectional control can drive it
   in only one direction.

   PteroSim checks entered property paths when the changes are applied. It
   can perform this check only after the model has been loaded. It then
   refuses a path that the model does not publish as a writable property and
   suggests a similarly named property when possible.

**Drive**
   Sends a raw channel value by hand for checking the binding. It is available
   only while the simulation is running and the active control source is not
   **Manual**. The slider covers the **In, raw** range.

   Moving the slider sends a complete 16-channel test frame. Channels not set
   by a **Drive** slider are sent as zero. The test frame does not take
   permanent control from the autopilot: whichever frame arrives last is the
   one PteroSim applies.

**Live**
   Shows the latest raw channel value followed by the value currently present
   at its destination. A dash means that the simulation is stopped or no frame
   has arrived. If the incoming frame does not contain the selected channel,
   the row reports that the channel is absent. **nothing reads this** means
   that the panel cannot observe where the value went; it does not prove that
   the destination ignored it. A working gripper binding, for example, always
   shows this message.

**In, raw**
   The minimum and maximum values expected on the incoming channel. PteroSim
   clamps the received value to this range and converts its position within
   the range to a value from 0 to 1. A throttle commonly arrives as 0 to 1;
   a centred control commonly arrives as -1 to 1. The two limits must not be
   equal; an equal pair is rejected as **Input range too small**. The editor
   limits both fields to -2 through 2. If any channel in a received frame is
   outside that range, PteroSim rejects the entire frame.

**Out, applied**
   The destination value produced at the two ends of **In, raw**. Values
   between the input limits are mapped linearly between these output limits.
   The units belong to the destination: a motor throttle is normalized,
   while a property ending in ``-deg`` uses degrees. Reversing the two output
   limits is allowed.

**Invert**
   Reverses the mapped output around the midpoint of the output range. It
   swaps the result produced at the two input limits without changing the
   four range fields.

The red **x** removes one binding. **+ Add binding** creates a row on the first
unused frame channel and selects the first unbound motor. If every motor is
already bound, the new row still targets **Motor 0** and asks for another
destination. The button refuses to add a row when all 16 channel numbers are
already in use. To fan one channel out to several destinations, add a row on
an unused channel and then change its **Frame channel** to the duplicate
number.

Errors
------

Red text above the bindings reports failures that leave the inputs unusable.
**No connector was fitted, so no autopilot can reach this vehicle** means that
the selected flight-stack connector could not be installed. **Controls.xml
was not usable and no channels were loaded** means that the controls file
could not be parsed or validated; the rest of the line gives the specific
cause.
