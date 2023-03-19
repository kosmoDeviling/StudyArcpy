import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\Projects" \
                      r"\FrameworkProject" \
                      r"\FrameworkProject.gdb"

countryName = "India"

arcpy.analysis.Select(
    r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_admin_0_countries.shp",
    r"SelCountry",
    f"NAME = '{countryName}'"
)

arcpy.analysis.Buffer(
    "SelCountry",
    "SelCountry_Buffer",
    "200 Kilometers",
    "FULL",
    "ROUND",
    "NONE",
    None,
    "PLANAR"
)
arcpy.analysis.Clip(
    r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_populated_places.shp",
    "SelCountry_Buffer",
    "Places_Clip",
    None
)
print(
    f'There are {arcpy.management.GetCount("Places_Clip")} in or whithin '
    f'200km of {countryName}'
)
