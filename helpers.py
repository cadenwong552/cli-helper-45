from typing import Dict, List, Optional, Tuple
import random


def parse_game_command(command: str) -> Dict[str, Optional[str]]:
    """Parse user command for the gaming CLI.

    Splits the command and extracts action and optional target.
    """
    parts: List[str] = command.strip().lower().split(maxsplit=1)
    if not parts:
        return {"action": None, "target": None}
    action: str = parts[0]
    target: Optional[str] = parts[1] if len(parts) > 1 else None
    return {"action": action, "target": target}


def calculate_score(stats: Dict[str, int]) -> int:
    """Calculate player score using weighted sum.

    Creative approach: uses generator expression with default weights.
    """
    weights: Dict[str, float] = {"strength": 2.0, "agility": 1.5, "intelligence": 3.0}
    return sum(
        stat_value * weights.get(stat_name, 1.0)
        for stat_name, stat_value in stats.items()
    )


def simulate_battle(player_hp: int, enemy_hp: int, max_turns: int = 5) -> Tuple[int, int]:
    """Simulate battle rounds until max turns or defeat.

    Returns remaining HP for player and enemy.
    """
    current_player_hp: int = player_hp
    current_enemy_hp: int = enemy_hp
    for turn in range(max_turns):
        if current_enemy_hp <= 0 or current_player_hp <= 0:
            break
        enemy_damage: int = random.randint(5, 15)
        current_player_hp -= enemy_damage
        player_damage: int = random.randint(3, 12)
        current_enemy_hp -= player_damage
    return max(current_player_hp, 0), max(current_enemy_hp, 0)


def generate_quest_hint(level: int, available_quests: List[str]) -> Optional[str]:
    """Select a quest hint based on player level.

    Unusual filter: quests longer than level number.
    """
    filtered_quests: List[str] = [
        quest for quest in available_quests if len(quest) > level
    ]
    if not filtered_quests:
        return None
    return random.choice(filtered_quests)


def format_inventory(items: List[Tuple[str, int]]) -> str:
    """Format the inventory into a display string.

    Uses list comprehension for creative formatting.
    """
    if not items:
        return "Your inventory is empty."
    formatted_items: List[str] = [f"{name} ({count})" for name, count in items]
    return "Inventory: " + " | ".join(formatted_items)


def recursive_level_up(current_level: int, experience: int, max_level: int = 20) -> int:
    """Recursively compute new level based on experience.

    Unusual recursive approach for level calculation.
    """
    if current_level >= max_level:
        return max_level
    required_exp: int = current_level * 50
    if experience < required_exp:
        return current_level
    return recursive_level_up(current_level + 1, experience - required_exp, max_level)
