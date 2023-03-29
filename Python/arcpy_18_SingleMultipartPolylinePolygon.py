import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\GeomProject\GeomProject.gdb"
srWGS84 = arcpy.SpatialReference("WGS 1984",)

# Create lit of coords
coodLists = [
    [(1.1, 2.4), (4.9, 2.6), (3.2, 7.3)],
    [(6.1, 8.8), (5.2, 7.6), (7.1, 2.3), (9.1, 5.3)]
]

polylineGeom = []

for coordList in coodLists:
    polylineGeom.append(
        # Create Polyline Geometry
        arcpy.Polyline(
            arcpy.Array([arcpy.Point(*coords) for coords in coordList]),
            srWGS84
        )
    )

# Create new Polyline Feature
arcpy.CopyFeatures_management(polylineGeom, "PolylineGeom")

polylygonGeom = []

for coordList in coodLists:
    polylygonGeom.append(
        # Create Polygon Geometry
        arcpy.Polygon(
            arcpy.Array([arcpy.Point(*coords) for coords in coordList]),
            srWGS84
        )
    )

# Create new Polyline Feature
arcpy.CopyFeatures_management(polylygonGeom, "PolygonGeom")

arrayList = []

for coordList in coodLists:
    arrayList.append(
            arcpy.Array([arcpy.Point(*coords) for coords in coordList])
    )

# Create Multipart Polygon
multiPartPolyGeom = arcpy.Polygon(
    arcpy.Array(arrayList), 
    srWGS84
)

# Create new Multipart Polygon Feature
arcpy.CopyFeatures_management(multiPartPolyGeom, "MultiPartPolyGeom")

arrayList = []

for coordList in coodLists:
    arrayList.append(
            arcpy.Array([arcpy.Point(*coords) for coords in coordList])
    )

# Create Multipart Polyline
multiPartLineGeom = arcpy.Polyline(
    arcpy.Array(arrayList),
    srWGS84
)

# Create new Multipart Polyline Feature
arcpy.CopyFeatures_management(multiPartLineGeom, "multiPartLineGeom")

print('Script Copleted')
