Metrics
=======

Metrics defines the reference geometry and reference points used by the JSBSim
flight model. It does not resize or move the meshes in ``Visual.xml``.

.. image:: ../Images/editor_metrics.png
   :alt: Metrics section in the vehicle editor
   :class: no-float-left

Fields
------

The three boxes in each point field are X, Y, and Z from left to right. These
points use the JSBSim structural frame: X points aft, Y right, and Z up.
Reference-point positions in the illustrations are schematic and model-dependent.

**Wing area, m²**
   The reference wing area, usually written as *S*. JSBSim combines it with
   dynamic pressure to provide ``qbar × S``, which aerodynamic functions use
   to turn dimensionless coefficients into forces. It is a reference value,
   not an area calculated from the visual mesh. The value must be greater than
   zero.

   .. image:: ../Images/metrics_wing_area.png
      :alt: Main-wing planform area
      :class: no-float-left
      :width: 100%

**Wing span, m**
   The reference distance from one wingtip to the other, usually written as
   *b*. JSBSim uses it as the lateral reference length for aerodynamic rates
   and coefficients. It is also used when JSBSim calculates the vertical-tail
   volume coefficient. The value must be greater than zero.

   .. image:: ../Images/metrics_wing_span.png
      :alt: Wingtip-to-wingtip span
      :class: no-float-left
      :width: 100%

**Chord, m**
   The mean aerodynamic chord, usually written as *c̄*. It is the longitudinal
   reference length for aerodynamic rates and pitching moments. JSBSim also
   uses it to calculate the horizontal-tail volume coefficient and Reynolds
   number. The value must be greater than zero.

   .. image:: ../Images/metrics_chord.png
      :alt: Mean aerodynamic chord between leading and trailing edges
      :class: no-float-left
      :width: 100%

**Wing incidence, deg**
   The angle between the wing reference line and the aircraft body axis.
   Positive incidence increases the wing's effective angle of attack while the
   body attitude stays unchanged. The editor accepts values from -90 to 90
   degrees.

   .. image:: ../Images/metrics_wing_incidence.png
      :alt: Wing incidence relative to the body reference line
      :class: no-float-left
      :width: 100%

**H-tail area, m²**
   The reference area of the horizontal tail. Together with **H-tail arm**, wing
   area, and chord, it defines the horizontal-tail volume coefficient:
   ``arm × tail area / (chord × wing area)``. This value does not create a tail
   force by itself; an aerodynamic function must use the resulting metric.

   .. image:: ../Images/metrics_h_tail_area.png
      :alt: Horizontal-tail planform area
      :class: no-float-left
      :width: 100%

**H-tail arm, m**
   The horizontal tail's reference lever arm. PteroSim draws it aft from the
   aerodynamic reference point. JSBSim uses it to calculate the normalized
   horizontal-tail arm and horizontal-tail volume coefficient. Use zero when
   the model does not use these derived metrics.

   .. image:: ../Images/metrics_h_tail_arm.png
      :alt: Horizontal-tail arm measured aft from the aerodynamic reference point
      :class: no-float-left
      :width: 100%

**V-tail area, m²**
   The reference area of the vertical tail. Together with **V-tail arm**, wing
   area, and wing span, it defines the vertical-tail volume coefficient:
   ``arm × tail area / (wing span × wing area)``. This value does not create a
   side force or yawing moment by itself.

   .. image:: ../Images/metrics_v_tail_area.png
      :alt: Vertical-tail area in side view
      :class: no-float-left
      :width: 100%

**V-tail arm, m**
   The vertical tail's reference lever arm. PteroSim draws it aft from the
   aerodynamic reference point. JSBSim uses it to calculate the normalized
   vertical-tail arm and vertical-tail volume coefficient. Use zero when the
   model does not use these derived metrics.

   .. image:: ../Images/metrics_v_tail_arm.png
      :alt: Vertical-tail arm measured along the fuselage
      :class: no-float-left
      :width: 100%

**Aero ref point, m**
   The point where JSBSim applies the resulting aerodynamic forces. Its offset
   from the centre of gravity determines the additional moment produced by
   those forces. Place it at the aerodynamic reference point used when deriving
   the model's coefficients.

   .. image:: ../Images/metrics_aero_ref_point.png
      :alt: Aerodynamic force applied at an offset from the centre of gravity
      :class: no-float-left
      :width: 100%

**Eyepoint, m**
   The pilot's eye position. JSBSim uses its offset from the centre of gravity
   when calculating accelerations sensed by the pilot during rotation. It does
   not position a PteroSim camera; cameras are configured under
   :doc:`sensors`.

   .. image:: ../Images/metrics_eyepoint.png
      :alt: Pilot eye position inside the cockpit
      :class: no-float-left
      :width: 100%

**Visual ref point, m**
   The point whose world position JSBSim reports to an external visual system.
   It does not move meshes authored in ``Visual.xml``. PteroSim retains the
   value and shows the point in debug drawing.

   .. image:: ../Images/metrics_visual_ref_point.png
      :alt: Model-defined visual reference point
      :class: no-float-left
      :width: 100%
