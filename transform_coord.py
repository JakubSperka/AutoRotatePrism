import pyproj


def transform_4326(lon, lat):
    # Create a transformer from the source CRS to the target CRS
    from_epsg = 4326
    to_epsg = 5514
    transformer = pyproj.Transformer.from_crs(from_epsg, to_epsg, always_xy=True)

    # Transform the coordinates
    point_5514 = transformer.transform(lat, lon)

    return point_5514


def transform_5514(x, y):
    # Create a transformer from the source CRS to the target CRS
    from_epsg = 5514
    to_epsg = 4326
    transformer = pyproj.Transformer.from_crs(from_epsg, to_epsg, always_xy=True)

    # Transform the coordinates
    point_4326 = transformer.transform(x, y)

    return point_4326
