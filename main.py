import tkinter as tk
from import_data import import_network


root = tk.Tk()
root.title("ARP Control Panel v.1.0.0")

frame_network_points = tk.LabelFrame(root, text="Imported network points", padx=100, pady=100)
frame_network_points.pack()

import_button = tk.Button(frame_network_points, text="Import Point Data", command=import_network)
import_button.pack(pady=20)

root.mainloop()


