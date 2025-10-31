echo off
pyinstaller --onefile ../src/__main__.py --name g2J-build.exe --distpath ../out
del build/* g2J-build.spec
rmdir build
