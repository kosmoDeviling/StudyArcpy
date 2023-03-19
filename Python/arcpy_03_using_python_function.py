import arcpy

def print_message(msg):
    print(msg)
    arcpy.AddMessage(msg)


arcpy.env.overwriteOutput = True

arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_admin_0_countries.shp"

fc = arcpy.GetParameterAsText(0)
if fc == "":
    fc = r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_admin_0_countries.shp"

numFeats = arcpy.GetCount_management(fc)

print_message("{0} has {1} feature(s)".format(fc, numFeats))

print_message("Script completed!")
