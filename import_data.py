"""
Function to import data from txt files used as command in tkinter button
"""

# Import modules and libraries
from tkinter import filedialog
import pandas as pd

network_points = pd.DataFrame()


def import_network(tree):
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            global network_points
            network_points = pd.read_csv(file_path, names=["ID", "X", "Y", "H", "Code"], delimiter=',')

            print("Imported Network points:")
            print(network_points)

            # Clear previous data in the Treeview
            tree.delete(*tree.get_children())

            for index, row in network_points.iterrows():
                tree.insert("", "end", values=(row["ID"], row["X"], row["Y"], row["H"], row["Code"]))

        except Exception as e:
            print(f"Error reading the file: {e}")
    else:
        print("No file selected.")
