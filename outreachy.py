from osm_fieldwork.basemapper import create_basemap_file
from io import BytesIO

with open(r"D:\Opensource\osm-fieldwork\tests\testdata\Rollinsville.geojson", "rb") as geojson_file:
    boundary = geojson_file.read()
    boundary_bytesio = BytesIO(boundary)  # add to the BytesIO wrapper

create_basemap_file(
    verbose=True,
    boundary=boundary_bytesio,
    outfile="outreachy.mbtiles",
    zooms="12-15",
    source="esri",
)