Installation
============

This guide covers building PteroSim from source. Ensure all :doc:`prerequisites` are installed before proceeding.

---

Clone the repository
--------------------

Clone with submodules to get all plugin dependencies:

.. code-block:: bash

   git clone --recursive git@github.com:AlexanderRex/PteroSim.git

If already cloned without ``--recursive``, initialize submodules manually:

.. code-block:: bash

   git submodule update --init --recursive

---

Build JSBSim
------------

Run the build script from the ``devops_data`` directory:

.. code-block:: bash

   cd devops_data
   ./build-jsbsim.bat
   cd ..

---

Generate project files
----------------------

Right-click ``PteroSim.uproject`` and select **Generate Visual Studio project files**.

---

Build the project
-----------------

1. Open ``PteroSim.sln`` in Visual Studio 2022.
2. Set build configuration to **Development Editor**.
3. Build the solution (Ctrl+Shift+B).

---

Launch the editor
-----------------

Run from Visual Studio or double-click ``PteroSim.uproject``.

---

Install Python SDK (optional)
-----------------------------

For gRPC scripting support, install the SDK package:

.. code-block:: bash

   cd Plugins/PteroSimScripting/SDK/python
   pip install -e .
