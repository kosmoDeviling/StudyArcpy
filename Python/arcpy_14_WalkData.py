import arcpy

# workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data"
workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\LPA"

dataList = []
for dirpath, dirnames, filenames in arcpy.da.Walk(workspace):
    for filename in filenames:
        dataList.append(rf"{dirpath}\{dirnames}")
print(dataList)

print(f"\nFound {len(dataList)} data elements in {workspace}")

for dirpath, dirnames, filenames in arcpy.da.Walk(
    workspace,
    type=["Point", "Polyline"]
    # datatype = "RaserDataset",
    # type = ["JPG", "PNG", "TIF"]
):
    for filename in filenames:
        dataList.append(rf"{dirpath}\{dirnames}")
print(dataList)

print(f"\nFound {len(dataList)} data elements in {workspace}")

print("\nScript completed!")

    