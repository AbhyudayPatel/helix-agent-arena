"""HELIX - Trajectory Intelligence Platform.

A layer above observability, autonomy, and world-models for self-healing agents.
The unit of observability is the *trajectory*: State -> Decision -> Action ->
Outcome -> State, recorded as a graph, indexed in a vector store, simulated by a
world-model, and repaired by a self-healing controller.

Submodules are imported lazily; importing :mod:`helix` does not pull AppWorld.
"""

__version__ = "0.1.0"
