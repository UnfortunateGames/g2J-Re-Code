# The **SOURCE TOOLS**

## What are these for?

It's quite **complicated** at first,
but it's just *automation* at its finest.

Although some of these might be "*why tf is this here*",
it's just for *convenience* if you can stand my **slop** *code*.

There's a **lot** of *things* here to help you!

### These include

- A compile script

> For your distribution needs!

- Save remover

> Remember to do this since you might leak your saves lol

- And a reformatter!

> Cause I suck at programming, though idk if you'll need this
> Though please run this before a pull request, it'd be awful
> to reformat your ass code too.

## What do I need?

For now it only needs **2 external Python modules**:
*PyInstaller*, and *Black*.

It should be *easy* nonetheless, as installing it should be no deal.

For **Windows**:

> Pretty simple.

```sh
pip install pyinstaller black
```

For **Linux** and **MacOS**:

> These systems differ slightly in how they manage Python
> modules, though they can be solved with one solution:
> Use a virtual Python environment.
> I recommend putting it in this directory!

```sh
python3 -m venv venv
```

> Activate it of course

```sh
source venv/bin/activate
```

> Then install via pip

```sh
pip install pyinstaller black
```

> Optionally for Linux
> Install Black using your package manager

```sh
# For Debian based systems:
sudo apt install python3-black

# For Arch Systems: (u use arch btw)
sudo pacman -S black

# RedHat also has the same package:
sudo dnf install python3-black
```

## For usage

All you need is the **dependencies listed above**, and these scripts should
just run *fine* without any precaution.

I'd recommend running the scripts in the root directory (g2J-Re-Code)
If you're in any other directory, it'd be my bet it's gonna throw an error.
