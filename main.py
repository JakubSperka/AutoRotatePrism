"""
Main program for APR Control panel GUI
"""

# Imported packages
import tkintermapview as tkmap
from tkinter import ttk
from import_data import *
from select_item import *
from center_mapview import *
from map_marker import *
from create_point import *
from map_click_events import *


# Set root GUI window
root = tk.Tk()
root.title("ARP Control Panel v.1.0.4 \"Celestial Dawn\"")
root.iconbitmap("compass.ico")
root.resizable(False, False)


"""
Commands for Map view tab
"""
frame_map_view = tk.LabelFrame(root, text="Map view", padx=10, pady=10)
frame_map_view.grid(row=0, column=0, rowspan=2, sticky="n")

map_server = tk.StringVar(value="https://ortofoto.tiles.freemap.sk/{z}/{x}/{y}.jpg")
map_view = tkmap.TkinterMapView(frame_map_view, width=570, height=595, corner_radius=0)
map_view.set_position(48.7284587, 19.1416669)
map_view.set_zoom(13)
map_view.set_tile_server(map_server.get(), max_zoom=19)
map_view.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

map_view.add_right_click_menu_command(label="Get coordinates",
                                      command=lambda coords: pick_temp_point_event(coords, entry_create_point_coord),
                                      pass_coords=True)

map_view.add_left_click_map_command(lambda coords: pick_temp_point_event(coords, entry_create_point_coord))

frame_map_view_buttons = tk.LabelFrame(frame_map_view, text="Center map view", padx=2, pady=2)
frame_map_view_buttons.grid(row=1, column=0, pady=5, padx=5, sticky="w")

zoom_to_network_point = tk.Button(frame_map_view_buttons, text="Center to network point",
                                  command=lambda: center_mapview(network_tree, map_view))
zoom_to_network_point.grid(row=0, column=0, pady=5, padx=5)

zoom_to_temp_point = tk.Button(frame_map_view_buttons, text="Center to temporary point",
                               command=lambda: center_mapview(temp_tree, map_view))
zoom_to_temp_point.grid(row=0, column=1, pady=5, padx=5)

frame_marker_buttons = tk.LabelFrame(frame_map_view, text="Map markers & ARP config", padx=2, pady=2)
frame_marker_buttons.grid(row=2, column=0, pady=5, padx=5, sticky="w")

show_marker_network = tk.Button(frame_marker_buttons, text="Show Network points",
                                command=lambda: place_markers(network_tree, map_view, "red",
                                                              "grey", "red"))
show_marker_network.grid(row=0, column=0, pady=5, padx=5)

show_marker_temp = tk.Button(frame_marker_buttons, text="Show Temporary points",
                             command=lambda: place_markers(temp_tree, map_view, "yellow",
                                                           "grey", "yellow"))
show_marker_temp.grid(row=0, column=1, pady=5, padx=5)

hide_marker = tk.Button(frame_marker_buttons, text="Hide markers",
                        command=lambda: hide_markers(), bg="darkgray")
hide_marker.grid(row=0, column=2, pady=5, padx=5)

show_marker_network = tk.Button(frame_marker_buttons, text="Show Orientation",
                                command=lambda: place_orientation(map_view), width=16)
show_marker_network.grid(row=1, column=0, pady=5, padx=5, sticky="w")

show_marker_temp = tk.Button(frame_marker_buttons, text="Show Target",
                             command=lambda: place_rotation(map_view), width=18)
show_marker_temp.grid(row=1, column=1, pady=5, padx=5, sticky="w")

hide_marker = tk.Button(frame_marker_buttons, text="Hide config",
                        bg="darkgray", command=lambda: hide_paths(), width=10)
hide_marker.grid(row=1, column=2, pady=5, padx=5, sticky="w")

frame_create_point = tk.LabelFrame(frame_map_view, text="Create temporary point", padx=2, pady=2)
frame_create_point.grid(row=3, column=0, pady=5, padx=5, sticky="w")

