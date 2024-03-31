import pandas as pd

selected_point = pd.DataFrame()
selected_arp = pd.DataFrame()
selected_arp_id = pd.DataFrame()
selected_base = pd.DataFrame()
selected_orientation = pd.DataFrame()


def select_point(tree_name):
    current_point = tree_name.item(tree_name.focus())['values']

    if not current_point:
        print("Error: No points Network Points imported/selected.")
    else:
        global selected_point
        selected_point = pd.DataFrame([current_point], columns=["ID", "X", "Y", "H", "Code"])

        print("Selected Network point:")
        print(selected_point)


def select_arp(tree_name):
    current_arp = tree_name.item(tree_name.focus())['values']

    if not current_arp:
        print("Error: No ARP parameters imported/selected.")
    else:
        global selected_arp
        selected_arp = pd.DataFrame([current_arp], columns=["ARP_ID", "Auth_token", "Prism_height", "Prism_constant"])

        global selected_arp_id
        selected_arp_id = selected_arp["ARP_ID"].astype('string')

        print("Selected ARP:")
        print(selected_arp)


def select_base(tree_name):
    current_base = tree_name.item(tree_name.focus())['values']

    if not current_base:
        print("Error: No points Network Points imported/selected.")
    else:
        global selected_base
        selected_base = pd.DataFrame([current_base], columns=["ID", "X", "Y", "H", "Code"])

        print("Selected ARP Base point:")
        print(selected_base)


def select_orientation(tree_name):
    current_orientation = tree_name.item(tree_name.focus())['values']

    if not current_orientation:
        print("Error: No points Network Points imported/selected.")
    else:
        global selected_orientation
        selected_orientation = pd.DataFrame([current_orientation], columns=["ID", "X", "Y", "H", "Code"])

        print("Selected ARP Orientation point:")
        print(selected_orientation)
