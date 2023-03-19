import arcpy

arcpy.env.overwriteOutput = True

# if arcpy.Exists("D:\00-Learning\02-GisDev\01-ArcPy\Projects\EnvProject\test.gdb"):
#     arcpy.Delete_management("D:\00-Learning\02-GisDev\01-ArcPy\Projects\EnvProject\test.gdb")

arcpy.CreateFileGDB_management(r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\EnvProject","Test.gdb")

print('\nScript Completed')
    