label_create_point_id = tk.Label(frame_create_point, text="Point ID:")
label_create_point_id.grid(row=0, column=0, sticky="e")

entry_create_point_id = tk.Entry(frame_create_point, width=30)
entry_create_point_id.grid(row=0, column=1, sticky="w", padx=5)

label_create_point_coord = tk.Label(frame_create_point, text="Coordinates:")
label_create_point_coord.grid(row=1, column=0, sticky="e")

entry_create_point_coord = tk.Entry(frame_create_point, width=30)
entry_create_point_coord.grid(row=1, column=1, sticky="w", padx=5)

label_create_point_code = tk.Label(frame_create_point, text="Survey code:")
label_create_point_code.grid(row=2, column=0, sticky="e")

entry_create_point_code = tk.Entry(frame_create_point, width=30)
entry_create_point_code.grid(row=2, column=1, sticky="w", padx=5)

# Add button for importing network points
create_point_button = tk.Button(frame_create_point, text="Create temporary point",
                                command=lambda: create_point(entry_create_point_id,
                                                             entry_create_point_coord,
                                                             entry_create_point_code,
                                                             temp_tree))
create_point_button.grid(row=3, column=0, columnspan=2, pady=5, padx=5)

frame_map_server = tk.LabelFrame(frame_map_view, text="Select base map")
frame_map_server.grid(row=1, column=1, rowspan=3, pady=5, padx=5, sticky="ne")

map_ugkk = tk.Radiobutton(frame_map_server, text="Ortho ÚGKK", variable=map_server,
                          value="https://ortofoto.tiles.freemap.sk/{z}/{x}/{y}.jpg")
