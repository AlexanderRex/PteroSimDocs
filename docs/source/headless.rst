Headless & Automated Runs
=========================

PteroSim can run without a visible window — for CI pipelines, Docker containers,
reinforcement-learning training, and display-less servers. You drive the running
instance over the gRPC :doc:`python_api`; the flags below control *how* the
process renders and how it accepts the license agreement without a human present.

Render modes
------------

Two command-line flags produce a windowless run, but they are **not** equivalent —
they differ on whether the GPU renders at all:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Flag
     - ``-RenderOffScreen``
     - ``-nullrhi``
   * - On-screen window
     - No
     - No
   * - GPU rendering
     - Yes — renders to an off-screen buffer
     - No — null render hardware interface
   * - Camera / image sensors
     - Work (frames are produced)
     - Unavailable (no frames rendered)
   * - Resource use
     - Full GPU
     - Minimal — no GPU
   * - Use when
     - You need camera sensors, screenshots, or pixel data
     - You only need physics, dynamics, and non-visual sensors

Common companions: ``-nosplash`` (skip the splash screen) and ``-unattended``
(declare there is no interactive user, suppressing engine dialogs).

.. code-block:: bash

   # Cameras must render (vision / RL training):
   PteroSim.exe -RenderOffScreen -nosplash     # Windows
   ./PteroSim.sh -RenderOffScreen -nosplash    # Linux

   # Physics only, no cameras (lightest footprint):
   PteroSim.exe -nullrhi -nosplash             # Windows
   ./PteroSim.sh -nullrhi -nosplash            # Linux

Accepting the EULA
------------------

On the **first launch**, PteroSim requires acceptance of the End-User License
Agreement (shipped as ``EULA.txt`` next to the executable). How that happens
depends on whether anyone can click a dialog.

Interactive run (normal window)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A windowed launch shows the EULA dialog once. Clicking **Accept** writes a flag
file (``eula.accepted``) into the save directory (``PteroLabs/``). Every later
launch — including headless ones — sees that file and skips the prompt.

Headless / non-interactive run
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A run where **nobody can click Accept** cannot show the dialog. This covers
``-nullrhi``, ``-RenderOffScreen``, ``-unattended``, dedicated servers, and
commandlets. In every one of these, consent must be given up front, either way:

* Environment variable ``PTEROSIM_ACCEPT_EULA`` set to ``Y``, ``YES``, or ``1``
* Command-line switch ``-AcceptEula``

Setting the variable or passing the flag **constitutes acceptance of the
Agreement**. Both are checked on every launch, before any dialog is created.

.. warning::

   ``-RenderOffScreen`` renders fine but shows no window, so the EULA dialog has
   nowhere to be clicked. Without consent, a non-interactive run prints a notice
   and **exits with code 1** — it does not hang. Supply the env var or
   ``-AcceptEula`` on the first headless launch.

.. note::

   The ``eula.accepted`` file is only ever written by clicking **Accept** in the
   GUI. A machine that has *never* had a windowed launch (a clean Docker image,
   a display-less CI runner) has no such file — always pass
   ``PTEROSIM_ACCEPT_EULA=Y`` or ``-AcceptEula`` there.

Examples
--------

.. code-block:: bash

   # WITHOUT consent → prints notice, exits with code 1:
   PteroSim.exe -RenderOffScreen               # Windows
   ./PteroSim.sh -RenderOffScreen              # Linux

   # WITH consent → starts normally:
   PteroSim.exe -RenderOffScreen -AcceptEula   # Windows
   ./PteroSim.sh -RenderOffScreen -AcceptEula  # Linux

Linux, via the environment variable:

.. code-block:: bash

   export PTEROSIM_ACCEPT_EULA=Y
   ./PteroSim.sh -RenderOffScreen -nosplash

Windows PowerShell:

.. code-block:: powershell

   $env:PTEROSIM_ACCEPT_EULA = "Y"
   .\PteroSim.exe -RenderOffScreen -nosplash

Docker — set consent once in the image or at run time:

.. code-block:: dockerfile

   ENV PTEROSIM_ACCEPT_EULA=Y

.. code-block:: bash

   docker run -e PTEROSIM_ACCEPT_EULA=Y my-pterosim-image
