# Mock Development Environment

While it is technically possible to run a debugger withing the context of a running instance of FreeCAD/OndselES; thus accessing the debugger, seeing the runtime libs, and getting an IDE to honor all this. It is royal pain in rear to do so.

This is a "mock" environment that makes things easier without bothering with FreeCAD itself.

HOWEVER, it is JUST a mocking environment. Final testing should always be done with FreeCAD.

## Using Jetbrain's PyCharm

- Create a configuration of type `Python` that runs `_mock_freecad.py` as it's "script" target.
- From settings->`Project`->`General Interpreter` choose a "new interpreter", Use VirtualEnv. Use subdirectory 'venv'. The `.gitignore` file is setup to ignore that directory.
- Add the libraries needed. If nothing else you can open an IDE terminal (the prompt should now have `(venv)` prefixed.)
- The packages are:
  - the contents of https://github.com/FreeCAD/FreeCAD/blob/main/requirements.txt (see note below)
  - `pyjwt`
  - `requests`
  - `tzlocal`
  - ... and examine package.xml for anything else it might need

Feel free to just copy that `requirements.txt` file locally. I have .gitignore also ignore that file if it exists. They very act of installing the requirements.txt might prompt PyCharm to manage the install for you. That is better.

Personally, I used Python 3.11 and had to modify some version numbers. Also I removed `Pivy` as that comes from my debian package manager not pip. PyCharm did most of the installs. But I had to manually run `pip install pyside2` for some reason.

I also had to move to `ifcopenshell==0.7.10` for mathutils to properly compile.