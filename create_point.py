import pandas as pd
from transform_coord import *

"""
    Create a point and insert its data into a Treeview widget.

    Parameters:
    - id_entry (tk.Entry): Entry widget containing the point ID.
    - coord_entry (tk.Entry): Entry widget containing the coordinate (format: "latitude longitude").
    - code_entry (tk.Entry): Entry widget containing the survey code.
    - tree_name (tk.Treeview): Treeview widget where the point data will be displayed.
"""


def create_point(id_entry, coord_entry, code_entry, tree_name):

    # Retrieve values from Entry widgets
    point_id = id_entry.get()      # Get the point ID from the ID Entry widget
    coord_input = coord_entry.get()    # Get the coordinate input from the Coordinate Entry widget
    survey_code = code_entry.get()     # Get the survey code from the Code Entry widget

    # Split the coordinate input string into X and Y
    coord_5514 = coord_input.split()
    coord_x_5514 = float(coord_5514[0])  # Extract X from split input and convert to float
    coord_y_5514 = float(coord_5514[1])  # Extract Y from split input and convert to float

    """
    # Split the coordinate input string into latitude and longitude
    coord_4326 = coord_input.split()
    coord_lat_4326 = float(coord_4326[1])   # Extract latitude from split input and convert to float
    coord_lon_4326 = float(coord_4326[0])   # Extract longitude from split input and convert to float
    
    # Convert the coordinates from WGS84 (EPSG:4326) to a specified CRS (e.g., EPSG:5514)
    coord_5514 = transform_4326(coord_lat_4326, coord_lon_4326)

    # Round the transformed coordinates to 3 decimal places
    rounded_y = round(coord_5514[0], 3)   # Round the transformed longitude to 3 decimal places
    rounded_x = round(coord_5514[1], 3)   # Round the transformed latitude to 3 decimal places
    
    """
    # Placeholder for elevation (assuming it's always 0 based on `placeholder_h = round(float(0.000), 3)`)
    placeholder_h = round(float(0.000), 3)

    # Create a DataFrame with the collected data
    data = {'ID': [point_id], 'X': [coord_x_5514], 'Y': [coord_y_5514], 'Code': [survey_code]}
    data_df = pd.DataFrame(data)

    # Insert data from DataFrame into the Treeview widget
    tree_name.insert("", "end", values=(data_df.loc[0, 'ID'],
                                        coord_x_5514, coord_y_5514, placeholder_h, data_df.loc[0, 'Code']))

    # Clear the Entry widgets after inserting data into the Treeview
    id_entry.delete(0, 'end')     # Clear the ID Entry widget
    coord_entry.delete(0, 'end')  # Clear the Coordinate Entry widget
    code_entry.delete(0, 'end')   # Clear the Code Entry widget
