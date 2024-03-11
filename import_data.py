"""
Function to import data from txt files used as command in tkinter button
"""
from tkinter import filedialog
import pandas as pd


def import_network():
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            # Assuming your TXT file has a header row
            network_points = pd.read_csv(file_path, delimiter=',')  # Adjust delimiter if needed

            # Print or use the data as needed
            print("Imported Network points:")
            print(network_points)

        except Exception as e:
            print(f"Error reading the file: {e}")
    else:
        print("No file selected.")


def import_temp():
    file_path = filedialog.askopenfilename(title="Select Point Data File", filetypes=[("Text files", "*.txt")])

    if file_path:
        try:
            # Assuming your TXT file has a header row
            temp_points = pd.read_csv(file_path, delimiter='\t')  # Adjust delimiter if needed

            # Print or use the data as needed
            print("Imported Temporary points:")
            print(temp_points)

        except Exception as e:
            print(f"Error reading the file: {e}")
    else:
        print("No file selected.")
