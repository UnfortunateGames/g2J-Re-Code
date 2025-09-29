"""The main function of g2J-Recode"""
from time import sleep
import gui.__gui__ as G
import gui.__sprites__ as S

has_loaded: bool = False



def character_select_menu() -> None:
    """
    This is the character select menu.
    """
    cur_menu = 0
    character_list: list = [
        newbie_stats, expert_stats,
        sustainer_stats, fallen_stats
    ]
    while True:
        clear()
        print(G.logo + "\n")
        G.menu_scroll(fetch_character_menu(character_list[cur_menu]))
        x = input(f"{' ' * 14}<?->> ").lower
        match x:
            case "left":
                continue
            case "right":
                continue
            case "buy":
                continue
            case "equip":
                continue
            case "menu":
                break

def game_menu() -> None:
    """
    The is the MAIN game menu
    """
    while True:
        G.clear()
        print(G.logo + "\n")
        G.menu_scroll(S.main_menu)
        x = input(f"\n{' ' * 14}<(->> ").lower()
        match x:
            case "start":
                continue
            case "continue":
                if has_loaded is False:
                    input(f"{' ' * 14}You haven't loaded a save yet!\n{' ' * 14}Press enter to continue...")
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
    print("\n\n\n\n" + ' ' * 19, end='')
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
