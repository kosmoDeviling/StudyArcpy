# import the arcpy library
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample.gdb"

fc = r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_admin_0_countries.shp"
numFeats = arcpy.GetCount_management(fc)
print("{0} has {1} feature(s)".format(fc, numFeats))

arcpy.CreateFileGDB_management(r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data", "Sample")
arcpy.Select_analysis(fc, "Egypt", "NAME = 'Egypt'")

print("Script completed!")
