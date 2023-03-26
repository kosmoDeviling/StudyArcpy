import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\GeomProject\GeomProject.gdb"
srWGS84 = arcpy.SpatialReference("WGS 1984",)

# Create Point Objects
pt1 = arcpy.Point(2.5, 1.75)
pt2 = arcpy.Point(7.5, 1.25)
pt3 = arcpy.Point(2.75, 1.5)

# Create Point Geometries
ptGeom1 = arcpy.PointGeometry(pt1, srWGS84)
ptGeom2 = arcpy.PointGeometry(pt2, srWGS84)
ptGeom3 = arcpy.PointGeometry(pt3, srWGS84)

# Create new Point Feature 
arcpy.CopyFeatures_management([ptGeom1, ptGeom2, ptGeom3], "PtGeom")

# Create lit of coords
coodLists = [
    [(1.1, 2.4), (4.9, 2.6), (3.2, 7.3)],
    [(6.1, 8.8), (5.2, 7.6), (7.1, 2.3), (9.1, 5.3)]
]

multiPtGeom = []

for coordList in coodLists:
    multiPtGeom.append(
        # Create MultiPoint Geometry
        arcpy.Multipoint(
            arcpy.Array([arcpy.Point(*coords) for coords in coordList]),
            srWGS84
        )
    )

# Create new MultiPoint Feature
arcpy.CopyFeatures_management(multiPtGeom, "MultiPtGeom")

print('Script Copleted')
