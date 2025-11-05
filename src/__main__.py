"""The main function of g2J-Recode"""

# Built-in Modules

from time import sleep
from sys import exit as syxit

# External Modules

import backend.__backend__ as BE
import gui.__gui__ as G
import gui.__sprites__ as S

# - IN-GAME LOGIC -


def game_intro() -> None:
    """
    The seemingly long intro to the game.
    """

    def he_speaks(message: str = "", withloc: bool = False) -> None:
        G.clear()
        print("\n\n\n\n")
        if withloc is True:
            G.print_location_display()
        G.print_animation(message)

    G.clear()
    sleep(2)
    he_speaks("Hello.")
    sleep(1)
    he_speaks("Do not worry, for I am your creator.")
    sleep(1)
    he_speaks("My creation.")
    sleep(1.5)
    he_speaks("You...")
    sleep(2)
    he_speaks("You are..?")
    sleep(1)
    BE.name = input(f"\n{' ' * 14}Your name. -> ")
    G.clear()
    sleep(1)
    he_speaks(f"{BE.name}...")
    sleep(2)
    he_speaks("Very wise...")
    sleep(2)
    he_speaks("I cast LIGHT upon you.")
    sleep(1)
    G.clear()
    G.print_animation(G.print_location_display(True))
    sleep(2)
    he_speaks("This is my relam.", True)
    sleep(1)
    he_speaks("For you to wander, and explore.", True)
    sleep(2)
    he_speaks("Don't be a strayed, as I am here.", True)
    sleep(1)
    he_speaks(f"You are not ready, {BE.name}.", True)
    sleep(1)
    he_speaks("You should go to my altar.", True)
    sleep(1)
    he_speaks("You have something to do for me.", True)
    sleep(1)
    he_speaks("Come... Come little one...", True)
    sleep(2)
    syxit(0)


def main_acts() -> None:
    """
    The main acts logic.

    This is the main branch of all
    act menus, where it handles all the menus
    via the user input.
    """
    G.print_location_display()
    G.act_scroll(S.fetch_main_acts())
    x = input(f"\n{' ' * 14}<!->>").lower()
    match x:
        case "":
            ...
        case _:
            print(f"\n{' ' * 16}What is {x}? I don't know that.")
            input(f"{' ' * 16}Press enter to continue...")
    main_acts()


# - MENU LOGIC -


def keybind_menu() -> None:
    """
    This is the menu that sets all the keybinds
    """
    cur_menu = 0
    keylist = [
        ["move", "acts", "task", "wait", "bag"],
        ["left", "right", "down", "up"],
        ["sleep", "check", "ask", "get"],
        ["back", "menu"],
    ]
    G.menu_scroll(S.keybind_change_menus[cur_menu])
    x = input(f"{' ' * 14}<?!->> ").lower()
    if x in keylist[cur_menu]:
        setter = input(
            f"\n{' ' * 15}Enter a keybind [Enter nothing to exit] -> "
        ).lower()
        if setter == "":
            keybind_menu()
            return
        idx = keylist[cur_menu].index(x)
        if idx < len(BE.keybind_list[cur_menu]):
            BE.keybind_list[cur_menu][idx] = setter
            print(f"\n{' ' * 16}Set {x} -> {setter}")
            input(f"{' ' * 16}Press enter to continue...")
        else:
            print(f"{' ' * 16}An error occured, please check the log file.")
            BE.write_log(
                "(FATAL) Outdated keybind list! Please open an issue in our github."
            )
            syxit(2)
        keybind_menu()
        return
    match x:
        case "exit":
            settings_menu()
        case _:
            print(f"\n{' ' * 16}{x} is not a valid option!")
            input(f"{' ' * 16}Press enter to continue...")


def load_logic(save: dict) -> None:
    """
    This sets all variables given by the parameter "save".

    The parameter should be:
    BE.load_save() since it returns a dict "save".
    """
    if not save:
        print(
            f"\n{' ' * 16}Save file was either empty or missing.\n"
            f"{' ' * 16}Plese check the log for more information."
        )
        input(f"{' ' * 16}Press enter to continue...")
        return
    BE.has_loaded = True
    BE.keybind_list = save["keybinds"]
    BE.bought_characters = save["bought"]
    BE.badges = save["badges"]
    BE.cur_location = save["location"]
    BE.cur_task = save["curtask"]
    BE.game_time = save["gametime"]
    BE.done_task = save["donetask"]
    BE.animal_exists = save["animalexists"]
    BE.deaths = save["deaths"]


