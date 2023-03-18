import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample.gdb"

fc = arcpy.GetParameterAsText(0)
numFeats = arcpy.GetCount_management(fc)
arcpy.AddMessage("{0} has {1} feature(s)".format(fc, numFeats))

print("Script completed!")
