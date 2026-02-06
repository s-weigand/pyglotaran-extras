"""Package containing widgets to be used in jupyter notebooks."""

from __future__ import annotations

try:
    import anywidget  # noqa: F401
    import networkx  # noqa: F401
    import traitlets  # noqa: F401

except ImportError:
    msg = (
        "Widget dependencies were not found, install `pyglotaran-extras` with the `widgets` extra "
        '(e.g. `uv pip install "pyglotaran-extras[widgets]"`).'
    )
    raise ImportError(msg) from None

from pyglotaran_extras.widgets.kineticschemevisualizer.visualizer import visualize_dataset_model
from pyglotaran_extras.widgets.kineticschemevisualizer.visualizer import visualize_megacomplex

__all__ = ["visualize_dataset_model", "visualize_megacomplex"]
