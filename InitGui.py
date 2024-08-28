# ***********************************************************************
# *                                                                     *
# * Copyright (c) 2023 Ondsel                                           *
# *                                                                     *
# ***********************************************************************
from PySide2 import QtCore

from lens_command import LensCommand, LensWorkbenchManipulator, start_mdi_tab
from CADAccess import FreeCADGui as Gui

import WorkspaceView


Gui.addCommand("OndselLens_OndselLens", LensCommand())
Gui.addWorkbenchManipulator(LensWorkbenchManipulator())

start_mdi_tab()

QtCore.QTimer.singleShot(3000, WorkspaceView.runsAfterLaunch)
