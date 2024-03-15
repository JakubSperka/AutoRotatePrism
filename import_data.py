"""
Function to import data from txt files used as command in tkinter button
"""

#Import modules and libraries
from tkinter import filedialog
import pandas as pd

network_points = None


def import_network():
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            global network_points
            network_points = pd.read_csv(file_path, names=["ID", "X", "Y", "H", "Code"], delimiter=',')

            # Print or use the data as needed
            print("Imported Network points:")
            print(network_points)

            return network_points

        except Exception as e:
            print(f"Error reading the file: {e}")
    else:
        print("No file selected.")


def import_temp():
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            temp_points = pd.read_csv(file_path, names=["ID", "X", "Y", "H", "Code"], delimiter='\t')

            # Print or use the data as needed
            print("Imported Temporary points:")
            print(temp_points)

        except Exception as e:
            print(f"Error reading the file: {e}")
    else:
        print("No file selected.")
