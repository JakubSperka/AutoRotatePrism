import numpy as np
from select_item import *


def calculate_angle():
    """
       Calculate the angle in degrees between the heading from a base point to an orientation point
       and the direction towards a rotation point, respecting tangent quadrants.

       Parameters:
       - base_point (DataFrame row): DataFrame row representing the base point with 'X' and 'Y' coordinates.
       - orientation_point (DataFrame row): DataFrame row representing the orientation point with
       'X' and 'Y' coordinates.
       - rotation_point (DataFrame row): DataFrame row representing the rotation point with 'X' and 'Y' coordinates.

       Returns:
       - angle_degrees (float): Angle in degrees from the orientation point to the rotation point
         relative to the base point.

       This function calculates the angle using vector mathematics and trigonometry.
       """

    # Extract coordinates of the points
    base_x = selected_base.get("X")
    base_y = selected_base.get("Y")
    orientation_x = selected_orientation.get("X")
    orientation_y = selected_orientation.get("Y")
    rotation_x = selected_rotation.get("X")
    rotation_y = selected_rotation.get("Y")

    print(base_x, base_y, orientation_x, orientation_y, rotation_x, rotation_y)

    # Vector from base point to orientation point
    vec_orientation = np.array([orientation_x - base_x, orientation_y - base_y])

    # Vector from base point to rotation point
    vec_rotation = np.array([rotation_x - base_x, rotation_y - base_y])

    # Calculate the angle between the vectors using dot product
    dot_product = np.dot(vec_orientation, vec_rotation)
    norm_orientation = np.linalg.norm(vec_orientation)
    norm_rotation = np.linalg.norm(vec_rotation)

    # Calculate the cosine of the angle using dot product formula
    cosine_angle = dot_product / (norm_orientation * norm_rotation)

    # Compute the angle in radians using arc cos
    angle_radians = np.arccos(cosine_angle)

    # Convert radians to degrees
    angle_degrees = np.degrees(angle_radians)

    print(f"Angle to target point: {angle_degrees} degrees")

    return angle_degrees
