"""The backend, containing all the in game variables and logic"""

# Built-in modules
from random import randint
from time import strftime, localtime

# External modules
import backend.__classes__ as BEC

# Do I really have to explain this to you?

# - STATIC TASK VARIABLES -

CHOP_TREES: BEC.Task = BEC.Task(
    name="Chop Trees",
    dialogue=["Cut down trees for me.", "This will train you."],
    guide=[
        "Go to the forest entrance.",
        "I placed trees there.",
        "Cut them down for me.",
    ],
    prize=2,
    location=[0, 0],
    drain=[0, 6],
)

PRAISE_ME: BEC.Task = BEC.Task(
    name="Praise me",
    dialogue=["Hallelujah!", "Rejoice in my world!"],
    guide=["In my altar...", "Praise me!"],
    prize=1,
    location=[0, 1],
    drain=[0, 4],
)

# ! I plan to make this a special task
# ! that if the player eats an animal
# ! it will fail automatically
# ! and if the player does not eat an animal until the next day
# ! it will be completed automatically
# ! This needs a special use-case in __main__.py
DONT_EAT: BEC.Task = BEC.Task(
    name="Don't Eat",
    dialogue=[
        "You must Resist the temptation.",
        "Do not eat the animals.",
    ],
    guide=["Go to the plains.", "There are animalss there.", "Don't eat them."],
    prize=3,
    location=[2, 1],
    drain=[3, 6],
)

# ! This needs a special use-case in __main__.py
# ! Temporarily a normal task for now
SACRIFICE: BEC.Task = BEC.Task(
    name="Sacrifice",
    dialogue=["Give me goats.", "Their blood, my creation."],
    guide=["Go to the cliff.", "Bring me a goat.", "Sacrfice it."],
    prize=6,
    location=[3, 0],
    drain=[0, 4],
)

BAPTISM: BEC.Task = BEC.Task(
    name="Baptism",
    dialogue=["You must be cleansed.", "Baptism is the way."],
    guide=["Go to the lake.", "Baptise yourself."],
    prize=2,
    location=[1, 1],
    drain=[0, 6],
)

CELEBRATE: BEC.Task = BEC.Task(
    name="Celebrate",
    dialogue=["Rejoice in my world.", "Hallelujah!"],
    guide=["Go to your camp.", "Celebrate with me."],
    prize=1,
    location=[1, 0],
    drain=[0, 4],
)

TASK_LIST: list = [CHOP_TREES, PRAISE_ME, DONT_EAT, SACRIFICE, BAPTISM, CELEBRATE]

# Holy Water Creation Task Soon (Special Task)

# - UNIMPLEMENTED CLASSES - (until 0.3.1)

# Weapons
# Items
# Inventory
# Locations (Map)

# - STATIC ENEMY VALUES -

COW_ENEMY: BEC.Animal = BEC.Animal(
    name="Cow",
    move_set=BEC.MoveSet(
        name="Instincts.",
        moves=[
            BEC.Move("Ram", 0, 4, 0),
            BEC.Move("Rest", 1, 8, 1),
            BEC.Move("Kick", 0, 12, 2),
        ],
    ),
    stats={30},
    prize=2,
    meat=3,
)

SHEEP_ENEMY: BEC.Animal = BEC.Animal(
    name="Cow",
    move_set=BEC.MoveSet(
        name="Instincts.",
        moves=[
            BEC.Move("Ram", 0, 2, 0),
            BEC.Move("Rest", 1, 8, 0),
            BEC.Move("Kick", 0, 10, 2),
        ],
    ),
    stats={35},
    prize=1,
    meat=2,
)

GOAT_ENEMY: BEC.Animal = BEC.Animal(
    name="Goat",
    move_set=BEC.MoveSet(
        name="Instincts.",
        moves=[
            BEC.Move("Kick", 0, 6, 1),
            BEC.Move("Preperation", 1, 6, 0),
            BEC.Move("Horn Ram", 0, 16, 3),
        ],
    ),
    stats={45},
    prize=3,
    meat=5,
)

# - STATIC CHARACTER VALUES -

NEWBIE_STATS: BEC.Character = BEC.Character(
    stats=BEC.Stats(20, 15, 0, 2),
    name="Newbie",
    head=" o ",
    body="/|\\",
    description="My first creation.",
    price=0,
    index=0,
    move_set=BEC.MoveSet(
        name="Instincts.",
        moves=[
            BEC.Move("Punch", 0, 2, 0),
            BEC.Move("Kick", 0, 3, 1),
            BEC.Move("Thrust", 0, 12, 4),
        ],
    ),
)

EXPERT_STATS: BEC.Character = BEC.Character(
    stats=BEC.Stats(45, 25, 0, 3),
    name="Expert",
    head="<+>",
    body="/|\\",
    description="Long forgotten.",
    price=10,
    index=1,
    move_set=BEC.MoveSet(
        name="Kung Fu.",
        moves=[
            BEC.Move("Fist Hit", 0, 3, 0),
            BEC.Move("Spin Kick", 0, 5, 1),
            BEC.Move("Power Fist", 0, 16, 3),
        ],
    ),
)

