# tests/test_app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app import app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("#header")
    assert header is not None
    assert "Quantium Dashboard" in header.text

def test_visualization_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#graph")
    assert graph is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dropdown = dash_duo.find_element("#region-picker")
    assert dropdown is not None
