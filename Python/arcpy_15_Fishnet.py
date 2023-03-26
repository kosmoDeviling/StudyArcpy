import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\GeomProject\GeomProject.gdb"
# Create a spatial refernce variable from spatial reference object
srWGS84 = arcpy.SpatialReference("WGS 1984",)

# Create a fishnet Lines
arcpy.management.CreateFishnet(
    "FishnetLines",
    "0 0", 
    "0 10", 
    1, 
    1, 
    10, 
    15, 
    None, 
    "LABELS", 
    None, 
    "POLYLINE"
)

if arcpy.Exists("FishnetPoints"):
    arcpy.Delete_management("FishnetPoints")

# Rename Feature Class
arcpy.Rename_management("FishnetLines_label", "FishnetPoints")

# Create Fishnet Polygon
arcpy.management.CreateFishnet(
    "FishnetPolys",
    "0 0", 
    "0 1", 
    1, 
    1, 
    4, 
    6, 
    None, 
    "NO_LABELS", 
    None, 
    "POLYGON"
)

# Define Projection for Feature Class
for gomType in ["Polys", "Lines", 'Points']:
    arcpy.management.DefineProjection(
        f"Fishnet{gomType}", 
        srWGS84
    )

print("Script Complete")