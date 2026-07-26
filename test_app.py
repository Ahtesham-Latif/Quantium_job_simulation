#Import pytest for testing
import pytest
# Import the Dash app from task3.py
from task3 import app 

# Test to check if the app layout contains the expected components

# 1.Test to check if the header is present
def test_header_present(dash_duo):
    # Start the Dash app in the test environment
    dash_duo.start_server(app)
    # Find the header element by its tag name
    header = dash_duo.find_element("h1")
    # Assert that the header text is as expected
    assert header.text == "Pink Morsel Sales Visualization"
# 2.Test to check if the main graph is present
def test_visualisation_present(dash_duo):

    dash_duo.start_server(app)
    
    # Wait for the graph to be rendered
    dash_duo.wait_for_element("#sales-graph", timeout=10)
    # Check if the graph SVG element is present
    visualisation = dash_duo.wait_for_element("#sales-graph .main-svg", timeout=10)
    
   # Assert that the graph is present
    assert visualisation is not None

# 3.Test to check if the region picker is present
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    # Wait for the region picker to be rendered
    region_picker = dash_duo.find_element("#region-picker") # Ensure this ID matches your radio items/dropdown
    assert region_picker.is_displayed()