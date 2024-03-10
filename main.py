# Library import

import sys
import tkinter as tk
import tkinter.messagebox
import tkintermapview as tkmap
import numpy as np


# Main

root = tk.Tk()
root.title("ARP Control Panel v.1.0.0")

frame_map_control= tk.LabelFrame(root, text="Map Control",padx=100,pady=100)
frame_equipment = tk.LabelFrame(root, text="Equipment",padx=100,pady=100)
frame_network_points = tk.LabelFrame(root, text="Imported network points",padx=100,pady=100)
frame_temp_points = tk.LabelFrame(root, text="Temporary points",padx=100,pady=100)

frame_map_control.grid(row=0,column=0)
frame_equipment.grid(row=0,column=1)
frame_network_points.grid(row=1,column=0)
frame_temp_points.grid(row=2,column=0)


b1 = tk.Label(frame_equipment,text="Frame")
b2 = tk.Label(frame_equipment,text="Frame")
b3 = tk.Label(frame_network_points,text="Frame")
b4 = tk.Label(frame_temp_points,text="Frame")


b1.grid(row=0,column=0)
b2.grid(row=1,column=1)
b3.pack()
b4.pack()

root.mainloop()

