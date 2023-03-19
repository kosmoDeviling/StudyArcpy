# import the arcpy library
import arcpy

# Set env for overwriting feature
arcpy.env.overwriteOutput = True
# Set the env default GDB
arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample.gdb"
# pointer to a shp file
fc = r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_admin_0_countries.shp"
numFeats = arcpy.GetCount_management(fc)
print("{0} has {1} feature(s)".format(fc, numFeats))
# Create a new GDB
arcpy.CreateFileGDB_management(
    r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data", "Sample")
arcpy.Select_analysis(fc, "Egypt", "NAME = 'Egypt'")

print("Script completed!")
