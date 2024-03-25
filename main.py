"""
Main program for APR Control panel GUI
"""

# Imported packages
import tkinter as tk
from tkinter import ttk
from import_data import import_network

# Set root GUI window
root = tk.Tk()
root.title("ARP Control Panel v.1.0.0")

# Create a frame from imported network points
frame_network_points = tk.LabelFrame(root, text="Imported network points", padx=10, pady=10)
frame_network_points.pack()

# Create a Treeview widget
network_tree = ttk.Treeview(frame_network_points, columns=["ID", "X", "Y", "H", "Code"],
                            show="headings", selectmode="browse")
network_tree.pack(pady=10)

# Add columns to the Treeview for imported network points
for col in ["ID", "X", "Y", "H", "Code"]:
    network_tree.heading(col, text=col, anchor="w")
    network_tree.column(col, anchor="w", width=100)

# Add button for importing network points
import_button = tk.Button(frame_network_points, text="Import Point Data", command=lambda: import_network(network_tree))
import_button.pack(pady=5)

# Initialize mainloop for the root window
root.mainloop()
