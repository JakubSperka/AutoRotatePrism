import pandas as pd
from transform_coord import *


def place_marker(tree_name, map_view):
    selected_point = tree_name.item(tree_name.focus())['values']

    if not selected_point:
        print("Error: No points Network Points imported/selected.")
    else:
        marker_point = pd.DataFrame([selected_point], columns=["ID", "X", "Y", "H", "Code"])

        marker_id = marker_point["ID"].iloc[0]

        marker_x_5514 = marker_point["X"].iloc[0]
        marker_y_5514 = marker_point["Y"].iloc[0]

        print("Selected point:")
        print(marker_x_5514)
        print(marker_y_5514)

        marker_4326 = transform_5514(marker_y_5514, marker_x_5514)

        map_view.set_marker(marker_4326[1], marker_4326[0], text=marker_id)
