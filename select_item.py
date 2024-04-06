"""
Functions to select data from treeview widget used as command in tkinter button
"""

# Import modules and libraries
import pandas as pd
from check_connection import *

# Define variables as dataframes for defining global variables later in code
selected_point = pd.DataFrame()
selected_arp = pd.DataFrame()
selected_arp_id = pd.DataFrame()
selected_base = pd.DataFrame()
selected_base_id = pd.DataFrame()
selected_orientation = pd.DataFrame()
selected_orientation_id = pd.DataFrame()
selected_rotation = pd.DataFrame()
selected_rotation_id = pd.DataFrame()
selected_arp_token = pd.DataFrame()


def select_point(tree_name):
    current_point = tree_name.item(tree_name.focus())['values']

    if not current_point:
        print("Error: No points Network Points imported/selected.")
    else:
        global selected_point
        selected_point = pd.DataFrame([current_point], columns=["ID", "X", "Y", "H", "Code"])

        print("Selected Network point:")
        print(selected_point)


def delete_point(tree_name):
    current_point = tree_name.selection()

    if not current_point:
        print("Error: No points Network Points imported/selected.")
    else:
        tree_name.delete(current_point)


def select_arp(tree_name, entry_field_id, entry_field_token, entry_arp_status):
    current_arp = tree_name.item(tree_name.focus())['values']

    if not current_arp:
        print("Error: No ARP parameters imported/selected.")
    else:
        global selected_arp
        selected_arp = pd.DataFrame([current_arp], columns=["ARP_ID", "Auth_token", "Prism_height", "Prism_constant"])

        global selected_arp_id
        selected_arp_id = selected_arp["ARP_ID"].astype('string').iloc[0]

        global selected_arp_token
        selected_arp_token = selected_arp["Auth_token"].astype('string').iloc[0]

        print("Selected ARP:")
        print(selected_arp_id)
        print(selected_arp_token)

        check_connection(selected_arp_token, entry_arp_status)

        # Insert selected_arp_id into the entry field
        entry_field_id.config(state="normal")
        entry_field_id.delete(0, tk.END)  # Clear the entry field
        entry_field_id.insert(0, selected_arp_id)  # Insert selected_arp_id
        entry_field_id.config(state="readonly")

        # Insert selected_arp_token into the entry field
        entry_field_token.config(state="normal")
        entry_field_token.delete(0, tk.END)  # Clear the entry field
        entry_field_token.insert(0, selected_arp_token)  # Insert selected_arp_auth_token
        entry_field_token.config(state="readonly")


def select_base(tree_name, entry_field):
    current_base = tree_name.item(tree_name.focus())['values']

    if not current_base:
        print("Error: No points Network Points imported/selected.")
    else:
        global selected_base
        selected_base = pd.DataFrame([current_base], columns=["ID", "X", "Y", "H", "Code"])

        global selected_base_id
        selected_base_id = selected_base["ID"].astype('string').iloc[0]

        print("Selected ARP Base point:")
        print(selected_base)

        # Insert selected_arp_id into the entry field
        entry_field.config(state="normal")
        entry_field.delete(0, tk.END)  # Clear the entry field
        entry_field.insert(0, selected_base_id)  # Insert selected_arp_id
        entry_field.config(state="readonly")


def select_orientation(tree_name, entry_field):
    current_orientation = tree_name.item(tree_name.focus())['values']

    if not current_orientation:
        print("Error: No points Network Points imported/selected.")
    else:
        global selected_orientation
        selected_orientation = pd.DataFrame([current_orientation], columns=["ID", "X", "Y", "H", "Code"])

        global selected_orientation_id
        selected_orientation_id = selected_orientation["ID"].astype('string').iloc[0]

        print("Selected ARP Orientation point:")
        print(selected_orientation)

        # Insert selected_arp_id into the entry field
        entry_field.config(state="normal")
        entry_field.delete(0, tk.END)  # Clear the entry field
        entry_field.insert(0, selected_orientation_id)  # Insert selected_arp_id
        entry_field.config(state="readonly")


def select_rotation(tree_name, entry_field):
    current_rotation = tree_name.item(tree_name.focus())['values']

    if not current_rotation:
        print("Error: No points Network Points imported/selected.")
    else:
        global selected_rotation
        selected_rotation = pd.DataFrame([current_rotation], columns=["ID", "X", "Y", "H", "Code"])

        global selected_rotation_id
        selected_rotation_id = selected_rotation["ID"].astype('string').iloc[0]

        print("Selected ARP Rotation point:")
        print(selected_rotation)

        # Insert selected_arp_id into the entry field
        entry_field.config(state="normal")
        entry_field.delete(0, tk.END)  # Clear the entry field
        entry_field.insert(0, selected_rotation_id)  # Insert selected_arp_id
        entry_field.config(state="readonly")
