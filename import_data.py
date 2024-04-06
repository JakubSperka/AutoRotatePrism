"""
Functions to import data from txt files used as command in tkinter button
"""

# Import modules and libraries
from tkinter import filedialog
import pandas as pd

# Define variables as dataframes for defining global variables later in code
network_points = pd.DataFrame()
temp_points = pd.DataFrame()
arps = pd.DataFrame()

# Function to import geodetic network points


def import_network(tree_name):
    # Get filepath from opened file explorer dialog
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    # Sequence after retrieving the filepath
    if file_path:
        try:
            # Defining global variable and reading, data from .txt file and inserting into dataframe
            global network_points
            network_points = pd.read_csv(file_path, names=["ID", "X", "Y", "H", "Code"], delimiter=',')

            print("Imported Network points:")
            print(network_points)

            # Clear previous data in the Treeview
            tree_name.delete(*tree_name.get_children())

            # Insert data into Treeview
            for index, row in network_points.iterrows():
                tree_name.insert("", "end", values=(row["ID"], row["X"], row["Y"], row["H"], row["Code"]))

        # Error message when invalid file is selected
        except Exception as e:
            print(f"Error reading the file: {e}")

    # Error message when no file is selected
    else:
        print("Error: No file selected.")


def import_temp(tree_name):
    # Get filepath from opened file explorer dialog
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    # Sequence after retrieving the filepath
    if file_path:
        try:
            # Defining global variable and reading, data from .txt file and inserting into dataframe
            global temp_points
            temp_points = pd.read_csv(file_path, names=["ID", "X", "Y", "H", "Code"], delimiter=',')

            print("Imported Temporary points:")
            print(temp_points)

            # Clear previous data in the Treeview
            tree_name.delete(*tree_name.get_children())

            # Insert data into Treeview
            for index, row in temp_points.iterrows():
                tree_name.insert("", "end", values=(row["ID"], row["X"], row["Y"], row["H"], row["Code"]))

        # Error message when invalid file is selected
        except Exception as e:
            print(f"Error reading the file: {e}")

    # Error message when no file is selected
    else:
        print("Error: No file selected.")


def import_arp(tree_name):
    # Get filepath from opened file explorer dialog
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    # Sequence after retrieving the filepath
    if file_path:
        try:
            # Defining global variable and reading, data from .txt file and inserting into dataframe
            global arps
            arps = pd.read_csv(file_path, names=["ARP_ID", "Auth_token", "Prism_height", "Prism_constant"],
                               delimiter=',')

            print("Imported ARPs:")
            print(arps)

            # Clear previous data in the Treeview
            tree_name.delete(*tree_name.get_children())

            # Insert data into Treeview
            for index, row in arps.iterrows():
                tree_name.insert("", "end", values=(row["ARP_ID"], row["Auth_token"], row["Prism_height"],
                                                    row["Prism_constant"]))

        # Error message when invalid file is selected
        except Exception as e:
            print(f"Error reading the file: {e}")

    # Error message when no file is selected
    else:
        print("No file selected.")
