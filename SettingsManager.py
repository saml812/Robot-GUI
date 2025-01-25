import json
import os

class SettingsManager:
    def __init__(self, file_path="settings.json"):
        self.file_path = file_path
        self.default_settings = {
            "window": {"width": 1280, "height": 720},
            "theme": "System",
            "scale": 1.0
        }
        self.settings = self.load_settings()

    def load_settings(self):
        # Load settings from the JSON file or return default.
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, KeyError):
                pass  # If invalid, uses default
        return self.default_settings

    def save_settings(self):
        # Save settings to the JSON file.
        with open(self.file_path, "w") as file:
            json.dump(self.settings, file, indent=4)

    def update_setting(self, key, value):
        # Update a specific key-value pair.
        self.settings[key] = value