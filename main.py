# Main

import tkinter as tk
from tkinter import ttk
from import_data import import_network

root = tk.Tk()
root.title("ARP Control Panel v.1.0.0")

# Create a frame
frame_network_points = tk.LabelFrame(root, text="Imported network points", padx=10, pady=10)
frame_network_points.pack()

# Create a Treeview widget
tree = ttk.Treeview(frame_network_points, columns=["ID", "X", "Y", "H", "Code"], show="headings", selectmode="browse")
tree.pack(pady=10)

# Add columns to the Treeview
for col in ["ID", "X", "Y", "H", "Code"]:
    tree.heading(col, text=col, anchor="w")
    tree.column(col, anchor="w", width=100)

import_button = tk.Button(frame_network_points, text="Import Point Data", command=lambda: import_network(tree))
import_button.pack(pady=5)

root.mainloop()
