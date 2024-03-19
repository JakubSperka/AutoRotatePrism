# Main

import tkinter as tk
from tkinter import ttk
from import_data import import_network
from import_data import network_points

root = tk.Tk()
root.title("ARP Control Panel v.1.0.0")

frame_network_points = tk.LabelFrame(root, text="Imported network points", padx=100, pady=100)
frame_network_points.pack()

import_button = tk.Button(frame_network_points, text="Import Point Data", command=import_network)
import_button.pack(pady=20)

# Create a Treeview widget
tree = ttk.Treeview(frame_network_points, columns=["ID", "X", "Y", "H", "Code"], show="headings", selectmode="browse")

# Add columns to the Treeview
for col in ["ID", "X", "Y", "H", "Code"]:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

# Insert data into the Treeview
for index, row in network_points.iterrows():
    tree.insert("", "end", values=(row["ID"], row["X"], row["Y"], row["H"], row["Code"]))


# Pack the Treeview onto the window
tree.pack(pady=20)

root.mainloop()
