try:
    import FreeCAD
except ImportError:
    from CADAccess.MockFreeCAD import FreeCAD
try:
    import FreeCADGui
except ImportError:
    from CADAccess.MockFreeCADGui import FreeCADGui
try:
    import AddonManager
except ImportError:
    from CADAccess.MockAddonManager import AddonManager
