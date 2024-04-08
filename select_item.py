# Import necessary modules
from check_connection import *  # Assuming this module exists and is correctly imported
import tkinter as tk  # Assuming tkinter is used for GUI
from calculate_angle import *

# Define global variables as dataframes to store selected data
selected_point = pd.DataFrame()
selected_arp = pd.DataFrame()
selected_arp_id = ""
selected_base = pd.DataFrame()
selected_base_id = ""
selected_orientation = pd.DataFrame()
selected_orientation_id = ""
selected_rotation = pd.DataFrame()
selected_rotation_id = ""
selected_arp_token = ""


def select_point(tree_name):
    """
    Function to select a point from a treeview widget and store it in 'selected_point' dataframe.

    Parameters:
    - tree_name (tkinter.Treeview): Treeview widget containing point data.

    """
    current_point = tree_name.item(tree_name.focus())['values']

    if not current_point:
        print("Error: No points. Network Points not imported or selected.")
    else:
        global selected_point
        selected_point = pd.DataFrame([current_point], columns=["ID", "X", "Y", "H", "Code"])

        print("Selected Network point:")
        print(selected_point)


def delete_point(tree_name):
    """
    Function to delete a selected point from a treeview widget.

    Parameters:
    - tree_name (tkinter.Treeview): Treeview widget containing point data.

    """
    current_point = tree_name.selection()

    if not current_point:
        print("Error: No points. Network Points not imported or selected.")
    else:
        tree_name.delete(current_point)


def select_arp(tree_name, entry_field_id, entry_field_token, entry_arp_status):
    """
    Function to select an ARP (Antenna Reference Point) from a treeview widget and display its details.

    Parameters:
    - tree_name (tkinter.Treeview): Treeview widget containing ARP data.
    - entry_field_id (tkinter.Entry): Entry widget to display ARP ID.
    - entry_field_token (tkinter.Entry): Entry widget to display ARP token.
    - entry_arp_status (tkinter.Label): Label widget to display ARP connection status.

    """
    current_arp = tree_name.item(tree_name.focus())['values']

    if not current_arp:
        print("Error: No ARP parameters imported/selected.")
    else:
        global selected_arp
        selected_arp = pd.DataFrame([current_arp], columns=["ARP_ID", "Auth_token", "Prism_height", "Prism_constant"])

        global selected_arp_id
        selected_arp_id = str(selected_arp["ARP_ID"].iloc[0])

        global selected_arp_token
        selected_arp_token = str(selected_arp["Auth_token"].iloc[0])

        print("Selected ARP:")
        print(selected_arp_id)
        print(selected_arp_token)

        # Check connection using 'check_connection' function (assumed to exist)
        check_connection(selected_arp_token, entry_arp_status)

        # Display selected ARP ID and token in entry fields
        entry_field_id.config(state="normal")
        entry_field_id.delete(0, tk.END)
        entry_field_id.insert(0, selected_arp_id)
        entry_field_id.config(state="readonly")

        entry_field_token.config(state="normal")
        entry_field_token.delete(0, tk.END)
        entry_field_token.insert(0, selected_arp_token)
        entry_field_token.config(state="readonly")


def select_base(tree_name, entry_field):
    """
    Function to select a base point from a treeview widget and display its ID.

    Parameters:
    - tree_name (tkinter.Treeview): Treeview widget containing base point data.
    - entry_field (tkinter.Entry): Entry widget to display base point ID.

    """
    current_base = tree_name.item(tree_name.focus())['values']

    if not current_base:
        print("Error: No points. Network Points not imported or selected.")
    else:
        global selected_base
        selected_base = pd.DataFrame([current_base], columns=["ID", "X", "Y", "H", "Code"])

        global selected_base_id
        selected_base_id = str(selected_base["ID"].iloc[0])

        print("Selected ARP Base point:")
        print(selected_base)

        # Display selected base point ID in entry field
        entry_field.config(state="normal")
        entry_field.delete(0, tk.END)
        entry_field.insert(0, selected_base_id)
        entry_field.config(state="readonly")


def select_orientation(tree_name, entry_field):
    """
    Function to select an orientation point from a treeview widget and display its ID.

    Parameters:
    - tree_name (tkinter.Treeview): Treeview widget containing orientation point data.
    - entry_field (tkinter.Entry): Entry widget to display orientation point ID.

    """
    current_orientation = tree_name.item(tree_name.focus())['values']

    if not current_orientation:
        print("Error: No points. Network Points not imported or selected.")
    else:
        global selected_orientation
        selected_orientation = pd.DataFrame([current_orientation], columns=["ID", "X", "Y", "H", "Code"])

        global selected_orientation_id
        selected_orientation_id = str(selected_orientation["ID"].iloc[0])

        print("Selected ARP Orientation point:")
        print(selected_orientation)

        # Display selected orientation point ID in entry field
        entry_field.config(state="normal")
        entry_field.delete(0, tk.END)
        entry_field.insert(0, selected_orientation_id)
        entry_field.config(state="readonly")


