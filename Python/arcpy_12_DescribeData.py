import arcpy

# Describing a Folder
dataElelement = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA'
desc =arcpy.Describe(dataElelement)
print(f"Describing    {dataElelement}")
print(f"Name:         {desc.name}" )
print(f"DataType:     {desc.dataType}" )
print(f"catalogPath:  {desc.catalogPath}" )

print()
# Describing a GDB
dataElelement2 = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample2.gdb'
desc2 =arcpy.Describe(dataElelement2)
print(f"Describing    {dataElelement2}")
print(f"Name:         {desc2.name}" )
print(f"DataType:     {desc2.dataType}" )
print(f"catalogPath:  {desc2.catalogPath}" )
print('Children:')
for child in desc2.children:
    print(f"{child.name} is a {child.dataType}")

print()
# Describing a Feature Dataset
dataElelement3 = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample2.gdb\NaturalEarth'
desc3 =arcpy.Describe(dataElelement3)
print(f"Describing    {dataElelement3}")
print(f"Name:         {desc3.name}" )
print(f"DataType:     {desc3.dataType}" )
print(f"catalogPath:  {desc3.catalogPath}" )
print('Children:')
for child in desc3.children:
    print(f"{child.name} is a {child.dataType}")

print()
# Describing  a Feature Class
dataElelement4 = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample2.gdb\NaturalEarth\ne_10m_railroads'
desc4 =arcpy.Describe(dataElelement4)
print(f"Describing    {dataElelement4}")
print(f"Name:         {desc4.name}" )
print(f"DataType:     {desc4.dataType}" )
print(f"catalogPath:  {desc4.catalogPath}" )
print('Children:')
for child in desc4.children:
    print(f"{child.name} is a {child.dataType}")
    
print()
# Describing  a Feature Class and its shapeType, Extent, Fields
dataElelement5 = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample2.gdb\NaturalEarth'
desc5 =arcpy.Describe(dataElelement5)
print(f"Describing    {dataElelement5}")
print(f"Name:         {desc5.name}" )
print(f"DataType:     {desc5.dataType}" )
print(f"catalogPath:  {desc5.catalogPath}" )
print('Children:')
for child in desc5.children:
    print(f"               {child.name} is a {child.dataType} of shapeType {child.shapeType}")
    print(f"with Extent:   {child.extent}")
    print("and Fields:")
    for field in child.fields:
        print(f"                {field.name} of type {field.type}")
    
print('\nScript Completed')
    
print()
# Describing  a GDB data and its shapeType, Extent, Fields
dataElelement6 = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\Sample2.gdb'
desc6 =arcpy.Describe(dataElelement6)
print(f"Describing    {dataElelement6}")
print(f"Name:         {desc6.name}" )
print(f"DataType:     {desc6.dataType}" )
print(f"catalogPath:  {desc6.catalogPath}" )
print('Children:')
for child in desc6.children:
    if child.dataType == 'FeatureDataset':
        pass
    elif hasattr(child,"shapeType"):
        print(f"               {child.name} is a {child.dataType} of shapeType {child.shapeType}")
        print(f"with Extent:   {child.extent}")
    else:
        print(f"               {child.name} is a {child.dataType}")
        print("and Fields:")
        for field in child.fields:
            print(f"                {field.name} of type {field.type}")
    
print('\nScript Completed')
    