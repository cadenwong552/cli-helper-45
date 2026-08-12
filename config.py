import os

class Config:
    def __init__(self):
        self.settings = {
            'WINDOW_WIDTH': self.get_env_variable('WINDOW_WIDTH', 800),
            'WINDOW_HEIGHT': self.get_env_variable('WINDOW_HEIGHT', 600),
            'FPS': self.get_env_variable('FPS', 60),
            'DEBUG': self.get_env_variable('DEBUG', False, as_bool=True),
            'RESOURCE_PATH': self.get_env_variable('RESOURCE_PATH', 'resources')
        }

    def get_env_variable(self, var_name, default, as_bool=False):
        value = os.getenv(var_name, default)
        return value.lower() == 'true' if as_bool and isinstance(value, str) else value

    def __getitem__(self, key):
        return self.settings.get(key)

    def __setitem__(self, key, value):
        self.settings[key] = value

config = Config()