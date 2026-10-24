Metrics
=======

Metrics supplies the reference geometry used by JSBSim aerodynamic formulas:
wing area, span, chord, incidence, tail dimensions, and reference points.

In the editor
-------------

Select **Metrics** to edit the reference dimensions and the aerodynamic,
eyepoint, and visual reference locations. These values describe the flight
model; they do not resize meshes in :doc:`parts`.

Stored in
---------

PteroSim writes this section to ``Metrics.xml``.

Checks
------

Wing area, span, and chord must be positive. Invalid metrics prevent the model
from reloading.
