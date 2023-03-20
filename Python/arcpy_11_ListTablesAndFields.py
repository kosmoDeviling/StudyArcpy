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

# List of Tables in GDB
for gdb in gdbListAll:
    arcpy.env.workspace = gdb
    print(f'\nTables in {gdb}:\n{arcpy.ListTables()}')

arcpy.env.workspace = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample.gdb'
for tbl in arcpy.ListTables():
    # Lst FieldObject in Teable
    fieldObjectList = arcpy.ListFields(tbl)
    # List Field Name in Table
    fieldNameList = [x.name for x in fieldObjectList]
    print(f'\nFields {arcpy.env.workspace}\{tbl}:\n{fieldNameList}')
    # List Filed Name and Type in Table
    fieldNameTypeList = [[x.name, x.type] for x in fieldObjectList]
    print(f'\nFields {arcpy.env.workspace}\{tbl}:\n{fieldNameTypeList}')
print('\nScript Completed')
    