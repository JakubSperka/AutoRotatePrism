import pyproj


def transform_4326(lon, lat):
    """
    Transform WGS84 (EPSG:4326) coordinates (longitude, latitude) to EPSG:5514 (a specific projected CRS).

    Parameters:
    lon (float): Longitude coordinate in decimal degrees.
    lat (float): Latitude coordinate in decimal degrees.

    Returns:
    tuple: Transformed coordinates in EPSG:5514 (x, y) format.
    """
    # Define the source and target EPSG codes
    from_epsg = 4326
    to_epsg = 5514

    # Create a transformer from the source CRS (WGS84) to the target CRS (EPSG:5514)
    transformer = pyproj.Transformer.from_crs(from_epsg, to_epsg, always_xy=True)

    # Transform the coordinates
    point_5514 = transformer.transform(lon, lat)

    return point_5514


def transform_5514(x, y):
    """
    Transform EPSG:5514 projected coordinates (x, y) to WGS84 (EPSG:4326) coordinates.

    Parameters:
    x (float): X coordinate in EPSG:5514.
    y (float): Y coordinate in EPSG:5514.

    Returns:
    tuple: Transformed coordinates in WGS84 (longitude, latitude) format.
    """
    # Define the source and target EPSG codes
    from_epsg = 5514
    to_epsg = 4326

    # Create a transformer from the source CRS (EPSG:5514) to the target CRS (WGS84)
    transformer = pyproj.Transformer.from_crs(from_epsg, to_epsg, always_xy=True)

    # Transform the coordinates
    point_4326 = transformer.transform(x, y)

    return point_4326


def transform(from_epsg, to_epsg, from_x, from_y):
    """
    Transforms coordinates from one Coordinate Reference System (CRS) to another.

    Parameters:
    - from_epsg (int): EPSG code of the source CRS.
    - to_epsg (int): EPSG code of the target CRS.
    - from_x (float): X coordinate in the source CRS.
    - from_y (float): Y coordinate in the source CRS.

    Returns:
    - tuple: Transformed coordinates (X, Y) in the target CRS.
    """
    # Create a transformer from the source CRS to the target CRS
    transformer = pyproj.Transformer.from_crs(from_epsg, to_epsg, always_xy=True)

    # Transform the coordinates
    point_target_crs = transformer.transform(from_x, from_y)

    return point_target_crs
