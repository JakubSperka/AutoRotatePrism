from transform_coord import *

# Global list to keep track of added markers
added_markers = []


def place_markers(tree_name, map_view, text_color, circle_color, outside_color):
    """
    Function to place markers on a map based on coordinates provided in a treeview.

    Parameters:
    - tree_name: The treeview containing coordinates (in a specific format) for markers.
    - map_view: The map view object where markers will be placed.
    - text_color: Color of the text displayed on the marker.
    - circle_color: Color of the circle part of the marker.
    - outside_color: Color of the outside part of the marker.

    This function retrieves coordinates from the treeview, transforms them if needed,
    and then places markers on the map_view accordingly.
    """
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

                # Transform coordinates from 5514 to 4326 (presumed EPSG 5514 to EPSG 4326)
                marker_4326 = transform_5514(marker_y_5514, marker_x_5514)

                # Set marker on map_view and store the marker object
                marker = map_view.set_marker(marker_4326[1], marker_4326[0], text=marker_id,
                                             text_color=text_color,
                                             marker_color_circle=circle_color,
                                             marker_color_outside=outside_color,
                                             font=("Consolas Bold", 10))
                added_markers.append(marker)  # Add the marker to the list
            else:
                print("Error: Incomplete values for item in treeview.")


def hide_markers():
    """
    Function to hide all previously added markers from the map_view.

    This function iterates through the list of added_markers and removes each marker
    from the map_view, effectively clearing the map of displayed markers.
    """
    global added_markers
    for marker in added_markers:
        marker.delete()  # Remove each marker from the map
    added_markers = []  # Clear the list of added markers
