echo off

pyinstaller --onefile src/__main__.py --name g2J-build.exe --distpath out
rmdir /s /q build
del __maiN__.spec

