Python Examples
===============

This page documents practical Python scripts from ``PteroSimScripts``.
Use it as a workflow guide; for method contracts and return types see :doc:`python_api`.

Prerequisites
-------------

* Running PteroSim with gRPC endpoint available (default ``localhost:10010``).
* Python 3.10+ environment with dependencies from ``PteroSimScripts/requirements.txt``.
* Installed ``pterosim`` SDK package compatible with your simulator build.

Quick setup
-----------

.. code-block:: bash

   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt

run_rl_hover_train.py
---------------------

Purpose
^^^^^^^

Single-drone SAC hover training with raw motor control.
The script uses ``set_actuator_controls()`` and IMU/status observations.

Typical commands
^^^^^^^^^^^^^^^^

.. code-block:: bash

   python run_rl_hover_train.py --mode train --timesteps 500000
   python run_rl_hover_train.py --mode play --load checkpoints/sac_hover.zip

Key CLI arguments
^^^^^^^^^^^^^^^^^

* ``--mode``: ``train`` or ``play``.
* ``--sim-address``: gRPC address (default ``localhost:10010``).
* ``--aircraft``: aircraft class name (default ``F450``).
* ``--timesteps``: total train timesteps (default ``500000``).
* ``--time-scale``: simulator speed multiplier.
* ``--load``: checkpoint path for resume/play.
* ``--save``: checkpoint base path (without ``.zip``).
* ``--tensorboard-log`` and ``--run-name``: TensorBoard output setup.

Outputs
^^^^^^^

* Checkpoints in ``checkpoints/``.
* TensorBoard logs in ``tensorboard_logs/``.

run_rl_race_train.py
--------------------

Purpose
^^^^^^^

Race RL training with C++ attitude controller.
The script uses ``set_attitude_command()``, race APIs (gates/state/reset), and IMU/status observations.

Typical commands
^^^^^^^^^^^^^^^^

.. code-block:: bash

   python run_rl_race_train.py --mode train --algo sac --timesteps 500000
   python run_rl_race_train.py --mode play --algo sac --load checkpoints/sac_pterorace.zip
   python run_rl_race_train.py --mode optuna --optuna-trials 50 --optuna-timesteps 30000

Key CLI arguments
^^^^^^^^^^^^^^^^^

* ``--mode``: ``random``, ``train``, ``play``, ``optuna``.
* ``--algo``: ``sac`` or ``ppo``.
* ``--sim``: gRPC address (default ``localhost:10010``).
* ``--episodes``: episode count for random/play flows.
* ``--timesteps`` or ``--max-iterations``: training duration control.
* ``--time-scale``: simulator speed multiplier.
* ``--load`` and ``--save``: checkpoint paths.
* ``--optuna-*`` flags: hyperparameter search configuration.

Outputs
^^^^^^^

* Checkpoints in ``checkpoints/``.
* Optional Optuna artifacts in ``optuna_checkpoints/`` or configured storage backend.
* TensorBoard logs in ``tensorboard_logs/``.

test_pid_hover.py
-----------------

Purpose
^^^^^^^

Smoke test for C++ attitude PID stabilization with fixed hover throttle.
Useful to validate actuator/controller pipeline before RL training.

Typical command
^^^^^^^^^^^^^^^

.. code-block:: bash

   python test_pid_hover.py

What it does
^^^^^^^^^^^^

* Starts simulation and spawns (or reuses) an ``F450`` aircraft.
* Sends ``set_attitude_command()`` with zero angles and constant throttle.
* Runs fixed-step loop and prints altitude/attitude health.

Troubleshooting
---------------

* ``UNAVAILABLE`` gRPC errors: verify simulator is running and address/port are correct.
* Empty ``aircraft_status()`` or missing sensors: ensure aircraft is spawned and map has required components.
* Unstable training: start with lower ``--time-scale`` and verify baseline with ``test_pid_hover.py``.
* Missing RL packages: reinstall ``requirements.txt`` in an isolated virtual environment.