SUSTAINER_STATS: BEC.Character = BEC.Character(
    stats=BEC.Stats(60, 20, 1, 4),
    name="Sustainer",
    head="[@]",
    body="/U\\",
    description="Gluttony.",
    price=15,
    index=2,
    move_set=BEC.MoveSet(
        name="Sumo.",
        moves=[
            BEC.Move("Crush", 0, 3, 0),
            BEC.Move("Smash", 0, 5, 1),
            BEC.Move("Push", 0, 20, 4),
        ],
    ),
)

FALLEN_STATS: BEC.Character = BEC.Character(
    stats=BEC.Stats(30, 1, 2, 0),
    name="Fallen",
    head="{*}",
    body="'|'",
    description="Im sorry angel.",
    price=30,
    index=3,
    move_set=BEC.MoveSet(
        name="Divine Power.",
        moves=[
            BEC.Move("Divine Bolt", 0, 6, 0),
            BEC.Move("Holy Smite", 0, 18, 1),
            BEC.Move("God's Will", 0, 100, 3),
        ],
    ),
)

# - DYNAMIC BACKEND VARIABLES -

# Character Bought List
# False = Not Bought | True = Bought
bought_characters: list = [True, False, False, False]

name: str = "Player"
badges: int = 0
cur_stats: BEC.Character = NEWBIE_STATS

has_loaded: bool = False

cur_location: list = [0, 0]
cur_animal: BEC.Animal = None
cur_task: BEC.Task = None

game_time: int = 0
cur_time: int = 0
what_time: str = "Day"
can_sleep: bool = False

done_task: bool = False
heard_task: bool = False
animal_exists: bool = False
wait_cooldown: int = 0

deaths: int = 0

seen_locations: list = [[False, False, True, False], [False, False, False, False]]
LOCATION_NAMES: list = [
    ["The Forest Entrance.", "My Campsite.", "The Spawn.", "A Cliff."],
    ["His Altar.", "A Small Lake.", "The Plains.", "The Waterfall."],
]
keybind_list: list = [
    ["move", "acts", "task", "wait", "bag"],
    ["left", "right", "up", "down"],
    ["ask", "sleep", "check", "get"],
    ["menu", "back"],
]

# - DEBUGGING -


def write_log(message: str = "(?) Log called but no messages") -> None:
    """
    This writes to a log file in backend/logFile/log.txt

    I will refactor the log to be more readable in the next patch

    It follows this structure:
    [time] - (type) message
    for example:
    [12:00:00] - (FATAL) unknown error saving game
    or
    [12:00:00] - (not fatal) Save File not found, creating

    and for attempts to a try except
    [12:00:00] - (attempt) Saving Game...
    """
    current_time = strftime("%H:%M:%S", localtime())
    try:
        with open("src/backend/logFile/__log__.txt", "a", encoding="utf-8") as file:
            file.write(f"[{current_time}] - {message}\n")
    except FileNotFoundError:
        with open("src/backend/logFile/__log__.txt", "x", encoding="utf-8") as file:
            file.close()
        write_log(message)
    except Exception as e:
        raise e


# - IF RETURN -


def check_death() -> int:
    """
    Checks for death to prevent repitition in __main__.py

    If current_health is below 1
    it returns 1 as in ACTUAL DEATH

    If current_stamina is below 1
    it returns 2 as in passing out
    it does not affect the death counter

    However if all fails, it returns 0
    As in not dead.
    """
    if cur_stats.stats.curHealth <= 0:
        return 1
    if cur_stats.stats.curStamina <= 0:
        return 2
    return 0


def return_task() -> BEC.Task:
    """
    This will return a task at random

    It creates a list "task_list"
    And returns a Task from that list
    at index randint(0, length of task_list)
    """
    return TASK_LIST[randint(0, len(TASK_LIST) - 1)]


# - UPDATE FUNCTIONS -


def update_time_values(time: int, what: str, sleep: bool) -> list:
    """
    Updates time variables

    This returns a list of structure:
    [time, what_time, can_sleep, return_value]

    return_value cases:
    0 = Do not degrade stats with cur_stats.stats.drain()
    1 = Do drain stats with cur_stats.stats.drain()
    """
    ctime = time % 4
    if time == 0:
        return [ctime, None, None, 0]
    if time > 12:
        time = 0
        what = "Day" if what == "Night" else "Night"
        sleep = False if sleep is True else False
        return [ctime, what, sleep, 0]
    if ctime == 0:
        return [ctime, None, None, 1]
    return 0


