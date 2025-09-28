"""The sprite module containing the sprites and animations for the GUI"""

from random import randint
from backend.__backend__ import keybind_list as KBL
from backend.__classes__ import Character
from backend.__backend__ import (
    bought_characters, write_log, cur_location,
    cur_task, animal_exists, what_time,
    done_task, wait_cooldown, seen_locations
)

# - MENU SPRITES -

main_menu: str = f"""
{" " * 16}<( Main Menu : )>

{" " * 16}  <> ->   Start Game   ]
{" " * 16}  () -> Continue Game  ]
{" " * 16}  @* ->    Settings    ]
{" " * 16}  ~~ ->    Credits     ]

{" " * 16}[] <- [ Exit ]
"""
settings_menu: str = f"""
{" " * 16}<( Settings : )>

{" " * 16}  !? ->    Keybinds   ]
{" " * 16}  _? -> Load Keybinds ]
{" " * 16}  _@ ->   Load Game   ]
{" " * 16}  #> ->   Save Game   ]

{" " * 16}() <- [ Back ]
"""

credit_menu: str = f"""
{" " * 16}<( Credits : )>

{" " * 16} Creator - '.- E-SPLASH -.'
{" " * 16}    THIS IS ALL I GOT

{" " * 16}() <- [ Back]
"""

keybind_change_menus: list = [
    f"""
{" " * 16}<( KeyBinds : )>

{" " * 16}?> Main Keybinds)
{" " * 16}-> Move : {KBL[0][0]}
{" " * 16}-> Acts : {KBL[0][1]}
{" " * 16}-> Task : {KBL[0][2]}
{" " * 16}-> Wait : {KBL[0][3]}
{" " * 16}-> Bag  : {KBL[0][4]}

{" " * 16}() <- [ Back ]
""",
    f"""
{" " * 16}<( KeyBinds : )>

{" " * 16}?> Move Keybinds )
{" " * 16}-> Left  : {KBL[1][0]}
{" " * 16}-> Right : {KBL[1][1]}
{" " * 16}-> Down  : {KBL[1][2]}
{" " * 16}-> Up    : {KBL[1][3]}

{" " * 16}() <- [ Back ]
""",
    f"""
{" " * 16}<( KeyBinds : )>

{" " * 16}?> Acts Keybinds )
{" " * 16}-> Sleep : {KBL[2][0]}
{" " * 16}-> Check : {KBL[2][1]}
{" " * 16}-> Ask   : {KBL[2][2]}
{" " * 16}-> Get   : {KBL[2][3]}

{" " * 16}() <- [ Back ]
""",
    f"""
{" " * 16}<( KeyBinds : )>

{" " * 16}?> Misc. Keybinds )
{" " * 16}-> Back : {KBL[3][0]}
{" " * 16}-> Menu : {KBL[3][1]}

{" " * 16}() <- [ Back ]
""",
]

def fetch_character_menu(character: Character) -> None:
    """
    This returns a menu sprite

    This SHOULD be used like:
    menu_scroll(fetch_character_menu(character))

    You have to pass in the character as the parameter
    Though I passed in newbie_stats for default so you can
    ONLY break this if you passed in an invalid character
    """
    head = character.head
    body = character.body
    price = character.price
    description = character.description
    if bought_characters[character.index] is False:
        equip = f"{price} badges > [ Get ]"
    elif bought_characters[character.index] is True:
        equip = "Unlocked! > Equip"
    else:
        write_log(
            f"(Not Fatal) Character equip was undefined at index: {character.index}"
        )
        equip = "Error!"
    sprite = f"""
{" " * 16}<( Character Select: )>

{" " * 16}   <- [ Left ] | [ Right ] ->
{" " * 16}  #->"{description}"
{" " * 16}    {head} | Health  : {character.stats.max_health}
{" " * 16}    {body} | Stamina : {character.stats.max_stamina}
{" " * 16}    / \ | {equip}

{" " * 16}<> <- [ Back ]
"""
    return sprite

# - IF RETURN -
# Moved from gui since circular imports are
# disallowed in python :(

def check_act(what: str = None, act: str = None) -> str:
    """
    This returns a '!' or ' '.
    
    This will be mainly used for the
    menu guis to check if available.

    SORRY! Seems like a specific default cannot be applied
    So you have to put None whether or not you're using "act"
    as the paramter! Deeply sorry.

    This should be applied like:
    [ button ]=======( check_act(button) )
    """
    return_value = ' '
    match what:
        case "left":
            if cur_location[0] != 0:
                return_value = '!'
        case "right":
            if cur_location[1] != 0:
                return_value = '!'
        case "down":
            if cur_location[0] != 3:
                return_value = '!'
        case "up":
            if cur_location[1] != 1:
                return_value = '!'
        case "task":
            if cur_location == cur_task.location:
                return_value = '!'
        case "get":
            # We will apply this added complexity later
            # in __main__.py
            match cur_location:
                case [0, 0]:
                    return_value = '@'
                case [1, 1]:
                    return_value = '#'
                case [2, 1]:
                    if animal_exists is True:
                        return_value = '&'
        case "acts":
            match act:
                case "sleep":
                    if what_time == "Night" & cur_location == [1, 0]:
                        return_value = 'Z'
                case "ask":
                    if done_task == False & cur_location == [0, 1]:
                        return_value = '?'
                case _:
                    if (
                        check_act("get") != ' '
                        |
                        check_act("acts", "sleep") != ' '
                        |
                        check_act("acts", "ask") != ' '
                        ):
                        return_value = '!'
        case "wait":
            if wait_cooldown <= 0:
                return_value = '!'
        case _:
            write_log("(Not Fatal) Invalid check_act call")
    return return_value

