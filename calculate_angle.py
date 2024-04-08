import numpy as np
import pandas as pd


def calculate_angle(selected_base, selected_orientation, selected_rotation):
    """
    Calculate the clockwise angle in degrees from the orientation point to the rotation point
    relative to the base point.

    Parameters:
    - selected_base (DataFrame row): DataFrame row representing the base point with 'X' and 'Y' coordinates.
    - selected_orientation (DataFrame row): DataFrame row representing the orientation point with
      'X' and 'Y' coordinates.
    - selected_rotation (DataFrame row): DataFrame row representing the rotation point with 'X' and 'Y' coordinates.

    Returns:
    - clockwise_angle_degrees (float): Clockwise angle in degrees from the orientation point to the rotation point
      relative to the base point.
    """

    # Extract coordinates from DataFrame rows and convert to numeric type
    try:
        base_x = pd.to_numeric(selected_base["X"].iloc[0])
        base_y = pd.to_numeric(selected_base["Y"].iloc[0])
        orientation_x = pd.to_numeric(selected_orientation["X"].iloc[0])
        orientation_y = pd.to_numeric(selected_orientation["Y"].iloc[0])
        rotation_x = pd.to_numeric(selected_rotation["X"].iloc[0])
        rotation_y = pd.to_numeric(selected_rotation["Y"].iloc[0])
    except (KeyError, ValueError):
        raise ValueError("DataFrame rows must contain numeric 'X' and 'Y' coordinates")

    # Vector from base point to orientation point
    vec_orientation = np.array([orientation_x - base_x, orientation_y - base_y])

    # Vector from base point to rotation point
    vec_rotation = np.array([rotation_x - base_x, rotation_y - base_y])

    # Calculate the angle between the vectors using cross product to determine direction
    cross_product = np.cross(vec_orientation, vec_rotation)

    # Calculate the dot product to determine the cosine of the angle
    dot_product = np.dot(vec_orientation, vec_rotation)
    norm_orientation = np.linalg.norm(vec_orientation)
    norm_rotation = np.linalg.norm(vec_rotation)

    # Calculate the cosine of the angle using dot product formula
    cosine_angle = dot_product / (norm_orientation * norm_rotation)

    # Determine the angle direction (clockwise or counterclockwise)
    if cross_product >= 0:
        # Clockwise direction
        angle_radians = np.arccos(cosine_angle)
    else:
        # Full circle (360 degrees) minus the counterclockwise angle
        angle_radians = 2 * np.pi - np.arccos(cosine_angle)

    # Convert radians to degrees
    clockwise_angle_degrees = np.degrees(angle_radians)

    print(f"Clockwise angle to target point: {clockwise_angle_degrees} degrees")

    return clockwise_angle_degrees
