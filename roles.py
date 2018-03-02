role_types_list = ["chaos","counteractive","investigative","killing","protective","support"]
alignments = ["Good","Evil","Neutral"]
class Role():
	"""Skeleton code for roles in the game"""
    tags = []
    isUnique = False
    isHuman = True
    alignment = 2 # Default alignment for roles is Neutral
    role_types = [] # Numerical list of role types; corresponds to role type in role_types_list
    def __init__(self):
            if isUnique:
                    tags.append("Unique")
            tags.append(alignments[alignment])
            if isHuman:
                    tags.append("Human")
            for role_type in role_types:
            	tags.append(role_types_list[role_type])