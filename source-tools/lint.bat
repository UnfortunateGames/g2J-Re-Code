echo off
echo Using Ruff to lint...
cd src
ruff check
ruff clean
cd ..
