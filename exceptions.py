import sys
import time
import random

class GamingException(Exception):
    """Base exception for the cli-helper-45 gaming companion."""
    def __init__(self, message="An unexpected boss appeared!", code=500):
        super().__init__(message)
        self.code = code
        self.timestamp = time.time()

    def show_game_over(self):
        banner = (
            "=================================\n"
            f" 🔴 GAME OVER: {self.__class__.__name__}\n"
            f" Reason: {self}\n"
            "================================="
        )
        return banner

class OutOfManaError(GamingException):
    """Raised when rate limits or API requests are exhausted."""
    def __init__(self, message="Not enough Mana to cast this command!", cooldown=5):
        super().__init__(message, code=429)
        self.cooldown = cooldown

    def drink_potion(self):
        """Creative recovery mechanism: simulates resting/cooldown."""
        for i in range(self.cooldown, 0, -1):
            sys.stdout.write(f"\r🧪 Drinking mana potion... {i}s remaining...")
            sys.stdout.flush()
            time.sleep(1)
        print("\n✨ Mana restored! Ready to retry.")

class InventoryFullError(GamingException):
    """Raised when temporary directories or cache size limit is exceeded."""
    def __init__(self, message="Your inventory is full! Discard items (clear cache)."):
        super().__init__(message, code=507)

    def auto_discard(self, target_list):
        """Randomly drops a low-value item to free space."""
        if target_list:
            discarded = target_list.pop(random.randrange(len(target_list)))
            print(f"🗑️ Discarded junk item: '{discarded}' from inventory.")
            return discarded
        return None

class BossFightFailedError(GamingException):
    """Raised when an external gaming API or subprocess crashes/fails."""
    def __init__(self, boss_name, loot_lost=None):
        message = f"Defeated by {boss_name}! You lost: {loot_lost or 'common loot'}."
        super().__init__(message, code=502)
        self.boss_name = boss_name
