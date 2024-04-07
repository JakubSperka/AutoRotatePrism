import pandas as pd
from transform_coord import *


def center_mapview(tree_name, map_view):
    """
    Centers the map view on a selected point from a tree view and zooms in.

    Parameters:
    - tree_name: The tree view widget containing point data.
    - map_view: The map view widget to be centered and zoomed.

    Description:
    This function retrieves the coordinates of a selected point from the tree view,
    transforms the coordinates to EPSG:4326 (WGS84), and centers the map view on
    this point with a zoom level of 19.

    Instructions:
    1. Select a point in the tree view widget (`tree_name`) by clicking on it.
    2. Call this function with the selected tree view (`tree_name`) and the map view (`map_view`).
    """

    # Retrieve the selected point data from the tree view item
    selected_point = tree_name.item(tree_name.focus())['values']

    # Check if a point is selected
    if not selected_point:
        # If no point is selected, display an error message
        print("Error: No points Network Points imported/selected.")
    else:
        # Create a DataFrame from the selected point data
        center_point = pd.DataFrame([selected_point], columns=["ID", "X", "Y", "H", "Code"])

        # Extract X and Y coordinates from the DataFrame
        center_x_5514 = center_point["X"].iloc[0]
        center_y_5514 = center_point["Y"].iloc[0]

        # Print the selected point coordinates
        print("Selected point:")
        print(center_x_5514)
        print(center_y_5514)

        # Transform the coordinates from EPSG:5514 to EPSG:4326 (WGS84)
        center_4326 = transform_5514(center_y_5514, center_x_5514)

        # Set the map view position to the transformed coordinates
        map_view.set_position(center_4326[1], center_4326[0])
        # Set the zoom level of the map view to 19
        map_view.set_zoom(19)
