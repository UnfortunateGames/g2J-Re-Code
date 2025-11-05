echo off
echo Using Ruff to format project...
cd src
ruff format
ruff clean
cd ..
echo Success!
