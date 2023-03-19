import arcpy

arcpy.env.overwriteOutput = True

print(arcpy.env.workspace)
# Set a workspace 
arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\EnvProject\Test.gdb"

print(arcpy.env.workspace)

# Copy/export Feature Class
arcpy.FeatureClassToFeatureClass_conversion(
    r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_admin_0_countries.shp",
    r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\EnvProject\Test.gdb",
    "Countries"
)

# Select 
arcpy.Select_analysis("Countries", "TrinidadTobago", "NAME = 'Trinidad and Tobago'")
print(arcpy.Exists("TrinidadTobago"))

# Check if a FC exists
print(arcpy.Exists(r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\EnvProject\Test.gdb\Countries"))

arcpy.Buffer_analysis(
    "TrinidadTobago", 
    "TrinidadTobago_EEZ",
    "200 NauticalMiles",
    method="GEODESIC"
)
print(arcpy.Exists(r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\EnvProject\Test.gdb\TrinidadTobago_EEZ"))

print('\nScript Completed')
    