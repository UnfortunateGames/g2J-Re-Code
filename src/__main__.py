"""The main function of g2J-Recode"""

from time import sleep
from sys import exit as syxit
import backend.__backend__ as BE
import gui.__gui__ as G
import gui.__sprites__ as S


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
    while True:
        G.menu_scroll(S.keybind_change_menus[cur_menu])
        x = input(f"{' ' * 14}<?!->> ").lower()
        if x in keylist[cur_menu]:
            setter = input(
                f"{' ' * 15}Enter a keybind [Enter nothing to exit] -> "
            ).lower()
            if setter == "":
                continue
            idx = keylist[cur_menu].index(x)
            if idx < len(BE.keybind_list[cur_menu]):
                BE.keybind_list[cur_menu][idx] = setter
                print(f"{' ' * 16}Set {x} -> {setter}")
                input(f"{' ' * 16}Press enter to continue...")
            else:
                print(f"{" " * 16}An error occured, please check the log file.")
                BE.write_log("(FATAL) Outdated keybind list!")
                syxit(2)
            continue
        match x:
            case "exit":
                break
            case _:
                print(f"{' ' * 16}{x} is not a valid option!")
                input(f"{' ' * 16}Press enter to continue...")


def settings_menu() -> None:
    """
    This is the settings menu.
    """
    while True:
        G.menu_scroll(S.settings_menu)
        x = input(f"{" " * 14}<?->> ").lower()
        match x:
            case "keybinds":
                keybind_menu()
            case "load save":
                save = BE.load_save()
                if not save:
                    print(
                        f"{' ' * 16}Save file was either empty or missing.\n" \
                        f"{' ' * 16}Plese check the log for more information."
                    )
                    input(f"{' ' * 16}Press enter to continue...")
                    continue
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
            case "save game":
                BE.save_game()
            case "back":
                break
            case _:
                print(f"{" " * 16}{x} is not a valid option!")
                input(f"{" " * 16}Press enter to continue...")


def character_select_menu() -> None:
    """
    This is the character select menu.
    """
    cur_menu = 0
    character_list: list = [
        BE.NEWBIE_STATS,
        BE.EXPERT_STATS,
        BE.SUSTAINER_STATS,
        BE.FALLEN_STATS,
    ]
    while True:
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
            case "left":
                cur_menu -= 1
                if cur_menu < 0:
                    cur_menu = 3
            case "buy":
                if BE.bought_characters[cur_menu] is True:
                    print(f"{" " * 16}Character is already bought!")
                    input(f"{" " * 16}Press enter to continue...")
                elif BE.badges < price:
                    print(f"{" " * 16}You don't have enough badges!")
                    input(f"{" " * 16}Press enter to continue...")
                else:
                    BE.badges -= price
                    BE.bought_characters[cur_menu] = True
                    print(f"{" " * 16}Successfully bought {name}!")
                    input(f"{" " * 16}Press enter to continue...")
            case "equip":
                if BE.bought_characters[cur_menu] is False:
                    print(f"{' ' * 16}Character hasn't been bought yet!")
                    input(f"{" " * 16}Press enter to continue...")
                else:
                    BE.cur_stats = character_list[cur_menu]
            case "back":
                break
            case _:
                print(f"{" " * 16}{x} is not a valid option!")
                input(f"{" " * 16}Press enter to continue...")


def game_menu() -> None:
    """
    This is the MAIN game menu
    """
    while True:
        G.menu_scroll(S.main_menu)
        x = input(f"\n{' ' * 14}<(->> ").lower()
        match x:
            case "start":
                # intro
                continue
            case "continue":
                if BE.has_loaded is False:
                    print(f"{' ' * 14}You haven't loaded a save yet!")
                    input(f"{' ' * 14}Press enter to continue...")
                else:
                    # start game
                    continue
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
                break


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
    print("\n" + S.Campsite_sprite)
    sleep(2)
    input(f"\n\n{' ' * 19}Press Enter to continue...")
    game_menu()


if __name__ == "__main__":
    # Maybe I need to rename it to main?
    # I mean who cares about names?
    initialize_intro()
