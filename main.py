"""
Main program for APR Control panel GUI
"""

# Imported packages
import tkinter as tk
from tkinter import ttk
from import_data import import_network, import_arp
from select_item import select_point, select_arp

# Set root GUI window
root = tk.Tk()
root.title("ARP Control Panel v.1.0.0")
root.iconbitmap("compass.ico")

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
                            show="headings", selectmode="browse", yscrollcommand=network_tree_scrollbar.set, height=5)
network_tree.pack()

# Config scrollbar for network points Treeview
network_tree_scrollbar.config(command=network_tree.yview)

# Add columns to the Treeview for imported network points
for col in ["ID", "X", "Y", "H", "Code"]:
    network_tree.heading(col, text=col, anchor="w")
    network_tree.column(col, anchor="w", width=100)

# Add button for importing network points
import_button_network = tk.Button(frame_network_points, text="Import Point Data",
                                  command=lambda: import_network(network_tree))
import_button_network.pack(pady=5)

# Add button for selecting values in network points Treeview
select_button_network = tk.Button(frame_network_points, text="Select Point",
                                  command=lambda: select_point(network_tree))
select_button_network.pack(pady=5)

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
                              show="headings", selectmode="browse",
                              yscrollcommand=equipment_tree_scrollbar.set, height=5)
equipment_tree.pack()

# Config scrollbar for equipment Treeview
equipment_tree_scrollbar.config(command=equipment_tree.yview)

# Add columns to the Treeview for equipment
equipment_tree.heading("ARP_ID", text="ARP ID", anchor="w")
equipment_tree.heading("Auth_token", text="Blynk Authentification token", anchor="w")
equipment_tree.heading("Prism_height", text="Target height", anchor="w")
equipment_tree.heading("Prism_constant", text="Prism constant", anchor="w")

equipment_tree.column("ARP_ID", anchor="w", width=75)
equipment_tree.column("Auth_token", anchor="w", width=225)
equipment_tree.column("Prism_height", anchor="w", width=100)
equipment_tree.column("Prism_constant", anchor="w", width=100)

# Add button for importing network points
import_button_arps = tk.Button(frame_equipment, text="Import Equipment",
                               command=lambda: import_arp(equipment_tree))
import_button_arps.pack(pady=5)

"""
Commands for ARP Status tab
"""

# Create labelframe for ARP control widgets
frame_arp_control = tk.LabelFrame(frame_equipment,
                                  text="ARP Status", padx=10, pady=10)
frame_arp_control.pack()

# Create label for ARP ID entry widgets
label_entry_arp_id = tk.Label(frame_arp_control, text="ARP ID:")
label_entry_arp_id.grid(row=0, column=0, sticky="e")

# Create entry widget for ARP ID
entry_arp_id = tk.Entry(frame_arp_control, width=25)
entry_arp_id.grid(row=0, column=1)

# Create label for ARP auth token entry widgets
label_entry_arp_auth_token = tk.Label(frame_arp_control, text="Auth. Token:")
label_entry_arp_auth_token.grid(row=1, column=0, sticky="e")

# Create entry widget for ARP auth token
entry_arp_auth_token = tk.Entry(frame_arp_control, width=25)
entry_arp_auth_token.grid(row=1, column=1)

# Create label for ARP Status entry widgets
label_entry_arp_status = tk.Label(frame_arp_control, text="Status:")
label_entry_arp_status.grid(row=2, column=0, sticky="e")

# Create entry widget for ARP Status
entry_arp_status = tk.Entry(frame_arp_control, width=25)
entry_arp_status.grid(row=2, column=1)

"""
Commands for ARP Rotation tab
"""

# Create labelframe for ARP control widgets
frame_arp_rotation = tk.LabelFrame(frame_equipment,
                                   text="ARP Rotation", padx=10, pady=10)
frame_arp_rotation.pack()

# Create label for ARP Base point
label_entry_arp_base = tk.Label(frame_arp_rotation, text="Base point:")
label_entry_arp_base.grid(row=0, column=0, sticky="e")

# Create entry widget for ARP Base point
entry_arp_base = tk.Entry(frame_arp_rotation, width=25)
entry_arp_base.grid(row=0, column=1)

# Create label for ARP Orientation point
label_entry_arp_orientation = tk.Label(frame_arp_rotation, text="Orientation point:")
label_entry_arp_orientation.grid(row=1, sticky="e")

# Create entry widget for ARP Orientation point
entry_arp_orientation = tk.Entry(frame_arp_rotation, width=25)
entry_arp_orientation.grid(row=1, column=1)

# Create label for ARP Rotation point
label_entry_arp_rotation = tk.Label(frame_arp_rotation, text="Rotation point:")
label_entry_arp_rotation.grid(row=2, sticky="e")

# Create entry widget for ARP Rotation point
entry_arp_rotation = tk.Entry(frame_arp_rotation, width=25)
entry_arp_rotation.grid(row=2, column=1)

# Add button for selecting values in ARP parameters Treeview
select_button_arp = tk.Button(frame_equipment, text="Select ARP",
                              command=lambda: select_arp(equipment_tree))
select_button_arp.pack(pady=5)


# Initialize mainloop for the root window
root.mainloop()