# - IN GAME SPRITES -

def random_sprinkle(
        elements: list, chance: int = 8, height: int = 3,
        length: int = 64
    ) -> list:
    """
    A random sprinkler

    This returns a list of structure:
    [[], [], ... height]

    You should use this like:
    output = random_sprinkle(parameters)
    """
    output = []
    for i in range(height):
        output.append([])
        for _ in range(length):
            output[i].append(elements[1] if randint(0, 10) > chance else elements[0])
    return output

def print_check_sprite(what: int) -> None:
    """
    This returns the check sprite

    The parameters are exactly the same as print_sky()
    0 for night, 1 for day

    It is standalone, you don't need to print() it
    """
    if what == 0:
        sky_elements = [' ', '*']
    else:
        sky_elements = [':', ';']
    output = random_sprinkle(sky_elements, 9, 7, 64)
    if what == 0:
        output[1][28:34] =   ".----."
        output[2][27:35] =  "' .  ; '"
        output[3][26:36] = "| - () + |"
        output[4][27:35] =  ". ( :  ."
        output[5][28:34] =   "'----'"
    else:
        output[1][28:34] =   ";----;"
        output[2][27:35] =  "'      '"
        output[3][26:36] = "| < () > |"
        output[4][27:35] =  ".      ."
        output[5][29:33] =    "----"
    for i in range(7):
        print("".join(output[i]))

def print_sky(what: int, return_sprite: bool) -> None:
    """
    This should create the illusion of a random sky.

    No print() statement is needed for this function.
    It will print it on it's own.

    The what parameter should be:
    0 if BE.what_time == "Night" else 1

    The return_sprite parameter is self explanatory.
    It returns the sprite instead if it's True

    Or as configured in the intro,
    Whatever you want essentially.
    The default is the day sky
    """
    sky = [[], [], []]
    if what == 0:
        sky_elements = [" ", "."]
    else:
        sky_elements = [":", ";"]
    sky = random_sprinkle(sky_elements, 8, 3, 64)
    sky[0][57:63] = ".';o'."
    sky[1][57:63] = "'.',.'"
    if what != 0:
        for i in range(64):
            sky[2][i] = (
                (";" if randint(0, 10) > 8 else ":")
                if i % 2 == 1
                else ("`" if randint(0, 10) > 8 else "'")
            )
    sprite = "".join(sky[0]) + "\n" + "".join(sky[1]) + "\n" + "".join(sky[2])
    if return_sprite is True:
        return sprite
    print(sprite, end='')

# - MAP SPRITES - ( omfg this takes too long )

Forest_Entrance_sprite: str = """

"""

Campsite_sprite: str = """

"""

Spawn_sprite: str = """

"""

Cliff0_sprite: str = """

"""

Altar_sprite: str = """

"""

Small_Lake_sprite: str = """

"""

Plains_sprite: str = """

"""

Cliff1_sprite: str = """

"""

location_sprites: list = [
    [Forest_Entrance_sprite, Campsite_sprite, Spawn_sprite, Cliff0_sprite],
    [Altar_sprite, Small_Lake_sprite, Plains_sprite, Cliff1_sprite]
]

def fetch_main_acts() -> str:
    """
    This returns a main acts menu.

    Note that this RETURNS a menu.
    You will need to print() this so do not treat
    this as a standalone function.
    """
    acts = check_act("acts")
    task = check_act("task")
    wait = check_act("wait")
    return f"""
    <( MAIN ACTS : )>

      -> [  Move  ]-<->-<->-<->-<->-<->-<->-<->-<->-<->[ ! ]
      -> [  Acts  ]<->-<->-<->-<->-<->-<->-<->-<->-<->-[ {acts} ]
      -> [  Task  ]->-<->-<->-<->-<->-<->-<->-<->-<->-<[ {task} ]
      -> [  Wait  ]>-<->-<->-<->-<->-<->-<->-<->-<->-<-[ {wait} ]
       [:) <- <[  Bag  ]>

    [!] <<- [  Menu  ]
"""

def fetch_move_acts() -> str:
    """
    This returns the move acts menu

    Note that this RETURNS a menu.
    You will need to print() this so do not treat
    this as a standalone function.
    """
    left = check_act("left")
    right = check_act("right")
    down = check_act("down")
    up = check_act("up")
    return f"""
    <( MOVE ACTS : )>
                                      [ 'FastTravel' ] ->
                                    ,-[ {up} ]
                    [ {left} ]-.   ([   UP   ])
                      ([ LEFT ])   <>   ([  RIGHT ])
                              ([  DOWN  ])    '-[ {right} ]
                             [ {down} ]-'
    [ !? ] <<- [ Back ]
"""

def fetch_fasttravel_acts() -> None:
    """
    This returns the fat travel menu

    Note that this RETURNS a menu.
    You will need to print() this so do not treat
    this as a standalone function.
    """
    forest = "FE" if seen_locations[0][0] is True else "??"
    return f"""
    <( FAST TRAVEL : )>

        (!) -> Fast Travel Consumes more stamina!
        [ ({forest}) ] >-< [ (??) ] <-> [ (??) ] >-< [ (??) ]
        [ (??) ] <-> [ (??) ] >-< [ (??) ] <-> [ (??) ]
"""
