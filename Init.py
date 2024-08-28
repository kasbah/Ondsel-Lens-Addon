from CADAccess import FreeCAD

param_group = FreeCAD.ParamGet()
param_group.SetBool("ShowOnStartup", False)

FreeCAD.Console.PrintMessage("Init Lens\n")
