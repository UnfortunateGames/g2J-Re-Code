#!/bin/bash
echo Compiling project to directory "out" with PyInstaller
PyInstaller --onefile ../src/__main__.py --distpath ../out/
echo Compiled to one executable at "out"