def extra_settings() -> None:
    """
    This manages in-game settings
    As for Animation speed, and difficulty.

    Yeah... that's it... for now?
    """


def settings_menu() -> None:
    """
    This is the settings menu.
    """
    G.menu_scroll(S.settings_menu)
    x = input(f"{' ' * 14}<?->> ").lower()
    match x:
        case "keybinds":
            keybind_menu()
        case "load save":
            load_logic(BE.load_save())
        case "save game":
            BE.save_game()
        case "extras":
            extra_settings()
        case "back":
            game_menu()
            return
        case _:
            print(f"\n{' ' * 16}{x} is not a valid option!")
            input(f"{' ' * 16}Press enter to continue...")
    settings_menu()


def character_select_menu(cur_menu: int = 0) -> None:
    """
    This is the character select menu.
    """
    character_list: list = [
        BE.NEWBIE_STATS,
        BE.EXPERT_STATS,
        BE.SUSTAINER_STATS,
        BE.FALLEN_STATS,
    ]
    character = character_list[cur_menu]
    price = character.price
    name = character.name
    G.menu_scroll(S.fetch_character_menu(character_list[cur_menu]))
    x = input(f"{' ' * 14}<?->> ").lower()
    match x:
        case "right":
            cur_menu += 1
            if cur_menu > 3:
                cur_menu = 0
            character_select_menu(cur_menu)
        case "left":
            cur_menu -= 1
            if cur_menu < 0:
                cur_menu = 3
            character_select_menu(cur_menu)
        case "buy":
            if BE.bought_characters[cur_menu] is True:
                print(f"\n{' ' * 16}Character is already bought!")
                input(f"{' ' * 16}Press enter to continue...")
            elif BE.badges < price:
                print(f"\n{' ' * 16}You don't have enough badges!")
                input(f"{' ' * 16}Press enter to continue...")
            else:
                BE.badges -= price
                BE.bought_characters[cur_menu] = True
                print(f"\n{' ' * 16}Successfully bought {name}!")
                input(f"{' ' * 16}Press enter to continue...")
        case "equip":
            if BE.bought_characters[cur_menu] is False:
                print(f"\n{' ' * 16}Character hasn't been bought yet!")
                input(f"{' ' * 16}Press enter to continue...")
            else:
                BE.cur_stats = character_list[cur_menu]
        case "back":
            settings_menu()
        case _:
            print(f"\n{' ' * 16}{x} is not a valid option!")
            input(f"{' ' * 16}Press enter to continue...")


def game_menu() -> None:
    """
    This is the MAIN game menu
    """
    G.menu_scroll(S.main_menu)
    x = input(f"\n{' ' * 14}<(->> ").lower()
    match x:
        case "start game":
            game_intro()
        case "continue":
            if BE.has_loaded is False:
                print(f"{' ' * 14}You haven't loaded a save yet!")
                input(f"{' ' * 14}Press enter to continue...")
            else:
                # start game (DISCARD BELOW)
                return
        case "settings":
            settings_menu()
        case "characters":
            character_select_menu()
        case "credits":
            G.clear()
            print(G.logo + "\n")
            G.menu_scroll(S.credit_menu)
            input(f"\n\n{' ' * 14}Press Enter to continue...")
        case "exit":
            syxit(0)
        case _:
            print(f"\n{' ' * 16}{x} is not a valid option!")
            input(f"{' ' * 16}Press enter to continue...")
    game_menu()


def initialize_intro() -> None:
    """
    This initializes the game, basically running the intro.
    """
    G.clear()
    print("\n\n\n\n")
    G.print_animation("ElectricSplash Presents...")
    sleep(1.5)
    G.clear()
    print(G.logo)
    BE.cur_location = [1, 0]
    G.print_location_display()
    sleep(2)
    input(f"\n\n{' ' * 19}Press Enter to continue...")
    game_menu()


if __name__ == "__main__":
    initialize_intro()
