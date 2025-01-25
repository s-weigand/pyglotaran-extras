from __future__ import annotations

import json
from typing import TYPE_CHECKING

from pydantic import BaseModel
from pydantic import ConfigDict

from pyglotaran_extras.widgets.kineticschemevisualizer.utils import build_all_transitions
from pyglotaran_extras.widgets.kineticschemevisualizer.utils import dump_cytpscape_json_data
from pyglotaran_extras.widgets.kineticschemevisualizer.utils import (
    get_filled_megacomplex_k_matrices,
)
from pyglotaran_extras.widgets.kineticschemevisualizer.widget import GraphWidget

if TYPE_CHECKING:
    from glotaran.model.model import Model
    from glotaran.parameter.parameters import Parameters


class Node(BaseModel):
    """Data used to visualize a node."""

    alternate_name: str | None = None
    width: int | None = 80
    height: int | None = 30


class VisualizationOptions(BaseModel):
    """Visualization option for visualizer functions."""

    model_config = ConfigDict(extra="allow")

    nodes: dict[str, Node] = {}
    colour_node_mapping: dict[str, list[str]] = {}
    omitted_rate_constants: list[str] = []


def visualize_megacomplex(
    megacomplex: str | list[str],
    model: Model,
    parameter: Parameters,
    visualization_options: VisualizationOptions = VisualizationOptions(),
) -> GraphWidget:
    megacomplexes = [megacomplex] if isinstance(megacomplex, str) else megacomplex

    k_matrices = get_filled_megacomplex_k_matrices(megacomplexes, model, parameter)

    transitions = build_all_transitions(k_matrices, visualization_options.omitted_rate_constants)

    graph_data = dump_cytpscape_json_data(transitions)

    return GraphWidget(graph_data, visualization_options=visualization_options.__dict__)


def visualize_dataset_model(
    dataset_model: str,
    model: Model,
    parameter: Parameters,
    exclude_megacomplexes: list[str] | None = None,
    visualization_options: VisualizationOptions = VisualizationOptions(),
) -> GraphWidget:
    if dataset_model not in model.dataset:
        msg = f"Dataset model {dataset_model} not found in the model."
        raise ValueError(msg)

    associated_megacomplexes = model.dataset[dataset_model].megacomplex
    if exclude_megacomplexes:
        megacomplexes = [mc for mc in associated_megacomplexes if mc not in exclude_megacomplexes]
    else:
        megacomplexes = associated_megacomplexes

    k_matrices = get_filled_megacomplex_k_matrices(megacomplexes, model, parameter)

    transitions = build_all_transitions(k_matrices, visualization_options.omitted_rate_constants)

    graph_data = dump_cytpscape_json_data(transitions)

    return GraphWidget(
        graph_data=graph_data,
        visualization_options=visualization_options.model_dump(),
    )
