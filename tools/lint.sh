#!/bin/bash
echo Using Ruff to lint...
cd ../g2J-RC
ruff analyze
ruff clean
cd ..
