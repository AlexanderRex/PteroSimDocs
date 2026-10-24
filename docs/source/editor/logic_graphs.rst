Logic Graphs
============

Logic graphs transform properties and actuator commands into the values used by
motors, aerodynamic formulas, control surfaces, and other systems.

In the editor
-------------

Select a control channel, then open its graph. Add nodes, connect outputs to
inputs, and name published properties explicitly. Add another channel with
**+ Add > Control channel**. The graph view fills the centre of the viewport;
close it to return to normal scene interaction.

Stored in
---------

Graphs are stored in ``FlightControl.xml`` or under ``Systems``.

Checks
------

Required inputs must be connected. Node names and output properties must be
valid and unambiguous.
