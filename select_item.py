import pandas as pd

selected_point = pd.DataFrame()


def select_point(tree_name):
    current_item = tree_name.item(tree_name.focus())['values']

    if not current_item:
        print("Error: No points Network Points imported.")
    else:
        global selected_point
        selected_point = pd.DataFrame([current_item], columns=["ID", "X", "Y", "H", "Code"])

        print("Selected Network point:")
        print(selected_point)