# The **SOURCE TOOLS**

## What are these for?

It's quite **complicated** at first,
but it's just *automation* at its finest.

Although some of these might be "*why tf is this here*",
it's just for *convenience* if you can stand my **slop** *code*.

> Or just for me...

There's a **lot** of *things* here to help you!

### These include

- A compile script

> For your distribution needs!

- Save remover

> Remember to do this since you might leak your saves lol

- A linter

> For all your garbage code to be removed!

- And a formatter!

> Cause I suck at programming, though idk if you'll need this
> Though please run this before a pull request, it'd be awful
> to reformat your ass code too.

## What do I need?

For now it only needs **2 external Python modules**:
*PyInstaller*, and *Ruff*.

It should be *easy* nonetheless, as installing it should be no deal.

For **Windows**:

> Pretty simple.

```sh
pip install pyinstaller ruff
```

> You should be ready to go ahead and run the scripts I made!

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
pip install pyinstaller ruff
```

> Optionally for Linux
> Install Black using your package manager

```sh
# For Debian based systems:
sudo apt install python3-ruff

# For Arch Systems: (u use arch btw)
sudo pacman -S ruff

# RedHat also has the same package:
sudo dnf install python3-ruff
```

> Unfortunately there is no PyInstaller package to my knowledge
> As i use arch btw. I will update this README accordingly if I find any.
> Or if you (Yes, you!) contributors, pull request some.

## For usage

All you need is the **dependencies listed above**, and these scripts should
just run *fine* without any precaution.

I'd recommend running the scripts in this directory ( g2J-Re-Code/tools )
If you're in any other directory, it'd be my bet it's gonna throw an error.