map_ugkk.pack(anchor="w")
map_oms = tk.Radiobutton(frame_map_server, text="OpenStreetMap", variable=map_server,
                         value="https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
map_oms.pack(anchor="w")
map_google_normal = tk.Radiobutton(frame_map_server, text="Google Maps", variable=map_server,
                                   value="https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
map_google_normal.pack(anchor="w")
map_google_satellite = tk.Radiobutton(frame_map_server, text="Google Satellite", variable=map_server,
                                      value="https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga")
map_google_satellite.pack(anchor="w")
map_google_hybrid = tk.Radiobutton(frame_map_server, text="Google Hybrid", variable=map_server,
                                   value="https://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}")
map_google_hybrid.pack(anchor="w")

map_google_hybrid = tk.Radiobutton(frame_map_server, text="Freemap Outdoor", variable=map_server,
                                   value="https://outdoor.tiles.freemap.sk/{z}/{x}/{y}.jpg")
map_google_hybrid.pack(anchor="w")

map_refresh_button = tk.Button(frame_map_server, text="Refresh base map",
                               command=lambda: map_view.set_tile_server(map_server.get(), max_zoom=19))
map_refresh_button.pack(pady=5, padx=5)

"""
Commands for Network points tab
"""
# Create a frame for trees
frame_points = tk.Frame(root)
frame_points.grid(row=0, column=1, sticky="n")

# Create a frame for imported network points
frame_network_points = tk.LabelFrame(frame_points, text="Imported network points", padx=10, pady=10)
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
network_tree.heading("ID", text="Point ID", anchor="w")
network_tree.heading("X", text="X [m]", anchor="w")
network_tree.heading("Y", text="Y [m]", anchor="w")
network_tree.heading("H", text="H [m]", anchor="w")
network_tree.heading("Code", text="Survey code", anchor="w")

network_tree.column("ID", anchor="w", width=110)
network_tree.column("X", anchor="w", width=110)
network_tree.column("Y", anchor="w", width=110)
network_tree.column("H", anchor="w", width=110)
network_tree.column("Code", anchor="w", width=110)

frame_network_points_buttons = tk.Frame(frame_network_points)
frame_network_points_buttons.pack(anchor="w")

# Add button for importing network points
import_button_network = tk.Button(frame_network_points_buttons, text="Import geodetic network points",
                                  command=lambda: import_network(network_tree))
import_button_network.grid(row=0, column=0, pady=5, padx=5)

delete_button_network = tk.Button(frame_network_points_buttons, text="Delete selected point",
                                  command=lambda: delete_point(network_tree), bg="red", fg="white")
delete_button_network.grid(row=0, column=1, pady=5, padx=5)


"""
Commands for Temp points tab
"""
# Create a frame for imported temp points
frame_temp_points = tk.LabelFrame(frame_points, text="Imported temporary points", padx=10, pady=10)
frame_temp_points.pack()

# Create a frame for temp points Treeview
treeview_frame_temp_points = tk.Frame(frame_temp_points)
treeview_frame_temp_points.pack()

# Create a scrollbar for network points Treeview
temp_tree_scrollbar = tk.Scrollbar(treeview_frame_temp_points)
temp_tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Treeview widget for imported network points
temp_tree = ttk.Treeview(treeview_frame_temp_points, columns=["ID", "X", "Y", "H", "Code"],
                         show="headings", selectmode="browse", yscrollcommand=temp_tree_scrollbar.set, height=5)
temp_tree.pack()

# Config scrollbar for network points Treeview
temp_tree_scrollbar.config(command=temp_tree.yview)

# Add columns to the Treeview for imported network points
temp_tree.heading("ID", text="Point ID", anchor="w")
temp_tree.heading("X", text="X [m]", anchor="w")
temp_tree.heading("Y", text="Y [m]", anchor="w")
temp_tree.heading("H", text="H [m]", anchor="w")
temp_tree.heading("Code", text="Survey code", anchor="w")

temp_tree.column("ID", anchor="w", width=110)
temp_tree.column("X", anchor="w", width=110)
temp_tree.column("Y", anchor="w", width=110)
temp_tree.column("H", anchor="w", width=110)
temp_tree.column("Code", anchor="w", width=110)

frame_temp_points_buttons = tk.Frame(frame_temp_points)
frame_temp_points_buttons.pack(anchor="w")

# Add button for importing network points
import_button_temp = tk.Button(frame_temp_points_buttons, text="Import temporary points",
                               command=lambda: import_temp(temp_tree))
import_button_temp.grid(row=0, column=0, pady=5, padx=5)

delete_button_temp = tk.Button(frame_temp_points_buttons, text="Delete selected point",
                               command=lambda: delete_point(temp_tree), bg="red", fg="white")
delete_button_temp.grid(row=0, column=1, pady=5, padx=5)

"""
Commands for Equipment tab
"""

# Create a frame for equipment tab
frame_equipment = tk.LabelFrame(frame_points, text="Equipment", padx=10, pady=10)
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
                              yscrollcommand=equipment_tree_scrollbar.set, height=3)
equipment_tree.pack()

# Config scrollbar for equipment Treeview
equipment_tree_scrollbar.config(command=equipment_tree.yview)

# Add columns to the Treeview for equipment
equipment_tree.heading("ARP_ID", text="ARP ID", anchor="w")
equipment_tree.heading("Auth_token", text="Authentication token", anchor="w")
equipment_tree.heading("Prism_height", text="Target height [m]", anchor="w")
equipment_tree.heading("Prism_constant", text="Prism constant [mm]", anchor="w")

equipment_tree.column("ARP_ID", anchor="w", width=55)
equipment_tree.column("Auth_token", anchor="w", width=235)
equipment_tree.column("Prism_height", anchor="w", width=130)
equipment_tree.column("Prism_constant", anchor="w", width=130)

frame_equipment_buttons = tk.Frame(frame_equipment)
frame_equipment_buttons.pack(anchor="w")

# Add button for importing network points
import_button_arps = tk.Button(frame_equipment_buttons, text="Import ARP parameters",
                               command=lambda: import_arp(equipment_tree))
import_button_arps.grid(row=0, column=0, pady=5, padx=5)

delete_button_arp = tk.Button(frame_equipment_buttons, text="Delete selected ARP",
                              command=lambda: delete_point(equipment_tree), bg="red", fg="white")
delete_button_arp.grid(row=0, column=1, pady=5, padx=5)


"""
Commands for ARP Status tab
"""
frame_arp_control = tk.LabelFrame(frame_points, text="Status and control", padx=30, pady=5)
frame_arp_control.pack()

# Create labelframe for ARP control widgets
frame_arp_status = tk.LabelFrame(frame_arp_control,
                                 text="ARP Status & Orientation", padx=5, pady=5)
frame_arp_status.grid(row=0, column=0, pady=5, padx=5, sticky="nw")

# Create label for ARP ID entry widgets
label_entry_arp_id = tk.Label(frame_arp_status, text="ARP ID:")
label_entry_arp_id.grid(row=0, column=0, sticky="e")

# Create entry widget for ARP ID
entry_arp_id = tk.Entry(frame_arp_status, width=40)
entry_arp_id.grid(row=0, column=1, sticky="w")

# Create label for ARP auth token entry widgets
label_entry_arp_auth_token = tk.Label(frame_arp_status, text="Auth. Token:")
label_entry_arp_auth_token.grid(row=1, column=0, sticky="e")

# Create entry widget for ARP auth token
entry_arp_auth_token = tk.Entry(frame_arp_status, width=40)
entry_arp_auth_token.grid(row=1, column=1, sticky="w")

# Create label for ARP Status entry widgets
label_entry_arp_status = tk.Label(frame_arp_status, text="Status:")
label_entry_arp_status.grid(row=2, column=0, sticky="e")

# Create entry widget for ARP Status
entry_arp_status = tk.Entry(frame_arp_status, width=40)
entry_arp_status.grid(row=2, column=1, sticky="w")

frame_environment = tk.LabelFrame(frame_arp_status, text="Environment", padx=5, pady=5)
frame_environment.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)

