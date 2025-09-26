"""The GUI Module ccontaining all the GUI Logic and functions"""
from time import sleep
animation_speed: int = 3.5

def print_animation(message: str) -> None:
    """
    Prints a message with a typing animation effect.
    Just a simple animation <3
    """
    for char in message:
        print(char, end='', flush=True)
        sleep(animation_speed / len(list(message)))
