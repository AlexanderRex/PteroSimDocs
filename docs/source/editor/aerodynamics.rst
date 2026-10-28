Aerodynamics
============

The **Aerodynamics** section defines formulas that produce aerodynamic forces
and moments. The editor reads the formulas stored in the selected vehicle;
their names, inputs, and structure can differ between vehicles.

Function fields
---------------

Each function has a name, an axis, and a formula.

**Name**
   The property under which the function publishes its result. Names are
   case-sensitive and must be unique. For example,
   ``aero/coefficient/CL`` and ``aero/coefficient/Cl`` are different
   properties. When a name matches one of the 20 standard aerodynamic
   derivatives recognized by PteroSim, the editor displays a short
   description under it, such as **Pitch damping**, **Roll per rudder**, or
   **Yaw per aileron (adverse)**.

**Axis**
   Selects where JSBSim adds the function's result. **LIFT**, **DRAG**, and
   **SIDE** are wind-axis forces; **ROLL**, **PITCH**, and **YAW** are moments.
   A vehicle that uses body-axis forces instead is offered **AXIAL**,
   **NORMAL**, **X**, **Y**, and **Z**. Wind-axis and body-axis force families
   cannot be mixed in one vehicle. **(section)** publishes a helper property
   that other formulas can read without adding its result to a force or
   moment.

**Formula type**
   Selects a value source or an operation. Operations contain their inputs as
   indented operands and can be nested. The red cross removes an operand or
   the entire function. **+ operand** is available only while the selected
   operation can accept another operand.

Value sources
-------------

**a property**
   Reads the current value of a simulator property selected in the field
   beside it.

**a number**
   Supplies a constant. Its units depend on the surrounding formula.

**pi**
   Supplies the mathematical constant pi.

**random (gaussian)** and **random (uniform)**
   Supply random values using the distribution stored in the formula.

**a lookup table**
   Returns a value from a curve or multidimensional table.

Operations
----------

The operation picker contains the following groups:

* **multiply**, **add**, **average of**, **subtract**, **smallest of**,
  **largest of**, **all of**, **any of**, and **pick by index** take two or
  more operands.
* **interpolate** takes an input followed by at least two breakpoint/value
  pairs. It therefore requires at least five operands and always uses an odd
  operand count.
* **divide**, **raise to a power**, **atan2 of**, **fmod**, **mod**,
  **is less than**, **is at most**, **is greater than**, **is at least**,
  **equals**, and **differs from** take exactly two operands.
* **absolute value of**, **sin of**, **cos of**, **tan of**, **asin of**,
  **acos of**, **atan of**, **square root of**, **log2 of**, **ln of**,
  **log10 of**, **e to the**, **sign of**, **fraction part of**,
  **integer part of**, **not**, **floor of**, **ceiling of**,
  **degrees to radians**, and **radians to degrees** take exactly one
  operand.
* **round to a multiple** takes one operand to round or a second operand that
  specifies the multiple.
* **if / then / else** takes exactly three operands: the condition, the value
  returned when true, and the value returned when false.
* **rotation: alpha**, **rotation: beta**, and **rotation: gamma** take six
  operands. **rotation: body to wind** and **rotation: wind to body** take
  seven.

If an operation does not yet have the required operand count, the editor
shows **not written yet** followed by the reason. The vehicle file keeps the
last complete version of that formula until the edited tree becomes valid.

Declarations and new functions
------------------------------

**+ declaration** creates a property owned by the aerodynamic section. Enter
its property path and starting value, then read it from formulas like any
other property. A declaration without an explicit value starts at zero.
Removing a declaration while a formula still reads it makes that reference
invalid.

**+ coefficient** adds a function under **LIFT**. Its initial formula is
``aero/qbar-psf × metrics/Sw-sqft × 0``, so it produces zero until its
name, axis, inputs, and constant are changed.

When **Apply to FDM** is pressed, PteroSim checks every property read by an
aerodynamic formula. Apply is refused if the loaded model does not publish a
property, because JSBSim would otherwise read it as zero. When a similar
published name exists, the error includes a **Did you mean...** suggestion.

Lookup tables
-------------

A newly selected **lookup table** starts as a two-row curve looked up in
``aero/alpha-rad``.

For a curve, **looked up in** selects the input property. **in** contains its
breakpoints and **out** contains the returned values. The graph displays the
same pairs. Values between rows are interpolated. Below the first breakpoint
or above the last one, the nearest end value is held constant. **+ Add row**
appends another breakpoint and copies the previous output as its initial
value.

A two-dimensional table is shown as a grid. The upper-left label identifies
the row property, and the first column contains its numeric breakpoints. The
remaining column headings are numeric breakpoints for the column property;
the property name itself is currently not shown or editable in the panel. Its
existing value is preserved when the grid is edited. Each cell is the result
for its row and column breakpoints. Wide grids scroll horizontally.

A three-dimensional table contains several grids. Buttons above it select a
slice by the third property's breakpoint. Adding or removing a row changes
that row in every slice.

Examples
--------

Simple product
~~~~~~~~~~~~~~

``aero/coefficient/CDo`` is assigned to **DRAG**. It multiplies dynamic
pressure, reference wing area, and 0.027. The formula therefore returns a
drag force. The name does not determine the units; the operands and selected
axis do.

.. image:: ../Images/editor_aerodynamics_03.png
   :alt: A drag function built as a simple product
   :class: no-float-left
   :width: 420px

Curve and section helper
~~~~~~~~~~~~~~~~~~~~~~~~

``aero/function/kCDge`` uses **(section)**, so it publishes a value for
other formulas instead of applying a force directly. Its curve looks up
``aero/h_b-mac-ft``: the height of the mean aerodynamic chord above the
ground divided by wing span. This input is dimensionless. The returned
ground-effect multiplier is interpolated between the listed rows and held at
the end values outside their range.

.. image:: ../Images/editor_aerodynamics_01.png
   :alt: A reusable section function containing a lookup curve
   :class: no-float-left
   :width: 420px

Grid
~~~~

``aero/coefficient/CDwbh`` contains a two-dimensional table. Its rows use
``aero/alpha-rad``; the numeric column breakpoints are 0, 10, 20, and 30.
In the source model, the hidden column property is
``fcs/flap-pos-deg``, so each column contains the angle-of-attack values
for one flap position. The table result is multiplied by dynamic pressure,
reference wing area, and the ``kCDge`` helper.

.. image:: ../Images/editor_aerodynamics_04.png
   :alt: A grid indexed by angle of attack and flap position
   :class: no-float-left
   :width: 420px
