import tkinter as tk
from transform_coord import *


def pick_temp_point_event(coords, entry_field):
    picked_coords = coords
    tsf_coords = transform_4326(picked_coords[1], picked_coords[0])
    entry_field.delete(0, tk.END)
    entry_field.insert(0, f"{tsf_coords[1]:.3f} {tsf_coords[0]:.3f}")
