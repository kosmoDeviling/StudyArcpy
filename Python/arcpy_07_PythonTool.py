# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [CountPlacesForCountry]


class CountPlacesForCountry(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Count Places For Country"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName = 'Country Name',
            name = 'Country_Name',
            datatype = "GPString",
            parameterType = 'Required',
            direction = 'Input'
        )

        shpFile = r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_admin_0_countries.shp'

        param0.filter.list = sorted(
            [row[0] for row in arcpy.da.SearchCursor(shpFile, "NAME")]
        )

        params = [param0]

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = r"D:\00-Learning\02-GisDev\01-ArcPy\Projects\FrameworkProject\FrameworkProject.gdb"
        countryName = parameters[0].valueAsText
        arcpy.analysis.Select(
            r'D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_admin_0_countries.shp',
            "SelCountry",
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
            r"D:\00-Learning\02-GisDev\01-ArcPy\LPA\Data\ne_10m_populated_places.shp"
            "SelCountry_Buffer",
            "Places_Clip",
            None
        )
        arcpy.AddMessage(
            "There are {0} populated places in or within 200km of {1}".format(
                arcpy.management.GetCount("Places_Clip"),
                countryName
            )
        )
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
