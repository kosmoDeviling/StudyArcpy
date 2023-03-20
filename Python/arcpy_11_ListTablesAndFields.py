import arcpy

arcpy.env.workspace = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample2.gdb'
for tbl in arcpy.ListTables():
    # Lst FieldObject in Teable
    fieldObjectList = arcpy.ListFields(tbl)
    print(f'\nfieldObjectList')
    # List Field Name in Table
    fieldNameList = [x.name for x in fieldObjectList]
    print(f'\nFields {arcpy.env.workspace}\{tbl}:\n{fieldNameList}')
    # List Filed Name and Type in Table
    fieldNameTypeList = [[x.name, x.type] for x in fieldObjectList]
    print(f'\nFields {arcpy.env.workspace}\{tbl}:\n{fieldNameTypeList}')
print('\nScript Completed')
    