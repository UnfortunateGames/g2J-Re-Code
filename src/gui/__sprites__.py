"""The sprite module containing the sprites and animations for the GUI"""

# Built-in Modules
from random import randint

# External Modules
from backend import __backend__ as BE
from backend.__backend__ import keybind_list as KBL
from backend.__classes__ import Character

# - MENU SPRITES -

main_menu: str = f"""
{" " * 16}<( Main Menu : )>

{" " * 16}  <> ->   Start Game   ]
{" " * 16}  () -> Continue Game  ]
{" " * 16}  @* ->    Settings    ]
{" " * 16}  o/ ->   Characters   ]
{" " * 16}  ~~ ->    Credits     ]

{" " * 16}[] <- [ Exit ]
"""
settings_menu: str = f"""
{" " * 16}<( Settings : )>

{" " * 16}  !? ->    Keybinds   ]
{" " * 16}  _@ ->   Load Save   ]
{" " * 16}  #> ->   Save Game   ]

{" " * 16}() <- [ Back ]
"""

credit_menu: str = f"""
{" " * 16}<( Credits : )>

{" " * 16} Creator - '.- E-SPLASH -.'
{" " * 16}    THIS IS ALL I GOT

{" " * 16}() <- [ Back ]
"""

keybind_change_menus: list = [
    f"""
{" " * 16}<( KeyBinds : )>

{" " * 16} <-[ '<' ] | [ '>' ]->

{" " * 16}?> Main Keybinds)
{" " * 16} -> Move : {KBL[0][0]}
{" " * 16} -> Acts : {KBL[0][1]}
{" " * 16} -> Task : {KBL[0][2]}
{" " * 16} -> Wait : {KBL[0][3]}
{" " * 16} -> Bag  : {KBL[0][4]}

{" " * 16}() <- [ Exit ]
""",
    f"""
{" " * 16}<( KeyBinds : )>

{" " * 16}?> Move Keybinds )
{" " * 16} -> Left  : {KBL[1][0]}
{" " * 16} -> Right : {KBL[1][1]}
{" " * 16} -> Down  : {KBL[1][2]}
{" " * 16} -> Up    : {KBL[1][3]}

{" " * 16}() <- [ Exit ]
""",
    f"""
{" " * 16}<( KeyBinds : )>

{" " * 16}?> Acts Keybinds )
{" " * 16} -> Sleep : {KBL[2][0]}
{" " * 16} -> Check : {KBL[2][1]}
{" " * 16} -> Ask   : {KBL[2][2]}
{" " * 16} -> Get   : {KBL[2][3]}

{" " * 16}() <- [ Exit ]
""",
    f"""
{" " * 16}<( KeyBinds : )>

{" " * 16}?> Misc. Keybinds )
{" " * 16} -> Back : {KBL[3][0]}
{" " * 16} -> Menu : {KBL[3][1]}

{" " * 16}() <- [ Exit ]
""",
]


