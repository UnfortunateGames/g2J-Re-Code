# go 2 JAMBOREE
```
                                   '.~~-go-2-~~-~~-~~-~~-~~.'
                                .   --. _ . . _ _ _ __ __ .
                                ."= , ||-||v||-'| ||-'|- |- =".
                                 "= '_'| || ||_''_'| )'__'__ ="
                                   '-._Made by : ESplash_.-'
```
A CLI Python game I'm working on.

A game where ~~God~~ guides you on your way to salvation!
Do tasks, hunt and eat for food.
Just don't make ~~God~~ angry!

## ANOUNCEMENTS:

This will now be the *official* **go 2 JAMBOREE** code base.
The last version will be archived.

## How to Run:
### Requirements:
- Python (Duh)
### For Developers:
- PyInstaller (To compress it to a directory or .exe file)
> To read the Python code from source, read the doc. (Yes I know it's not implemented in yet)
> Or if you're a huge chad just read the docstrings instead.

*If running from source, please follow the instructions below in each specified platform.*

### Windows
Simply double-click or *"run"* the *runGame.bat* file in the root directory or either run below:
```
./runGame.bat
```

### Linux / MacOS
Run the .sh file in your terminal, follow these instructions:

Set directory to the repository:
```
cd g2J-Re-Code
```
Then run the _shell_ file:
```
./rungame.sh
```
**If it doesn't run**, then run this command on the _runGame_ shell file:
```
chmod +x ./runGame.sh
```

If downloading from releases, please select the specified platform package from there.
No need for any special run cases.

## How to play:
### 1. Do your tasks!
In the altar you have to **ask**  before doing the task, *he* will guide you how.
### 2. Survive!
You can get food by the lake, or the forest entrance!
Or if you really dare. Hunt the animals for better food!
### ~~3. escape~~
~~you will be ##@^#*&$#.~~

## For developers:
If you want to modify the game or *maybe* fix the game bugs yourself.
Simply download the source code.
Or if you're a **giant** *nerd*, clone the repo via terminal:
```
git clone https://github.com/UnfortunateGames/g2J-Re-Code.git
```
And just set your directory to the repo

Now *optionally* you can compress it to a directory or a singular .exe file using PyInstaller.
Just by running:
```
PyInstaller src/__main__.py
```
But of course you need PyInstaller to begin with.
If you're a Windows User you're lucky to only need 1 command to install it:
```
pip install PyInstaller
```
Else if your a Linux/MacOS User, you're gonna need a virtual environment for that.
So with a staggering *1 extra command*
You need to run this:
```
python -m venv g2J-Tools
pip install PyInstaller
```

Now for reading the Python code? Go ahead to the doc of the repository.
> [!WARNING]
> For now just read the docstrings my bad.