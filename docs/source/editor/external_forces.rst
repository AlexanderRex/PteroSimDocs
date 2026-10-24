External Forces
===============

External Forces adds forces or moments driven by a JSBSim property.

In the editor
-------------

Select an external force to set its name, choose force or moment, select the
BODY, LOCAL, WIND, or INERTIAL frame, and edit its location and direction. The
magnitude is written at runtime through
``external_reactions/<name>/magnitude``.

Stored in
---------

PteroSim writes external reactions to ``ExternalReactions.xml``. A script or
:doc:`logic_graphs` must publish the magnitude property.

Checks
------

Names must be usable as property paths, and direction must not be a zero
vector. A runtime force remains zero until something writes its magnitude.