# Create label for ARP Status entry widgets
label_entry_arp_env_temp = tk.Label(frame_environment, text="Temperature:")
label_entry_arp_env_temp.grid(row=0, column=0, sticky="e")

# Create entry widget for ARP Status
entry_arp_env_temp = tk.Entry(frame_environment, width=15)
entry_arp_env_temp.grid(row=0, column=1, sticky="w")

# Create label for ARP Status entry widgets
label_entry_arp_env_humid = tk.Label(frame_environment, text="Humidity:")
label_entry_arp_env_humid.grid(row=1, column=0, sticky="e")

# Create entry widget for ARP Status
entry_arp_env_humid = tk.Entry(frame_environment, width=15)
entry_arp_env_humid.grid(row=1, column=1, sticky="w")

# Add button for selecting values in ARP parameters Treeview
select_button_arp = tk.Button(frame_arp_status, text="Select ARP", width=42,
                              command=lambda: select_arp(equipment_tree, entry_arp_id, entry_arp_auth_token,
                                                         entry_arp_status, entry_arp_env_temp, entry_arp_env_humid))
select_button_arp.grid(row=4, column=0, columnspan=2, pady=5, padx=5)

"""
Commands for ARP Rotation tab
"""

# Create labelframe for ARP control widgets
frame_arp_rotation = tk.LabelFrame(frame_arp_control,
                                   text="Control points", padx=5, pady=5)
frame_arp_rotation.grid(row=0, column=1, columnspan=2, pady=5, padx=5, sticky="w")

# Create label for ARP Base point
label_entry_arp_base = tk.Label(frame_arp_rotation, text="Base point:")
label_entry_arp_base.grid(row=0, column=0, sticky="e")

# Create entry widget for ARP Base point
entry_arp_base = tk.Entry(frame_arp_rotation, width=10)
entry_arp_base.grid(row=0, column=1)

# Create label for ARP Orientation point
label_entry_arp_orientation = tk.Label(frame_arp_rotation, text="Orientation point:")
label_entry_arp_orientation.grid(row=1, sticky="e")

# Create entry widget for ARP Orientation point
entry_arp_orientation = tk.Entry(frame_arp_rotation, width=10)
entry_arp_orientation.grid(row=1, column=1)

