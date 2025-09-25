"""Import randint from module random"""
from random import randint as rng

# Goodluck.

class Stats:
    """
    The standard Stat class.

    This class holds the management of stats.

    Initializer is fairly self explanatory.
    Though extra variables are used:
    Current and Maximum variables are used to hold current and max values
    Drain variables are used to hold the amount of drain per time reset.
    """
    def __init__(
        self, health: int = 0, stamina: int = 0,
        drain_health: int = 0, drain_stamina: int = 0
        ) -> None:
        self.cur_health = self.max_health = health
        self.cur_stamina = self.max_stamina = stamina
        self.drain_health = drain_health
        self.drain_stamina = drain_stamina
    # Heals the player
    def heal(self, health: int = None, stamina: int = None) -> None:
        """
        The heal function heals the player by either a specified amount
        or a full recovery.
        """
        # Check if Health is None
        if health is None:
            # Heals max
            self.cur_health = self.max_health
        else:
            # Else heals by specified amount
            self.cur_health += health
            # Overflow check
            if self.cur_health > self.max_health:
                self.cur_health = self.max_health
        # Self Explanatory
        if stamina is None:
            self.cur_stamina = self.max_stamina
        else:
            self.cur_stamina += stamina
            if self.cur_stamina > self.max_stamina:
                self.cur_stamina = self.max_stamina
    # Similar to heal(), but drains stats instead
    def damage(self, health: int = None, stamina: int = None) -> None:
        """
        damage's parameters is similar to heal's, but instead of fully draining,
        it drains by the drain stat.
        """
        # Checks if it is not None
        if health is not None:
            # Drains by specified amount
            self.cur_health -= health
        else:
            # Else drains by the drain stat
            self.cur_health -= self.drain_health
        # Repeat
        if stamina is not None:
            self.cur_stamina -= stamina
        else:
            self.cur_stamina -= self.drain_stamina

class Task:
    """
    The standard Task class.

    This holds the logic for tasks.

    Initializer is straight forward.
    """
    def __init__(
        self, name: str, dialogue: list,
        guide: list, prize: int, location: list,
        drain: list
        ) -> None:
        self.name = name
        self.dialogue = dialogue
        self.guide = guide
        self.prize = prize
        self.location = location
        self.drain = drain
    def do_task(self, heard, location, stats) -> list:
        """
        This is the logic for toggling the task.

        Return Value is [done_task?, prize]

        If conditions are unmet it will return [False, 0].
        Else it will degrade the stats parameter by invoking
        the drain function given by the Stats class.
        """
        if heard is False or location != self.location:
            return [False, 0]
        stats.curHealth -= self.drain[0]
        stats.curStamina -= self.drain[1]
        return [True, self.prize]

class Item:
    """
    A fairly simple Item class.

    ? Should this even be here? It's so small!

    Self explanatory.
    It accepts only 2 parameters:
    Description and Heal.
    # I don't have any ideas for another item lol #
    """
    def __init__(
        self, description: str, heal: list
        ) -> None:
        self.description = description
        self.heal = heal
    # Use Item function
    def use(self, stats) -> None:
        """
        This invokes the heal function from the Stats class
        with the heal parameter given by the initializer.
        """
        stats.heal(self.heal[0], self.heal[1])

class Move:
    """
    A Battle Move class.


    """
    def __init__(
        self, name: str, mode: int,
        damageORheal: int, cooldown: int
        ) -> None:
        self.name = name
        self.mode = mode
        self.damageORheal = damageORheal
        self.cooldown = cooldown
        self.curCooldown = 0
    # Do move function
    def do(self, stats: Stats, itself: Stats):
        if self.mode == 1:
            itself.curHealth += self.damageORheal
            self.curCooldown = self.cooldown
            return
        stats.curHealth -= self.damageORheal
        self.curCooldown = self.cooldown

class MoveSet: # A set of class moves
    pass

class Character: # Standard character class
    def __init__(
        self, stats: Stats, name: str,
        head: str, body: str, description: str,
        price: int, index: int, moveSet: MoveSet
        ) -> None:
        self.stats = stats
        self.name = name
        self.head = head
        self.body = body
        self.description = description
        self.price = price
        self.index = index
        self.moveSet = moveSet
    # Buy selected Character
    def buy(self) -> None:
        global boughtCharacters, badges
        # Decrease badges by rpice
        badges -= self.price
        # Set it's bought value to true
        boughtCharacters[self.index] = True
    # Equip selected Characetr
    def equip(self) -> None:
        global curCharacter, curStats
        # Set Character Variable to character's name
        curCharacter = self.name
        # Set current stats to the class holder
        curStats = self

class Animal: # The standard enemy class
    def __init__(
        self, name: str, moveSet: MoveSet,
        stats: Stats, prize: int, meat: int
        ) -> None:
        self.name = name
        self.moveSet = moveSet
        self.stats = stats
        self.prize = prize
    # Choice algorithm
    def choice(self) -> Move:
        y = self.moveSet.moves[rng(0, 2)].curCooldown
        while y != 0:
            y = self.moveSet.moves[rng(0, 2)].curCooldown
        return y
