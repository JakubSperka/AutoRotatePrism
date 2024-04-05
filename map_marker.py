from transform_coord import *

# Global list to keep track of added markers
added_markers = []


def place_markers(tree_name, map_view):
    items = tree_name.get_children()

    if not items:
        print("Error: No points in Network Points imported.")
    else:
        for item in items:
            values = tree_name.item(item)['values']

            if values:
                marker_id = values[0]
                marker_x_5514 = values[1]
                marker_y_5514 = values[2]

                # Transform coordinates to 4326
                marker_4326 = transform_5514(marker_y_5514, marker_x_5514)

                # Set marker on map_view and store the marker object
                marker = map_view.set_marker(marker_4326[1], marker_4326[0], text=marker_id)
                added_markers.append(marker)  # Add the marker to the list
            else:
                print("Error: Incomplete values for item in treeview.")


def hide_markers():
    global added_markers
    for marker in added_markers:
        marker.delete()  # Remove each marker from the map
    added_markers = []  # Clear the list of added markers



