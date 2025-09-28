"""The main function of g2J-Recode"""
from time import sleep
import gui.__gui__ as G
import gui.__sprites__ as S

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
    # Game Menu Function

if __name__ == "__main__":
    initialize_intro()
