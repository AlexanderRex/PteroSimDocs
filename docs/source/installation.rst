Installation
============

1. Clone repository with submodules:

   .. code-block:: bash

      git clone --recursive git@github.com:AlexanderRex/PteroSim.git

   If already cloned without ``--recursive``:

   .. code-block:: bash

      git submodule update --init --recursive

2. Build JSBSim (run from ``devops_data``, e.g. in PowerShell):

   .. code-block:: bash

      cd devops_data
      ./build-jsbsim.bat
      cd ..

3. Right-click ``PteroSim.uproject`` → **Generate Visual Studio project files**

4. Open ``PteroSim.sln`` in Visual Studio 2022

5. Set build configuration to **Development Editor**

6. Build the solution (Ctrl+Shift+B)

7. Launch the editor from Visual Studio or double-click ``PteroSim.uproject``

8. Install PteroSim Python SDK (optional, for gRPC scripting):

   .. code-block:: bash

      cd Plugins/PteroSimScripting/SDK/python
      pip install -e .
      cd -
