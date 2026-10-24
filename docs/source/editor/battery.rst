Battery
=======

Battery models the electrical pack that supplies supported brushless motors
and avionics. A vehicle can carry one pack.

In the editor
-------------

Add a pack with **+ Add > Battery**. Select its chemistry, series and parallel
cell counts, cell capacity and resistance, initial charge, warning threshold,
and avionics load. **Infinite** keeps charge constant while retaining voltage
sag under load.

Stored in
---------

The pack is stored in ``Battery.xml``. Its chemistry table is stored under
``Batteries`` in the vehicle directory. Battery mass must be included in
:doc:`mass_balance` separately.

Checks
------

The chemistry file must exist and its open-circuit-voltage table must rise from
empty to full charge. Cell counts and capacity must be positive. Percentages
must stay between 0 and 100.
