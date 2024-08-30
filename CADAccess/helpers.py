# import fnmatch
# import os
# import re
# import subprocess
#
# source_dir = "Resources"
# output_dir = "_mock_environment"
# name = "ondselmock"
#
# def scan(directory):
#     resources = []
#     for path, dirs, files in os.walk(directory):
#         files = [os.path.join(path, f) for f in files]
#         resources += files
#     return resources
#
# def write(resources):
#     with open(f"{name}.qrc", 'w') as f:
#         f.write('<RCC>\n')
#         f.write('  <qresource>\n')
#         for r in resources:
#             f.write(f'    <file>{r}</file>\n')
#         f.write('  </qresource>\n')
#         f.write('</RCC>\n')
#
# def build_local_resources_py_during_mock():
#     resources = scan(source_dir)
#     write(resources)
#     subprocess.run([
#         "pyside2-rcc",
#         f"{name}.qrc",
#         "-o",
#         f"resources.py"
#     ])
