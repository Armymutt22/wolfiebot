role_types_list = [
    "chaos", "counteractive", "investigative", "killing", "protective",
    "support"
]
alignments = ["Good", "Evil", "Neutral"]
attack_save_types = ["Standard", "Strong", "Powerful", "Unstoppable"]
save_durations = ["active", "lunar", "queued"]


class Role():
    """Skeleton code for roles in the game"""
    tags = []
    isUnique = False
    isHuman = True
    alignment = 2  # Default alignment for roles is Neutral
    role_types = []  # corresponds to role type in role_types_list

    def __init__(self):
        if self.isUnique:
            self.tags.append("Unique")
        self.tags.append(alignments[self.alignment])
        if self.isHuman:
            self.tags.append("Human")
        for role_type in self.role_types:
            self.tags.append(role_types_list[role_type])


class Save():
    """Save class"""

    def __init__(self, save_type, duration):
        self.save_type = save_type
        self.duration = duration


class Player():
    """Player class:
        Handles saves, attacks, suicids and objectives
        """

    def init(self, role):
        self.role = role
        self.alignment = role.alignment
        self.objectives = role.objectives
        self.isAlive = True
        self.saves = role.saves

    def attacked(self, attack):
        for save in self.saves:
            if save.type >= attack.type:
                return "saved"
        self.isAlive = False
        return "killed"

    def suicide(self):
        self.isAlive = False
        return "Suicided"

    def isWinner(self, game_objectives):
        for objective in game_objectives:
            if objective in self.objectives:
                return True
        return False


class Seer(Role):
    """In-game Seer role"""
    name = "Seer"
    description = """
    Her silence, well, that's the worst part of it.
    She doesn't raise her voice, she doesn't cry out,
    it's just her deathly silence.
    Her silver pupils scan the room and they'll lock onto you.
    And she then she just points.
    There are no words, no anger, no sorrow - only the stare.
    And as you're being dragged away to the gallows, her apathy is unwavering.
    No smirks, no grins, just the cold and unfeeling gaze.
    And then, as the rope is being tightened around your neck,
    her silence is the last thing you'll ever hear.
    """
    objectives = ["good-standard"]
    alignment = 0
    role_types = [2]

    def __init__(self):
        super().__init__()

    def investigate(self, player):
        if player.alignment == 1 and not player.isInvestigated:
            return player.role.__name__, player.alignment, Save(1, 2)
        return player.role.__name__, player.alignment
