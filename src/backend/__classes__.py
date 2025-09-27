"""
The classes of the backend

I seperated them so you could read __backend__ properly <3
"""
from random import randint

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

    ? This one too! It's small!

    Initializer seems complex.
    It accepts 4 parameters:
    name = The name of the move
    mode = 0 for damage, 1 for heal
    damage_or_heal = The amount of damage or heal
    cooldown = The amount of turns before it can be used again
    
    It also has a cur_cooldown variable to hold the current cooldown.
    """
    def __init__(
        self, name: str, mode: int,
        damage_or_heal: int, cooldown: int
        ) -> None:
        self.name = name
        self.mode = mode
        self.damage_or_heal = damage_or_heal
        self.cooldown = cooldown
        self.cur_cooldown = 0
    # Do move function
    def do(self, stats: Stats, itself: Stats):
        """
        This is the logic for the move.

        It checks if it's mode is either 1 or 0.
        If it's 1, it heals the user by invoking the heal function
        given by the itself parameter.
        If it's 0, it damages the opponent by invoking the damage function
        given by the stats parameter.
        """
        if self.mode == 1:
            itself.curHealth += self.damage_or_heal
            self.cur_cooldown = self.cooldown
            return
        stats.curHealth -= self.damage_or_heal
        self.cur_cooldown = self.cooldown

class MoveSet:
    """
    This class will contain 3 move classes

    Initializer will only contain one parameter:
    moves = A list of 3 move classes
    """
    def __init__(self, moves: list) -> None:
        self.moves = moves
    def next_move(self) -> None:
        """
        This uses a for loop to iterate through the moves
        and decrease their cooldown by 1 if they are above 0.

        ? Is this efficient?
        """
        for move in self.moves:
            move.cur_cooldown -= 1 if move.cur_cooldown > 0 else 0

class Character:
    """
    The Character class.

    This class holds the logic for your characters.

    Initializer is fairly self explanatory.
    It accepts several parameters:
    stats = The stats class holder
    name = The name of the character
    head = The head sprite of the character
    body = The body sprite of the character
    description = The description of the character
    price = The price of the character
    index = The index of the character in the boughtCharacters list
    move_set = The move set class holder

    This heavily relies on functions managing it.
    It will only contain 1 function:
    It's buy function.

    Any other modifications require direct access.
    """
    def __init__(
        self, stats: Stats, name: str,
        head: str, body: str, description: str,
        price: int, index: int, move_set: MoveSet
        ) -> None:
        self.stats = stats
        self.name = name
        self.head = head
        self.body = body
        self.description = description
        self.price = price
        self.index = index
        self.move_set = move_set
    def buy(self, badges, bought) -> None:
        """
        The buy function checks if the player has enough badges
        and if the character is already bought.

        Return Value is [bought?, remaining_badges]

        If conditions are unmet it will return [False, badges].
        Else it will return [True, badges - price].
        """
        if badges < self.price or bought[self.index] is True:
            return [False, badges]
        return [True, badges - self.price]

class Animal:
    """
    The Animal Class.

    This class holds the simple logic for animals.
    It serves as a simple enemy.

    Initializer has only 5 Parameters:
    name = The name of the animal
    move_set = The move set class holder
    stats = The stats class holder
    prize = The amount of badges given when defeated
    meat = The amount of meat given when defeated

    Note that prize and meat are stored in a list.

    ! I will add more battle features for more variety later!
    """
    def __init__(
        self, name: str, move_set: MoveSet,
        stats: Stats, prize: int, meat: int
        ) -> None:
        self.name = name
        self.move_set = move_set
        self.stats = stats
        self.prize = [prize, meat]
    # Choice algorithm
    def choice(self) -> Move:
        """
        Will return a random move that is not on cooldown.

        It uses the randint function imported from the random module.
        No cases for if all moves are on cooldown.
        Since atleast ONE move has no cooldown

        ! I should refactor this
        """
        y = self.move_set.moves[randint(0, 2)].curCooldown
        while y != 0:
            y = self.move_set.moves[randint(0, 2)].curCooldown
        return y
