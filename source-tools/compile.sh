#!/bin/bash
cd source-tools
pyinstaller --onefile ../src/__main__.py --name g2J-build --distpath ../out
rm -r g2J-build.spec build