# Create label for ARP Rotation point
label_entry_arp_rotation = tk.Label(frame_arp_rotation, text="Rotation point:")
label_entry_arp_rotation.grid(row=2, sticky="e")

# Create entry widget for ARP Rotation point
entry_arp_rotation = tk.Entry(frame_arp_rotation, width=10)
entry_arp_rotation.grid(row=2, column=1)

# Frame for ARP control buttons
frame_arp_buttons = tk.Frame(frame_arp_status)
frame_arp_buttons.grid(row=5, column=0, columnspan=5)

# Add button for selecting Base point in Network points Treeview
select_button_base = tk.Button(frame_arp_buttons, text="Select Base point", width=20,
                               command=lambda: select_base(network_tree if var_tree.get() == "network_tree"
                                                           else temp_tree, entry_arp_base))
select_button_base.grid(row=0, column=1, pady=1, padx=4)

# Add button for selecting orientation point in Network points Treeview
select_button_orientation = tk.Button(frame_arp_buttons, text="Select Orientation point", width=19,
                                      command=lambda: select_orientation(network_tree if
                                                                         var_tree.get() == "network_tree"
                                                                         else temp_tree, entry_arp_orientation))
select_button_orientation.grid(row=0, column=2, pady=1, padx=4)

frame_rotation = tk.LabelFrame(frame_arp_rotation, text="Target selection")
frame_rotation.grid(row=3, column=0, columnspan=2, pady=5, padx=5, sticky="w")

# Add button for selecting rotation point in temp points Treeview
select_button_rotation = tk.Button(frame_rotation, text="Select Rotation point",
                                   command=lambda: select_rotation(network_tree if var_tree.get() == "network_tree"
                                                                   else temp_tree, entry_arp_rotation))
select_button_rotation.grid(row=0, column=0, pady=5, padx=5)

frame_selection = tk.LabelFrame(frame_arp_rotation, text="Select from")
frame_selection.grid(row=4, column=0, columnspan=2, pady=5, padx=5, sticky="w")

var_tree = tk.StringVar(value="network_tree")
selection_network = tk.Radiobutton(frame_selection, text="Network points", variable=var_tree, value="network_tree")
selection_network.pack(anchor="w")
selection_temp = tk.Radiobutton(frame_selection, text="Temporary points", variable=var_tree, value="temp_tree")
selection_temp.pack(anchor="w")

frame_movement = tk.LabelFrame(frame_arp_control, text="ARP Movement")
frame_movement.grid(row=2, column=0, pady=5, padx=5, sticky="nw")

# Add button for calculate heading and rotate
button_rotate = tk.Button(frame_movement, text="Rotate ARP", height=2, width=30, bg="forestgreen", fg="white",
                          command=lambda: update_angle(entry_rotation_status))
button_rotate.grid(row=0, column=0, pady=5, padx=5)

# Add button for reset rotation
button_reset = tk.Button(frame_movement, text="Reset rotation", height=2, bg="darkorange", fg="white",
                         command=lambda: reset_angle(entry_rotation_status))
button_reset.grid(row=0, column=1, pady=5, padx=5)

# Add button for ARP lock
# button_lock = tk.Button(frame_movement, text="Lock ARP", height=2,
#                         command=lambda: lock_stepper(entry_rotation_status))
# button_lock.grid(row=0, column=2, pady=5, padx=5)


frame_movement_entry = tk.Frame(frame_movement)
frame_movement_entry.grid(row=1, column=0, columnspan=2, pady=5, padx=5, sticky="w")

# Create label for ARP Status entry widgets
label_entry_rotation_status = tk.Label(frame_movement_entry, text="Status:")
label_entry_rotation_status.grid(row=0, column=0, sticky="e")

# Create entry widget for ARP Status
entry_rotation_status = tk.Entry(frame_movement_entry, width=45)
entry_rotation_status.grid(row=0, column=1, sticky="w")


# Initialize mainloop for the root window
root.mainloop()
