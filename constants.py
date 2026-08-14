from typing import Final

# Game constants

PLAYER_MAX_HEALTH: Final[int] = 100
PLAYER_MIN_HEALTH: Final[int] = 0
ENEMY_MAX_HEALTH: Final[int] = 150
ENEMY_MIN_HEALTH: Final[int] = 50

# Item constants

ITEM_HEALTH_POTION: Final[int] = 20
ITEM_MANA_POTION: Final[int] = 15

# Game settings

FPS: Final[int] = 60
MAX_PLAYERS: Final[int] = 4

# Game states

class GameState:
    MAIN_MENU: str = 'main_menu'
    IN_GAME: str = 'in_game'
    GAME_OVER: str = 'game_over'

    @classmethod
    def get_states(cls) -> list[str]:
        return [cls.MAIN_MENU, cls.IN_GAME, cls.GAME_OVER]  

# Player roles

class PlayerRole:
    WARRIOR: str = 'warrior'
    MAGE: str = 'mage'
    ARCHER: str = 'archer'

    @classmethod
    def get_roles(cls) -> list[str]:
        return [cls.WARRIOR, cls.MAGE, cls.ARCHER]