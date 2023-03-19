{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Script Completed\n"
     ]
    }
   ],
   "source": [
    "import arcpy\n",
    "\n",
    "arcpy.env.overwriteOutput = True\n",
    "\n",
    "# if arcpy.Exists(\"D:\\00-Learning\\02-GisDev\\01-ArcPy\\Projects\\EnvProject\\test.gdb\"):\n",
    "#     arcpy.Delete_management(\"D:\\00-Learning\\02-GisDev\\01-ArcPy\\Projects\\EnvProject\\test.gdb\")\n",
    "\n",
    "arcpy.CreateFileGDB_management(r\"D:\\00-Learning\\02-GisDev\\01-ArcPy\\Projects\\EnvProject\",\"Test.gdb\")\n",
    "\n",
    "print('\\nScript Completed')\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "arcgispro-py3-for_study",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.11"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