def fetch_character_menu(character: Character) -> str:
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
    if BE.bought_characters[character.index] is False:
        equip = f"{price} badges > [ Get ]"
    elif BE.bought_characters[character.index] is True:
        equip = "Unlocked! > Equip"
    else:
        BE.write_log(
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
    # ! I should probably refactor this...
    return_value = " "
    location = BE.cur_location
    match what:
        case "left":
            if location[0] != 0:
                return_value = "!"
        case "right":
            if location[1] != 0:
                return_value = "!"
        case "down":
            if location[0] != 3:
                return_value = "!"
        case "up":
            if location[1] != 1:
                return_value = "!"
        case "task":
            if location == BE.cur_task.location:
                return_value = "!"
        case "get":
            # We will apply this added complexity later
            # in __main__.py
            match location:
                case [0, 0]:
                    return_value = "@"
                case [1, 1]:
                    return_value = "#"
                case [2, 1]:
                    if BE.animal_exists is True:
                        return_value = "&"
        case "acts":
            match act:
                case "sleep":
                    if BE.what_time == "Night" & BE.cur_location == [1, 0]:
                        return_value = "Z"
                case "ask":
                    if BE.done_task == False & BE.cur_location == [0, 1]:
                        return_value = "?"
                case _:
                    if (
                        check_act("get")
                        != " " | check_act("acts", "sleep")
                        != " " | check_act("acts", "ask")
                        != " "
                    ):
                        return_value = "!"
        case "wait":
            if BE.wait_cooldown <= 0:
                return_value = "!"
        case _:
            BE.write_log("(Not Fatal) Invalid check_act call")
    return return_value


# - IN GAME SPRITES -


def random_sprinkle(
    elements: list, chance: int = 10, height: int = 3, length: int = 64
) -> list:
    """
    A random sprinkler

    This returns a list of structure:
    [[], [], ... height]

    You should use this like:
    output = random_sprinkle(parameters)
    """
    chance = chance % 11
    output = []
    for i in range(0, height):
        output.append([])
        for _ in range(0, length):
            rng = randint(0, 10)
            output[i].append(
                elements[2] if rng > chance * 0.95
                else elements[1] if rng > chance * 0.8
                else elements[0]
            )
    return output


def insert_slice(target: list, start: int, text: str) -> None:
    """
    This inserts a slice of string to a list

    This is used for the random sprinkle method.
    As for you a normal human, can't do math.
    But a computer does! So why not let it do the work?
    """
    target[start:start + len(text)] = text


def join_lists(list_of_lists: list) -> str:
    """
    This expects a list of structure:
    [[], [], [] ...]
    
    And joins them to return their result of strings.
    This is for the random_sprinkler method to create
    the location sprites.
    """
    joined = ""
    for strings in list_of_lists:
        joined += "".join(strings) + "\n"
    return joined


# ? Hey contributers! Should I add in a comment
# ? for what the output could look like?
# ? For some readability, I could add it in the docstring.


def print_check_sprite(what: int) -> None:
    """
    This prints the check sprite

    The parameters are exactly the same as print_sky()
    0 for night, 1 for day

    It is standalone, you don't need to print() it
    """
    if what == 0:
        sky_elements = [" ", "*", "."]
    else:
        sky_elements = [":", ":", ";"]
    output = random_sprinkle(sky_elements, 9, 7)
    if what == 0:
        insert_slice(output[1], 28, ".----.")
        insert_slice(output[2], 27, "' .  ; '")
        insert_slice(output[3], 26, "| - () + |")
        insert_slice(output[4], 27, ". ( :  .")
        insert_slice(output[5], 28, "'----'")
    else:
        insert_slice(output[1], 28, ";----;")
        insert_slice(output[2], 27, "'      '")
        insert_slice(output[3], 26, "| < () > |")
        insert_slice(output[4], 27, ".      .")
        insert_slice(output[5], 29, "----")
    for i in range(7):
        print("".join(output[i]))


def print_sky(what: int, print_sprite: bool) -> None:
    """
    This should create the illusion of a random sky.

    No print() statement is needed for this function.
    It will print it on it's own.

    The what parameter should be:
    0 if BE.what_time == "Night" else 1

    The print_sprite parameter is self explanatory.
    It prints the sprite instead if it's True

    Or as configured in the intro,
    Whatever you want essentially.
    The default is the day sky
    """
    sky = [[], [], []]
    if what == 0:
        sky_elements = [" ", ".", "*"]
    else:
        sky_elements = [":", ";", ":"]
    sky = random_sprinkle(sky_elements)
    sky[0][57:63] = ".';o'."
    sky[1][57:63] = "'.',.'"
    if what != 0:
        for i in range(63):
            sky[2][i] = (
                (";" if randint(0, 10) > 8 else ":")
                if i % 2 == 1
                else ("`" if randint(0, 10) > 8 else "'")
            )
    sprite = join_lists(sky)
    if print_sprite is True:
        print(sprite, end="")
    return sprite


# - MAP SPRITES - ( omfg this takes too long )


def get_forest_entrance_sprite() -> str:
    r"""
    This returns the Forest Entrance sprite.

    #! I'll rework this don't worry... or not...

    I'm sorry okay? Is that what you want?
    I should maybe remove this small feature anyways...

    This returns an output of:
    /\^./\__./\_/\_.________________________________________________
      \\  \/ \ \  \ \                   '      "                  ' 
      \\  /  \ /  \ \.--------  -     -       "        '  "      '  
    ||| || |||| |||| |  .------   -     - ''   "   '   "'     '  "  
    """
    ground = [[], [], [], []]
    ground = random_sprinkle(elements=[' ', '"', "'"], height=4)
    insert_slice(ground[0], 0, "_" * 64)
    insert_slice(ground[0], 0, "/\\^./\\__./\\_/\\_.")
    insert_slice(ground[1], 0, "  \\\\  \\/ \\ \\  \\ \\")
    insert_slice(ground[2], 0, "  \\\\  /  \\ /  \\ \\.--------  -     -")
    insert_slice(ground[3], 0, "||| || |||| |||| |  .------   -     -")
    sprite = join_lists(ground)
    return sprite


def get_campsite_sprite() -> None:
    r"""
    This returns the Campsite sprite.

    Goodluck.

    This returns an output of:
    ______.-------.______,___'____________/\__^__/\_____/\__________
       ' / [  ] /||\    '  ' .    " "    /  \/ \/  \./\/  \ '  ""  '
        /______/_||_\     ('./ '' ' "- ."/  \ | /  \ \ \  \'.-------
    ' "   "'"  '    "    ./|\.     '-. "  ||"' ' ||'   \||  |  .----
    """
    ground = [[], [], [], []]
    ground = random_sprinkle(elements=[' ', '"', "'"], height=4)
    insert_slice(ground[0], 0, "_" * 64)
    insert_slice(ground[0], 6, ".-------.")
    insert_slice(ground[0], 21, ",___'")
    insert_slice(ground[0], 38, "/\\__^__/\\_____/\\")
    insert_slice(ground[1], 5, "/ [  ] /||\\")
    insert_slice(ground[1], 20, "'  ' .")
    insert_slice(ground[1], 37, "/  \\/ \\/  \\./\\/  \\")
    insert_slice(ground[2], 4, "/______/_||_\\")
    insert_slice(ground[2], 22, "('./")
    ground[2][33] = "-"
    ground[2][35] = "."
    insert_slice(ground[2], 37, "/  \\")
    ground[2][42] = "|"
    insert_slice(ground[2], 44, "/  \\ \\ \\  \\")
    insert_slice(ground[2], 56, ".-------")
    insert_slice(ground[3], 21, "./|\\.")
    insert_slice(ground[3], 32, "-.")
    insert_slice(ground[3], 38, "||")
    insert_slice(ground[3], 45, "||")
    insert_slice(ground[3], 51, "\\||")
    insert_slice(ground[3], 56, "|  .----")
    sprite = join_lists(ground)
    return sprite

Spawn_sprite: str = """
_____________________________________________________________________
"      "  '   "      '    "    "    '    "    '    "     "    '   "
  "      "  '   "      '    "    "    '    "    '    "     "    '   "
   "  '   "      '    "    "    '    "    '    "     "    '   "   ' "
"""

Cliff0_sprite: str = """
_____________________________________________________________________
"      "  '   "      '    "    "    '    "    '    "     "    '   "
  "      "  '   "      '    "    "    '    "    '    "     "    '   "
   "  '   "      '    "    "    '    "    '    "     "    '   "   ' "
"""

Altar_sprite: str = """
_____________________________________________________________________
"      "  '   "      '    "    "    '    "    '    "     "    '   "
  "      "  '   "      '    "    "    '    "    '    "     "    '   "
   "  '   "      '    "    "    '    "    '    "     "    '   "   ' "
"""

Small_Lake_sprite: str = """
_____________________________________________________________________
"      "  '   "      '    "    "    '    "    '    "     "    '   "
  "      "  '   "      '    "    "    '    "    '    "     "    '   "
   "  '   "      '    "    "    '    "    '    "     "    '   "   ' "
"""

Plains_sprite: str = """
_____________________________________________________________________
"      "  '   "      '    "    "    '    "    '    "     "    '   "
  "      "  '   "      '    "    "    '    "    '    "     "    '   "
   "  '   "      '    "    "    '    "    '    "     "    '   "   ' "
"""

Cliff1_sprite: str = """
_____________________________________________________________________
"      "  '   "      '    "    "    '    "    '    "     "    '   "
  "      "  '   "      '    "    "    '    "    '    "     "    '   "
   "  '   "      '    "    "    '    "    '    "     "    '   "   ' "
"""

location_sprites: list = [
    [get_forest_entrance_sprite(), get_campsite_sprite(), Spawn_sprite, Cliff0_sprite],
    [Altar_sprite, Small_Lake_sprite, Plains_sprite, Cliff1_sprite],
]


def fetch_main_acts() -> str:
    """
    This returns a main acts menu.

    Note that this RETURNS a menu.
    You will need to act_scroll() this so do not treat
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
    You will need to act_scroll() this so do not treat
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
    This returns the fast-travel menu

    Note that this RETURNS a menu.

    You will need to act_scroll() this.
    So do not treat this as a standalone function.
    """
    seen = BE.seen_locations
    forest = "FE" if seen[0][0] is True else "??"
    camp = "CS" if seen[0][1] is True else "??"
    spawn = "SP" if seen[0][2] is True else "??"
    cliff0 = "C0" if seen[0][3] is True else "??"
    altar = "AL" if seen[0][0] is True else "??"
    lake = "LA" if seen[0][1] is True else "??"
    plains = "PL" if seen[0][2] is True else "??"
    cliff1 = "C1" if seen[0][3] is True else "??"
    # I know, I was surprised it even lined up.
    return f"""
    <( FAST TRAVEL : )>

        (!) -> Fast Travel Consumes more stamina!
        [ ({forest}) ] >-< [ ({camp}) ] <-> [ ({spawn}) ] >-< [ ({cliff0}) ]
        [ ({altar}) ] <-> [ ({lake}) ] >-< [ ({plains}) ] <-> [ ({cliff1}) ]
"""
