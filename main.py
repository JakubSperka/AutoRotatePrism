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

"""
Commands for Network points tab
"""
# Create a frame for imported network points
frame_network_points = tk.LabelFrame(root, text="Imported network points", padx=10, pady=10)
frame_network_points.pack()

# Create a frame for network points Treeview
treeview_frame_network_points = tk.Frame(frame_network_points)
treeview_frame_network_points.pack()

# Create a scrollbar for network points Treeview
network_tree_scrollbar = tk.Scrollbar(treeview_frame_network_points)
network_tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Treeview widget for imported network points
network_tree = ttk.Treeview(treeview_frame_network_points, columns=["ID", "X", "Y", "H", "Code"],
                            show="headings", selectmode="browse", yscrollcommand=network_tree_scrollbar.set)
network_tree.pack()

# Config scrollbar for network points Treeview
network_tree_scrollbar.config(command=network_tree.yview)

# Add columns to the Treeview for imported network points
for col in ["ID", "X", "Y", "H", "Code"]:
    network_tree.heading(col, text=col, anchor="w")
    network_tree.column(col, anchor="w", width=100)

# Add button for importing network points
import_button = tk.Button(frame_network_points, text="Import Point Data", command=lambda: import_network(network_tree))
import_button.pack(pady=5)

"""
Commands for Equipment tab
"""

# Create a frame for equipment tab
frame_equipment = tk.LabelFrame(root, text="Equipment", padx=10, pady=10)
frame_equipment.pack()

# Create a frame for equipment Treeview
treeview_frame_equipment = tk.Frame(frame_equipment)
treeview_frame_equipment.pack()

# Create a scrollbar for equipment Treeview
equipment_tree_scrollbar = tk.Scrollbar(treeview_frame_equipment)
equipment_tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Treeview widget for equipment
equipment_tree = ttk.Treeview(treeview_frame_equipment,
                              columns=["ARP_ID", "Auth_token", "Prism_height", "Prism_constant"],
                              show="headings", selectmode="browse", yscrollcommand=equipment_tree_scrollbar.set)
equipment_tree.pack()

# Config scrollbar for equipment Treeview
equipment_tree_scrollbar.config(command=equipment_tree.yview)

# Add columns to the Treeview for equipment
for col in ["ARP_ID", "Auth_token", "Prism_height", "Prism_constant"]:
    equipment_tree.heading(col, text=col, anchor="w")
    equipment_tree.column(col, anchor="w", width=125)

# Initialize mainloop for the root window
root.mainloop()
