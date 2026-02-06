import pytest
from task3 import app # or however you import your dash app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    # Match exactly what appears in your browser
    assert header.text == "Pink Morsel Sales Visualization"

def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    
    # 1. Wait for the graph container to exist
    dash_duo.wait_for_element("#sales-graph", timeout=10)
    
    # 2. Wait for the Plotly-specific SVG to appear inside the container.
    # This is the "true" check that the graph has finished rendering.
    visualisation = dash_duo.wait_for_element("#sales-graph .main-svg", timeout=10)
    
    # If the above line doesn't time out, the graph is present and rendered.
    assert visualisation is not None

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    region_picker = dash_duo.find_element("#region-picker") # Ensure this ID matches your radio items/dropdown
    assert region_picker.is_displayed()