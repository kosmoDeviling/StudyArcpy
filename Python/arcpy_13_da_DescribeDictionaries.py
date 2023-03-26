import arcpy

# dataElelement = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample.gdb'
dataElelement = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample.gdb\Countries'
descDictionary = arcpy.da.Describe(dataElelement)
# print(descDictionary)
for i,key in enumerate(descDictionary):
    print(f'{i+1}.{key}:{descDictionary[key]}')
    
print('\nScript Completed')
    