import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\GeomProject\GeomProject.gdb"

# Create List of Geometry from Feature Class
geomList = arcpy.CopyFeatures_management("FishnetPolys", arcpy.Geometry())

area = 0.0

for geom in geomList:
    if area == 0.0:
        # get geometry spatial reference
        sr = geom.spatialReference
    # get geometry area    
    area += geom.area

print(f"Total area: {area}" )
print(f"Statial Reference: {sr.name}")

print("Script Copleted")

