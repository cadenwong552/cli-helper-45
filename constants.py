import json

PLAYER_STATUS = {
    'ACTIVE': 'active',
    'INACTIVE': 'inactive',
    'BANNED': 'banned'
}

ITEM_TYPES = {
    'WEAPON': 'weapon',
    'ARMOR': 'armor',
    'POTION': 'potion'
}

LEVELS = {
    'BEGINNER': 1,
    'INTERMEDIATE': 2,
    'ADVANCED': 3
}

class GameConstants:
    @staticmethod
    def get_player_statuses():
        return json.dumps(PLAYER_STATUS)
    
    @staticmethod
    def get_item_types():
        return json.dumps(ITEM_TYPES)
    
    @staticmethod
    def get_levels():
        return json.dumps(LEVELS)