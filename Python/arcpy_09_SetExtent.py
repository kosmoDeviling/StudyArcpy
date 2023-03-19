import arcpy

arcpy.env.overwriteOutput = True

# Set a workspace 
arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\EnvProject\Test.gdb"

# Copy/export Feature Class
arcpy.FeatureClassToFeatureClass_conversion(
    r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_admin_1_states_provinces.shp",
    r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\EnvProject\Test.gdb",
    "States"
)

print(arcpy.GetCount_management("States"))

arcpy.env.extent = "TrinidadTobago_EEZ"

arcpy.CopyFeatures_management(
    "States",
    "StatesInExtent"
)

print(arcpy.GetCount_management("StatesInExtent"))

print('\nScript Completed')
    