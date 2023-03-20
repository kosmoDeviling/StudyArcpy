import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\LPA"

gdbListAll =[]

# List of worspaces
wsList = arcpy.ListWorkspaces()

for w in wsList:
    arcpy.env.workspace = w
    # List of GDB
    gdbList = arcpy.ListWorkspaces("", "FileGDB")
    gdbListAll += gdbList

print(f"List of geodabases:\n{gdbListAll}")

for gdb in gdbListAll:
    arcpy.env.workspace = gdb
    # List Feauture Classes in GDB    
    print(f"\nFeature Classes in {gdb}:\n{arcpy.ListFeatureClasses()}")
    # List Feature Datasets in GDB
    print(f"\nFeature Datasets in {gdb}: \n{arcpy.ListDatasets('','Feature')}")
    fdList = arcpy.ListDatasets("", "Feature")
    for fd in fdList:
        arcpy.env.workspace = rf"{gdb}\{fd}"
        # List Feature Classes in Feature Dataset
        print(f'\nFeature Classes in featrure dataset {fd}:\n{arcpy.ListFeatureClasses()}')

print('\nScript Completed')
    