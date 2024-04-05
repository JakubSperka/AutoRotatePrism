import pandas as pd
import pyproj

point_5514 = pd.DataFrame()


def transform_4326(lon, lat):
    # Create a transformer from the source CRS to the target CRS
    from_epsg = 4326
    to_epsg = 5514
    transformer = pyproj.Transformer.from_crs(from_epsg, to_epsg, always_xy=True)

    # Transform the coordinates
    global point_5514
    point_5514 = transformer.transform(lat, lon)

    return point_5514
