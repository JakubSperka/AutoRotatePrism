import tkinter as tk


def pick_temp_point_event(coords, entry_field):
    picked_coords = coords
    entry_field.delete(0, tk.END)
    entry_field.insert(0, f"{picked_coords[0]:.7f} {picked_coords[1]:.7f}")