def select_rotation(tree_name, entry_field):
    """
    Function to select a rotation point from a treeview widget and display its ID.

    Parameters:
    - tree_name (tkinter.Treeview): Treeview widget containing rotation point data.
    - entry_field (tkinter.Entry): Entry widget to display rotation point ID.

    """
    current_rotation = tree_name.item(tree_name.focus())['values']

    if not current_rotation:
        print("Error: No points. Network Points not imported or selected.")
    else:
        global selected_rotation
        selected_rotation = pd.DataFrame([current_rotation], columns=["ID", "X", "Y", "H", "Code"])

        global selected_rotation_id
        selected_rotation_id = str(selected_rotation["ID"].iloc[0])

        print("Selected ARP Rotation point:")
        print(selected_rotation)

        # Display selected rotation point ID in entry field
        entry_field.config(state="normal")
        entry_field.delete(0, tk.END)
        entry_field.insert(0, selected_rotation_id)
        entry_field.config(state="readonly")


def update_angle(entry_field):

    token = selected_arp_token
    pin = "v0"
    value = round(calculate_angle(selected_base, selected_orientation, selected_rotation), 5)

    print(f"Importing value: {value}")
    print(f"Token: {token}")

    url = f"https://blynk.cloud/external/api/update?token={token}&{pin}={value}"
    print(url)

    try:
        response = requests.get(url)

        if response.status_code == 200:
            entry_field.config(state="normal")
            entry_field.delete(0, tk.END)  # Clear the entry field
            entry_field.insert(0, f"ARP rotation successful: {round(value, 5)} degrees")  # Update entry
            entry_field.config(state="readonly", foreground="green")
        elif response.status_code == 400:
            error_message = response.json().get('message')  # Extract error message from JSON response
            if error_message:
                entry_field.config(state="normal")
                entry_field.delete(0, tk.END)  # Clear the entry field
                entry_field.insert(0, f"API Error: {error_message}")  # Display API error message
                entry_field.config(state="readonly", foreground="red")
            else:
                entry_field.config(state="normal")
                entry_field.delete(0, tk.END)  # Clear the entry field
                entry_field.insert(0, "Bad request. Check input.")  # Default error message
                entry_field.config(state="readonly", foreground="red")
        else:
            entry_field.config(state="normal")
            entry_field.delete(0, tk.END)  # Clear the entry field
            entry_field.insert(0, f"Unexpected error: {response.status_code}")  # Display unexpected error
            entry_field.config(state="readonly", foreground="orange")
    except requests.exceptions.RequestException as e:
        entry_field.config(state="normal")
        entry_field.delete(0, tk.END)  # Clear the entry field
        entry_field.insert(0, f"Error updating Blynk pin: {e}")  # Display exception message
        entry_field.config(state="readonly", foreground="orange")


def reset_angle(entry_field):

    token = selected_arp_token
    pin = "v0"
    value = round(calculate_angle(selected_base, selected_rotation, selected_orientation), 5)

    print(f"Importing value: {value}")
    print(f"Token: {token}")

    url = f"https://blynk.cloud/external/api/update?token={token}&{pin}={value}"
    print(url)

    try:
        response = requests.get(url)

        if response.status_code == 200:
            entry_field.config(state="normal")
            entry_field.delete(0, tk.END)  # Clear the entry field
            entry_field.insert(0, f"Orientation reset succesful: {round(value, 5)} degrees")  # Update entry
            entry_field.config(state="readonly", foreground="green")
        elif response.status_code == 400:
            error_message = response.json().get('message')  # Extract error message from JSON response
            if error_message:
                entry_field.config(state="normal")
                entry_field.delete(0, tk.END)  # Clear the entry field
                entry_field.insert(0, f"API Error: {error_message}")  # Display API error message
                entry_field.config(state="readonly", foreground="red")
            else:
                entry_field.config(state="normal")
                entry_field.delete(0, tk.END)  # Clear the entry field
                entry_field.insert(0, "Bad request. Check input.")  # Default error message
                entry_field.config(state="readonly", foreground="red")
        else:
            entry_field.config(state="normal")
            entry_field.delete(0, tk.END)  # Clear the entry field
            entry_field.insert(0, f"Unexpected error: {response.status_code}")  # Display unexpected error
            entry_field.config(state="readonly", foreground="orange")
    except requests.exceptions.RequestException as e:
        entry_field.config(state="normal")
        entry_field.delete(0, tk.END)  # Clear the entry field
        entry_field.insert(0, f"Error updating Blynk pin: {e}")  # Display exception message
        entry_field.config(state="readonly", foreground="orange")
