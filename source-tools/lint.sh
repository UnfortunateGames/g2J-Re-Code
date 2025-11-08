#!/bin/bash
echo Using Ruff to lint...
cd g2J-RC
ruff check
ruff clean
cd ..