def move_game_time(
    amount: int = 1,
    time: int = None,
    what: str = None,
    sleep: bool = None,
    wait: int = 0,
) -> list:
    """
    The main function to move game time

    This returns a list of structure:
    [cur_time, what_time, wait_cooldown]

    If parameter amount is 0
    It will move time back 4 hours to emulate sleep
    and heal the player in the process

    Else it will move time forward by a specified amount
    And invokes the update_time_values() function to update time variables

    If the return_value is 0, it will invoke cur_stats.stats.damage()
    to degrade the player's stats
    """
    if amount == 0:
        time -= 4
        if time < 0:
            time += 12
        elif time > 12:
            time -= 12
        what = "Day" if what == "Night" else "Night"
        x = update_time_values(time, what, sleep)
        time = x[0]
        what = x[1]
        sleep = x[2]
        cur_stats.stats.heal()
        return [time, what, 0]
    if amount != 1:
        time += amount
        wait = amount
        x = update_time_values(time, what, False)
        if x[3] == 0:
            cur_stats.stats.damage()
        return [time, what, wait]
    time += amount
    x = update_time_values(time, what, False)
    wait = 1 if wait <= 0 else wait
    if x[3] == 0:
        cur_stats.stats.damage()
    return [time, what, wait - 1]


# initialize variables sent to the shadow realm.


# - SAVE FILE SHENANIGANS -


def save_game() -> None:
    """
    This saves the game to a file named "__save__.txt"
    Located in backend/saveFile

    It saves all essential backend variables
    In a structure that follows below:
    keybinds...
    bought characters...
    badges
    cur stats index
    name
    cur stats current health
    cur stats current stamina
    cur location x
    cur location y
    cur task
    game time
    done task
    animal exists
    deaths

    If file does not exist a failsafe is incurred
    and will create the file then repeat the process

    If a known error occurs
    It raises the error to be handled in __main__.py
    To continue the game without saving

    Else if an unknown error occurs
    It raises the error for the python interpreter to handle
    """
    try:
        write_log("(Attempt) Saving Game...")
        with open("backend/saveFile/__save__.txt", "w", encoding="utf-8") as file:
            for x in enumerate(keybind_list):
                for y in enumerate(keybind_list[x]):
                    file.write(f"{keybind_list[x][y]}\n")
            for x in bought_characters:
                file.write(f"{x}\n")
            file.write(f"{name}\n")
            file.write(f"{badges}\n")
            file.write(f"{cur_stats.index}\n")
            file.write(f"{cur_stats.name}\n")
            file.write(f"{cur_stats.stats.curHealth}\n")
            file.write(f"{cur_stats.stats.curStamina}\n")
            file.write(f"{cur_location[0]}\n")
            file.write(f"{cur_location[1]}\n")
            file.write(f"{cur_task}\n")
            file.write(f"{game_time}\n")
            file.write(f"{done_task}\n")
            file.write(f"{animal_exists}\n")
            file.write(f"{deaths}\n")
    except FileNotFoundError:
        write_log("(Not Fatal) Save File not found, creating new file")
        with open("src/backend/saveFile/__save__.txt", "x", encoding="utf-8") as file:
            file.close()
        save_game()
    except Exception as e:
        write_log("(FATAL) Unknown error saving game with exit code: " + e)
        raise e


def load_save() -> dict:
    """
    This loads the game from a file named "__save__.txt"
    Located in backend/saveFile

    It loads all essential backend variables
    Read the save_game function DOCSTRING for the structure

    It first checks if the file exists or it has something inside.
    If it doesn't exist or is empty, it will still run nonetheless.
    As it doesn't need to load anything.

    Else if an unknown error occurs no failsafe will be incurred
    and it raises the error for the python interpreter to handle.

    It will return a dictionary.
    It's keywords are:
    keybinds, bought, badges, location, curtask, gametime,
    donetask, animalexists, deaths

    This saves a global statement
    and it is to be unpacked in __main__.py
    """
    try:
        write_log("(Attempt) Loading Game...")
        save_var = {
            "keybinds": [],
            "bought": [],
            "name": "",
            "badges": 0,
            "location": [],
            "curtask": False,
            "gametime": 0,
            "donetask": False,
            "animalexists": False,
            "deaths": 0,
        }
        i = 0
        with open("src/backend/saveFile/__save__.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) < 29:
                write_log("(Not Fatal) Save File is empty or corrupted, skipping load")
                return {}
            for x in enumerate(keybind_list):
                save_var["keybinds"].append([])
                for y in enumerate(keybind_list[x]):
                    save_var["keybinds"][x][y] = lines[i]
                    i += 1
            for z in range(4):
                save_var["bought"][z] = lines[z + 14].strip() == "True"
            save_var["badges"] = int(lines[18].strip())
            cur_stats.index = int(lines[189].strip())
            cur_stats.name = lines[20].strip()
            cur_stats.stats.curHealth = int(lines[21].strip())
            cur_stats.stats.curStamina = int(lines[22].strip())
            save_var["location"] = [int(lines[23].strip()), int(lines[24].strip())]
            save_var["curtask"] = lines[25].strip()
            save_var["gametime"] = int(lines[26].strip())
            save_var["donetask"] = lines[27].strip() == "True"
            save_var["animalexists"] = lines[28].strip() == "True"
            save_var["deaths"] = int(lines[29].strip())
        return save_var
    except FileNotFoundError:
        write_log("(Not Fatal) Save File not found, skipping load")
        return {}
    except Exception as e:
        write_log("(FATAL) Unknown error loading game with exit code: " + e)
        raise e
