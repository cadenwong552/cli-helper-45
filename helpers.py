from typing import List, Dict


def calculate_score(player_actions: List[str]) -> Dict[str, int]:
    """
    Calculate the total score based on player actions.

    Args:
        player_actions (List[str]): A list of actions performed by the player.

    Returns:
        Dict[str, int]: A dictionary with action names as keys and their respective scores as values.
    """
    score: Dict[str, int] = {}
    score['attack'] = sum(1 for action in player_actions if action == 'attack') * 10
    score['defend'] = sum(1 for action in player_actions if action == 'defend') * 5
    score['heal'] = sum(1 for action in player_actions if action == 'heal') * 8
    return score


def apply_bonus(score: Dict[str, int], bonus_multiplier: float) -> Dict[str, int]:
    """
    Apply a bonus multiplier to the scores.

    Args:
        score (Dict[str, int]): The current score of the player.
        bonus_multiplier (float): The multiplier to apply to the score.

    Returns:
        Dict[str, int]: The updated score after applying the bonus.
    """
    return {action: int(value * bonus_multiplier) for action, value in score.items()}


def display_scores(score: Dict[str, int]) -> None:
    """
    Print the scores in a formatted way.
    
    Args:
        score (Dict[str, int]): The scores to display.
    """
    for action, value in score.items():
        print(f"{action.capitalize()}: {value}")