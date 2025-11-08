"""The GUI Module containing all the GUI Logic and functions"""

# Built-in modules
from time import sleep
from random import randint
from os import system, name

# External Modules
from gui.__sprites__ import location_sprites, print_sky
import backend.__backend__ as BE


logo: str = f"""
{" " * 16}    '.~~-go-2-~~-~~-~~-~~-~~.'
{" " * 16}.   --. _ . . _  _  _  __ __   .
{" " * 16}."= , ||-||v||-'| ||-'|- |-  =".
{" " * 16} "= '_'| || ||_''_'| )'__'__ ="
{" " * 16}    '-._Made by : ESplash_.-'
"""


def menu_scroll(menu: str) -> None:
    """
    Prints the menu with a scroll wrapper
    To reduce any repetition in the sprites
    """
    clear()
    print(logo)
    print(f"{' ' * 12}_0_{' ' * 34}_0_")
    print(f"{' ' * 12}|/|{'~' * 34}|/|")
    print(menu)
    print(f"{' ' * 12}|/|{'~' * 34}|/|")
    print(f"{' ' * 12}'0'{' ' * 34}'0'")


# - IN GAME MENUS -


def act_scroll(sprite: str = None) -> None:
    """
    This prints an action scroll wth the maximum width

    If sprite is not given it will print automatically
    with the cur_menu variable
    """
    print(f"_0_{' ' * 58}_0_")
    print(f"|/|{'~' * 58}|/|")
    if sprite:
        print(sprite)
    else:
        print()


def display_stats() -> None:
    """
    This will print the stat panel in the game

    This is a standalone function, So don't pass it to
    a print() statement, it will print it on it's own.
    """
    stats = BE.cur_stats.stats
    cur_health = stats.cur_health
    max_health = stats.max_health
    cur_stamina = stats.cur_stamina
    max_stamina = stats.max_stamina
    health_amount = int(cur_health // (max_health / 10))
    stamina_amount = int(cur_stamina // (max_stamina / 10))
    health = "#" * health_amount
    no_health = "-" * (10 - health_amount)
    stamina = "#" * stamina_amount
    no_stamina = "-" * (10 - stamina_amount)
    head = BE.cur_stats.head
    body = BE.cur_stats.body
    output = f"""
.'.{head}.| Health  : {cur_health} / {max_health} | Hunger : |  //_- go 2 JAMBOREE - '.
|::{body}.| Stamina : {cur_stamina} / {max_stamina} | ## / ##  | /_ / A game made by:   |
'.==HP==[{health}{no_health}]=SP==[{stamina}{no_stamina}]=|  // -> ELECTRICSPLASH .'
"""
    print(output)


def print_location_display(return_sprite: bool = False) -> str:
    """
    This is the logic for displaying the current location
    in the game.

    This is a standalone function. So don't pass it to
    a print() statement, it will print it on it's own.
    """
    if return_sprite is True:
        return (
            print_sky(0 if BE.what_time == 0 else 1, False)
            + location_sprites[BE.cur_location[1]][BE.cur_location[0]]
        )
    print_sky(0 if BE.what_time == 0 else 1, True)
    print(location_sprites[BE.cur_location[1]][BE.cur_location[0]])
    return ""


def print_animation(message: str = "", centralize: bool = True) -> None:
    """
    Prints a message with a typing animation effect.
    Just a simple animation <3
    """
    delay_amount = BE.animation_speed / (len(list(message)) * len(list(message)))
    delay = delay_amount
    if centralize is True:
        print(" " * ((64 - len(list(message))) // 2), end="")
    for char in message:
        print(char, end="", flush=True)
        sleep(delay)
        delay += delay_amount
    print()


def centralize_print(message: str) -> None:
    """
    This centralizes the parameter message to print.
    """
    spaces = " " * ((64 - len(list(message))) // 2)
    print(f"{spaces}{message}")


def clear() -> None:
    """
    Clears the screen of the terminal while
    also checking for the platform to execute the
    appropriate command for said platform.
    """
    system("cls" if name == "nt" else "clear")


# add the task animation function here


def move_animation(speed: int = 1, debug: bool = False) -> None:
    """
    This is the move animation function.
    Debug mode is available.

    The debug mode will write to the log however!
    This is done so you can report how trash I am at
    coding.
    """
    legs = ["/ \\", "/<", "<|"]
    head = BE.cur_stats.head
    body = BE.cur_stats.body
    dots = 0
    delay = (BE.animation_speed / 15) / speed
    if debug is True:
        BE.write_log("(Not Fatal) Move animation function on debug mode!")
    for i in range(15):
        clear()
        leg = i % 3
        dot_timer = i % 5
        if dot_timer == 0:
            dots += 1
        # Yeah, I'd revise this, but nah.
        # One print call is all it takes
        print(
            i + "\n" if debug is True else "\n",
            f"\n\n{' ' * 25}_0_{' ' * 11}_0_\n",
            f"{' ' * 24}|/|{'~' * 11}|/|\n",
            f"\n{(' ' * 32) + head}\n{(' ' * 32) + body}\n",
            f"{(' ' * 31) + legs[leg]}\n",
            f"{' ' * 28}Moving{'.' * dots}\n",
            f"\n{' ' * 25}|/|{'~' * 11}|/|\n",
            f"{' ' * 24}'0'{' ' * 11}'0'",
        )
        sleep(delay)


def fetch_task_dialogue() -> list:
    """
    This fetches the task dialogue.
    and returns the said dialogue.

    Note that this RETURNS a list.
    Use a special loop for this.
    """
    if BE.done_task is True:
        return ["Your task is done.", "Go ahead and rest.", "Carry on."]
    if BE.heard_task is False:
        return [
            "Ah, you have come back.",
            f"Your task is {BE.cur_task.name}",
            BE.cur_task.guide[0],
            BE.cur_task.guide[1],
            "Carry on.",
        ]
    return [
        "Have you forgotten?",
        f"Your task is {BE.cur_task.name}",
        BE.cur_task.guide[0],
        BE.cur_task.guide[1],
        "Carry on.",
    ]


def fetch_random_dialogue(dialogue_type: str) -> str:
    """
    This fetches a random piece of dialogue.

    Used in the if statements below.
    """
    dialogue = []
    if dialogue_type == "task":
        dialogue = [BE.cur_task.dialogue[0], BE.cur_task.dialogue[1]]
    if dialogue_type == "sleep":
        dialogue = ["Ah... Home sweet home...", "Nothing beats a good night's rest"]
    if dialogue_type == "wait":
        dialogue = [
            "Hmmm... Zen...",
            "Nature... Serenity...",
            "Sin... No... Grr...",
        ]
    return dialogue[randint(0, len(dialogue) - 1)]
