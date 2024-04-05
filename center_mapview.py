import pandas as pd
from transform_coord import *


def center_mapview(tree_name, map_view):
    selected_point = tree_name.item(tree_name.focus())['values']

    if not selected_point:
        print("Error: No points Network Points imported/selected.")
    else:
        center_point = pd.DataFrame([selected_point], columns=["ID", "X", "Y", "H", "Code"])

        center_x_5514 = center_point["X"].iloc[0]
        center_y_5514 = center_point["Y"].iloc[0]

        print("Selected point:")
        print(center_x_5514)
        print(center_y_5514)

        center_4326 = transform_5514(center_y_5514, center_x_5514)

        map_view.set_position(center_4326[1], center_4326[0])
        map_view.set_zoom(19)
