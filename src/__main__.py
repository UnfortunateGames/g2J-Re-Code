"""The main function of g2J-Recode"""
from time import sleep
import backend.__backend__ as BE
import gui.__gui__ as G
import gui.__sprites__ as S

has_loaded: bool = False

def settings_menu() -> None:
    """
    This is the settings menu.
    """
    while True:
        G.clear()

def character_select_menu() -> None:
    """
    This is the character select menu.
    """
    cur_menu = 0
    character_list: list = [
        BE.newbie_stats, BE.expert_stats,
        BE.sustainer_stats, BE.fallen_stats
    ]
    while True:
        G.clear()
        print(G.logo + "\n")
        G.menu_scroll(S.fetch_character_menu(character_list[cur_menu]))
        x = input(f"{' ' * 14}<?->> ").lower
        match x:
            case "left":
                cur_menu += 1
                if cur_menu > 3:
                    cur_menu = 0
            case "right":
                cur_menu -= 1
                if cur_menu < 0:
                    cur_menu = 3
            case "buy":
                continue
            case "equip":
                if BE.bought_characters[cur_menu] is False:
                    input(f"{' ' * 16}Character is not bought yet!")
                else:
                    BE.cur_stats = character_list[cur_menu]
            case "menu":
                break

def game_menu() -> None:
    """
    This is the MAIN game menu
    """
    while True:
        G.menu_scroll(S.main_menu)
        x = input(f"\n{' ' * 14}<(->> ").lower()
        match x:
            case "start":
                continue
            case "continue":
                if has_loaded is False:
                    print(f"{' ' * 14}You haven't loaded a save yet!")
                    input(f"{' ' * 14}Press enter to continue...")
                else:
                    # start game
                    continue
            case "settings":
                # settings menu
                continue
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
    # Eh... What even is this for?
    initialize_intro()
