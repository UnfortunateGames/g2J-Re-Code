echo off
echo Removing __save__.txt...
del src/backend/saveFile/__save__.txt
type nul > src/backend/saveFile/__save__.txt
echo Success!
