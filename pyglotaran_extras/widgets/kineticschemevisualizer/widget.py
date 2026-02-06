"""Kinetic Scheme Visualizer widget module."""

from __future__ import annotations

import pathlib
from typing import TYPE_CHECKING
from typing import Any

import anywidget
import traitlets

if TYPE_CHECKING:
    from collections.abc import Mapping


class GraphWidget(anywidget.AnyWidget):
    """Widget for editing kinetic scheme graphs."""

    _esm: pathlib.Path = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css: pathlib.Path = pathlib.Path(__file__).parent / "static" / "widget.css"
    graph_data = traitlets.Dict().tag(sync=True)
    visualization_options = traitlets.Dict().tag(sync=True)
    cy_json = traitlets.Dict({}).tag(sync=True)
    height = traitlets.Int(default_value=600).tag(sync=True)

    def __init__(
        self,
        graph_data: Mapping[str, Any] | None = None,
        visualization_options: dict[str, Any] | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.graph_data = graph_data if graph_data is not None else {}
        self.visualization_options = (
            visualization_options if visualization_options is not None else {}
        )
        super().__init__(*args, **kwargs)
