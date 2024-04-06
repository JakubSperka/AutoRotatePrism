import pandas as pd
from transform_coord import *


def create_point(id_entry, coord_entry, code_entry, tree_name):
    # Retrieve values from Entry widgets
    point_id = id_entry.get()
    coord_input = coord_entry.get()
    survey_code = code_entry.get()

    coord_4326 = coord_input.split()

    coord_lat_4326 = float(coord_4326[0])
    coord_lon_4326 = float(coord_4326[1])

    # Assuming 'transform_4326' is a function that converts coordinates
    coord_5514 = transform_4326(coord_lat_4326, coord_lon_4326)

    # Round the coordinates to 3 decimal places
    rounded_x = round(coord_5514[1], 3)
    rounded_y = round(coord_5514[0], 3)

    placeholder_h = round(float(0.000), 3)

    # Create a DataFrame with the collected data
    data = {'ID': [point_id], 'X': [rounded_x], 'Y': [rounded_y], 'Code': [survey_code]}
    data_df = pd.DataFrame(data)

    # Insert data from DataFrame into the Treeview
    tree_name.insert("", "end", values=(data_df.loc[0, 'ID'],
                                        rounded_x, rounded_y, placeholder_h, data_df.loc[0, 'Code']))

    id_entry.delete(0, 'end')
    coord_entry.delete(0, 'end')
    code_entry.delete(0, 'end')
