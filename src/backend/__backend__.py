"""Import Backend Classes"""
import backend.__classes__ as BEC

# Do I really have to explain this to you?

# - STATIC TASK VARIABLES -

chop_trees: BEC.Task = BEC.Task(
    name="Chop Trees",
    dialogue=[
        "Cut down trees for me.",
        "This will train you."
    ],
    guide=[
        "Go to the forest entrance.",
        "I placed trees there.",
        "Cut them down for me."
    ],
    prize=2,
    location=[0, 0],
    drain=[0, 6]
)

praise_me: BEC.Task = BEC.Task(
    name="Praise me",
    dialogue=[
        "Hallelujah!",
        "Rejoice in my world!"
    ],
    guide=[
        "In my altar...",
        "Praise me!"
    ],
    prize=1,
    location=[0, 1],
    drain=[0, 4]
)



# - STATIC ENEMY VALUES -

cow_enemy: BEC.Animal = BEC.Animal(
    name="Cow",
    moveSet={
        "Instincts.",
        BEC.Move("Ram", 0, 4, 0),
        BEC.Move("Rest", 1, 8, 1),
        BEC.Move("Kick", 0, 12, 2)
    },
    stats={30},
    prize=2,
    meat=3
)

sheep_enemy: BEC.Animal = BEC.Animal(
    name="Cow",
    moveSet={
        "Instincts.",
        BEC.Move("Ram", 0, 2, 0),
        BEC.Move("Rest", 1, 8, 0),
        BEC.Move("Kick", 0, 10, 2)
    },
    stats={35},
    prize=1,
    meat=2
)

goat_enemy: BEC.Animal = BEC.Animal(
    name="Goat",
    moveSet={
        "Instincts.",
        BEC.Move("Kick", 0, 6, 1),
        BEC.Move("Preperation", 1, 6, 0),
        BEC.Move("Horn Ram", 0, 16, 3)
    },
    stats={45},
    prize=3,
    meat=5
)

# - STATIC CHARACTER VALUES -

newbie_stats: BEC.Character = BEC.Character(
    stats={20, 15, 0, 2},
    name="Newbie",
    head=" o ",
    body="/|\\",
    description="My first creation.",
    price=0,
    index=0,
    moveSet={
        "Instincts.",
        BEC.Move("Punch", 0, 2, 0),
        BEC.Move("Kick", 0, 3, 1),
        BEC.Move("Thrust", 0, 12, 4)
    }
)

expert_stats: BEC.Character = BEC.Character(
    stats={45, 25, 0, 3},
    name="Expert",
    head="<+>",
    body="/|\\",
    description="Long forgotten.",
    price=10,
    index=1,
    moveSet={
        "Kung Fu.",
        BEC.Move("Fist Hit", 0, 3, 0),
        BEC.Move("Spin Kick", 0, 5, 1),
        BEC.Move("Power Fist", 0, 16, 3)
    }
)

sustainer_stats: BEC.Character = BEC.Character(
    stats={60, 20, 1, 4},
    name="Sustainer",
    head="[@]",
    body="/U\\",
    description="Gluttony.",
    price=15,
    index=2,
    moveSet={
        "Sumo.",
        BEC.Move("Crush", 0, 3, 0),
        BEC.Move("Smash", 0, 5, 1),
        BEC.Move("Push", 0, 20, 4)
    }
)

fallen_stats: BEC.Character = BEC.Character(
    stats={30, 1, 2, 0},
    name="Fallen",
    head="{*}",
    body="'|'",
    description="Im sorry angel.",
    price=30,
    index=3,
    moveSet={
        "Divine Power.",
        BEC.Move("Divine Bolt", 0, 6, 0),
        BEC.Move("Holy Smite", 0, 18, 1),
        BEC.Move("God's Will", 0, 100, 3)
    }
)

# - DYNAMIC BACKEND VARIABLES -

# Character Bought List
# False = Not Bought | True = Bought
bought_characters: list = [True, False, False, False]

badges: int = 0
cur_stats: BEC.Character = newbie_stats

cur_location: list = [0, 0]
cur_task: BEC.Task = None

game_time: int = 0
cur_time: int = 0
what_time: str = "Day"

can_sleep: bool = False
done_task: bool = False
heard_task: bool = False
animal_exists: bool = False
can_wait: bool = True

deaths: int = 0

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
    time = time % 4
    if time == 0:
        return [time, None, None, 0]
    if time > 12:
        time = 0
        what = "Day" if what == "Night" else "Night"
        sleep = False if sleep is True else False
        return time, time, sleep, 0
    if time == 0:
        return [time, None, None, 1]
    return 0

# def mvGTime(amount: int = 1) -> None:
#     global GTime, WTime
#     if amount == 0:
#         GTime -= 4
#         if GTime < 0:
#             GTime += 12
#         elif GTime > 12:
#             GTime -= 12
#         WTime = "Day"
#         updTVal()
#         # initVar()
#         curStats.stats.heal()
#         return
#     GTime += amount
#     x = updTVal()
#     if x == 0:
#         curStats.stats.damage()
