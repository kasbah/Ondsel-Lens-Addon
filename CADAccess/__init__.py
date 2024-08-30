INSIDE_MOCK = False

try:
    import FreeCAD
except ImportError:
    from CADAccess.MockFreeCAD import FreeCAD

try:
    import FreeCADGui
except ImportError:
    from CADAccess.MockFreeCADGui import FreeCADGui

    INSIDE_MOCK = True
    # try:
    #     import resources
    # except ImportError:
    #     import CADAccess.helpers
    #     helpers.build_local_resources_py_during_mock()
    #     import resources

try:
    import AddonManager
except ImportError:
    from CADAccess.MockAddonManager import AddonManager
