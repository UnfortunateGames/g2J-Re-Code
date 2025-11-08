#!/bin/bash
pyinstaller --onefile g2J-RC/__main__.py --name g2J-build --distpath out
rm -r g2J-build.spec build
