echo off
pyinstaller --onefile ../g2J-RC/__main__.py --name g2J-build.exe --distpath out
rmdir /s /q build
del *.spec
