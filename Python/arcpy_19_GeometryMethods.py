import arcpy
from pathlib import Path

arcpy.env.overwriteOutput = True
arcpy.env.workspace =r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\GeomProject\GeomProject.gdb"
srWGS84 = arcpy.SpatialReference("WGS 1984")
pt1 = arcpy.Point(2.5, 1.75)
ptGeom = arcpy.PointGeometry(pt1, srWGS84)

# Create lit of coords
coodLists = [
    [(1.1, 2.4), (4.9, 2.6), (3.2, 7.3)],
    [(6.1, 8.8), (5.2, 7.6), (7.1, 2.3), (9.1, 5.3)]
]

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

# Create Multipart Polygon
multiPartPolyGeom = arcpy.Polygon(
    arcpy.Array(arrayList), 
    srWGS84
)

# Create new Multipart Polygon Feature
arcpy.CopyFeatures_management(multiPartPolyGeom, "MultiPartPolyGeom")

# Buffer a multipart Geometry
bufferGeom = multiPartLineGeom.buffer(0.5)
arcpy.CopyFeatures_management(bufferGeom, "BufferGeom")

# Convex Hull
convexHullGeom = multiPartPolyGeom.convexHull()
arcpy.CopyFeatures_management(convexHullGeom, "ConvexHullGeom")

# Circle from point as center
circleCenter = arcpy.Point(5,3)
circleCenterGeom = arcpy.PointGeometry(circleCenter, srWGS84)
# print(ptGeom.distanceTo(circleCenter))
circleGeom = circleCenterGeom.buffer(2.8)
arcpy.CopyFeatures_management(circleGeom, "circleGeom")

# Intersect 
intersectGeom =circleGeom.intersect(multiPartPolyGeom, 4)
arcpy.CopyFeatures_management(intersectGeom, "intersectGeom")

# Multipart to singlepart !!BUG in Arcpy!!
# intersectGeomList = []
# for i in range(0, intersectGeom.partCount):
#     intersectGeomList.append(
#         arcpy.Polygon(
#         # Array of vertices
#         arcpy.Array(intersectGeom.getPart(i)),
#         srWGS84
#         )
#     )
# arcpy.CopyFeatures_management(intersectGeomList, "intersectSinglePartGeom")

# Multipart to singlepart using the mangement method
arcpy.MultipartToSinglepart_management(intersectGeom,"intersectSinglePartGeom")

print('Script Copleted')