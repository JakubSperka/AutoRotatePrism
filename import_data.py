# Import necessary modules and libraries
from tkinter import filedialog  # Module for file dialog
import pandas as pd  # Module for data manipulation and analysis

# Define global variables as empty DataFrames
network_points = pd.DataFrame()
temp_points = pd.DataFrame()
arps = pd.DataFrame()


def import_network(tree_name):
    """
    Function to import geodetic network points from a text file.

    Parameters:
    tree_name (tkinter.Treeview): Treeview widget to display imported data.

    Returns:
    None
    """
    # Get file path using file dialog
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    # Process after retrieving the file path
    if file_path:
        try:
            # Define global variable and read data from the text file into a DataFrame
            global network_points
            network_points = pd.read_csv(file_path, names=["ID", "X", "Y", "H", "Code"], delimiter=',')

            print("Imported Network points:")
            print(network_points)

            # Clear previous data in the Treeview
            tree_name.delete(*tree_name.get_children())

            # Insert data into Treeview
            for index, row in network_points.iterrows():
                tree_name.insert("", "end", values=(row["ID"], row["X"], row["Y"], row["H"], row["Code"]))

        # Error handling for invalid file selection
        except Exception as e:
            print(f"Error reading the file: {e}")

    # Error message when no file is selected
    else:
        print("Error: No file selected.")


# Function to import temporary points from a text file
def import_temp(tree_name):
    """
    Function to import temporary points from a text file.

    Parameters:
    tree_name (tkinter.Treeview): Treeview widget to display imported data.

    Returns:
    None
    """
    # Get file path using file dialog
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    # Process after retrieving the file path
    if file_path:
        try:
            # Define global variable and read data from the text file into a DataFrame
            global temp_points
            temp_points = pd.read_csv(file_path, names=["ID", "X", "Y", "H", "Code"], delimiter=',')

            print("Imported Temporary points:")
            print(temp_points)

            # Clear previous data in the Treeview
            tree_name.delete(*tree_name.get_children())

            # Insert data into Treeview
            for index, row in temp_points.iterrows():
                tree_name.insert("", "end", values=(row["ID"], row["X"], row["Y"], row["H"], row["Code"]))

        # Error handling for invalid file selection
        except Exception as e:
            print(f"Error reading the file: {e}")

    # Error message when no file is selected
    else:
        print("Error: No file selected.")


# Function to import ARP (Automatic Target Recognition) points from a text file
def import_arp(tree_name):
    """
    Function to import ARP (Automatic Target Recognition) points from a text file.

    Parameters:
    tree_name (tkinter.Treeview): Treeview widget to display imported data.

    Returns:
    None
    """
    # Get file path using file dialog
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    # Process after retrieving the file path
    if file_path:
        try:
            # Define global variable and read data from the text file into a DataFrame
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

        # Error handling for invalid file selection
        except Exception as e:
            print(f"Error reading the file: {e}")

    # Error message when no file is selected
    else:
        print("Error: No file selected.")
