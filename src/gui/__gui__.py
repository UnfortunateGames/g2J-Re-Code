"""The GUI Module ccontaining all the GUI Logic and functions"""
from time import sleep
from os import system, name
from gui.__sprites__ import location_sprites, print_sky
from backend.__backend__ import (
    cur_location, cur_stats, what_time
)

animation_speed: int = 3.5
cur_menu: int = 0

logo: str = f"""
{' ' * 16}    '.~~-go-2-~~-~~-~~-~~-~~.'
{' ' * 16}.   --. _ . . _  _  _  __ __   .
{' ' * 16}."= , ||-||v||-'| ||-'|- |-  =".
{' ' * 16} "= '_'| || ||_''_'| )'__'__ ="
{' ' * 16}    '-._Made by : ESplash_.-'
"""

def menu_scroll(menu: str) -> None:
    """
    Prints the menu with a scroll wrapper
    To reduce any repitition in the sprites
    """
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
    stats = cur_stats.stats
    chealth = stats.cur_health
    mhealth = stats.max_health
    cstamina = stats.cur_stamina
    mstamina = stats.max_stamina
    health_amount = int(
        chealth // (mhealth / 10)
    )
    stamina_amount = int(
        cstamina // (mstamina / 10)
    )
    health = '#' * health_amount
    no_health = '-' * (10 - health_amount)
    stamina = '#' * stamina_amount
    no_stamina = '-' * (10 - stamina_amount)
    head = cur_stats.head
    body = cur_stats.body
    output = f"""
.'.{head}.| Health  : {chealth} / {mhealth} | Hunger : |  //_- go 2 JAMBOREE - '.
|::{body}.| Stamina : {cstamina} / {mstamina} | ## / ##  | /_ / A game made by:   |
'.==HP==[{health}{no_health}]=SP==[{stamina}{no_stamina}]=|  // -> ELECTRICSPLASH .'
"""
    print(output)

def print_location_display(return_sprite: bool) -> None:
    """
    This is the logic for displaying the current location
    in the game.

    This is a standalone function. So don't pass it to
    a print() statement, it will print it on it's own.
    """
    if return_sprite is True:
        return (
            print_sky(0 if what_time == 0 else 1, True)
            +
            location_sprites[cur_location[1]][cur_location[0]]
        )
    print_sky(0 if what_time == 0 else 1, False)
    print(location_sprites[cur_location[1]][cur_location[0]])

def print_animation(message: str = "", centralize: bool = True) -> None:
    """
    Prints a message with a typing animation effect.
    Just a simple animation <3
    """
    if centralize is True:
        print(' ' * ((64 - len(list(message))) // 2), end='')
    for char in message:
        print(char, end='', flush=True)
        sleep(animation_speed / len(list(message)))

def centralize_print(message: str) -> None:
    print(f"{' ' * ((64 - len(list(message))) // 2)}{message}")

def clear() -> None:
    """
    Clears the screen of the terminal while
    also checking for the platform to execute the
    appropriate command for said platform.
    """
    system('cls' if name == 'nt' else 'clear')

def fetch_task_dialogue(type: str) -> str:    
    """
    This fetches the task dialogue.
    and returns the said dialogue.

    Note that this RETURNS a string.
    Not print it, so do print it yourself.
    """
    if done_task is True:
        return [
            "Your task is done.", "Go ahead and rest.",
            "Carry on."
    ]
    if heard_task is False:
        return [
            "Ah, you have come back.", f"Your task is {cur_task.name}",
            cur_task.guide[0], cur_task.guide[1],
            "Carry on."
        ]
    return [
        "Have you forgotten?", f"Your task is {cur_task.name}",
        cur_task.guide[0], cur_task.guide[1],
        "Carry on."
    ]

def fetch_random_dialogue(type: str) -> Dialogue:
    if type == "task":
        dialogue = [cur_task.dialogue[0], cur_task.dialogue[1]]
    if type == "sleep":
        dialogue =  [
            "Ah... Home sweet home...",
            "Nothing beats a good night's rest"
        ]
