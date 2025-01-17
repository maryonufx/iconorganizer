import os
import shutil
import json
from pathlib import Path

class IconOrganizer:
    def __init__(self, config_file='config.json'):
        self.desktop_path = Path(os.path.join(os.path.expanduser("~"), "Desktop"))
        self.config_file = config_file
        self.rules = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_file):
            return {}
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.rules, file, indent=4)

    def add_rule(self, extension, folder_name):
        self.rules[extension] = folder_name
        self.save_config()

    def organize_icons(self):
        for item in self.desktop_path.iterdir():
            if item.is_file():
                extension = item.suffix.lower()
                if extension in self.rules:
                    self.move_file(item, self.rules[extension])

    def move_file(self, file_path, folder_name):
        target_folder = self.desktop_path / folder_name
        if not target_folder.exists():
            target_folder.mkdir()

        target_path = target_folder / file_path.name
        shutil.move(file_path, target_path)
        print(f"Moved {file_path.name} to {target_folder}")

    def run(self):
        print("Organizing desktop icons...")
        self.organize_icons()
        print("Done!")

if __name__ == "__main__":
    organizer = IconOrganizer()
    # Example rules, add as needed
    organizer.add_rule('.txt', 'Text Files')
    organizer.add_rule('.jpg', 'Images')
    organizer.run()