# IconOrganizer

IconOrganizer is a Python program designed to help you keep your Windows desktop tidy by arranging desktop icons according to user-defined rules. With IconOrganizer, you can specify how files on your desktop should be sorted into folders based on their extensions.

## Features

- Organize desktop files into folders based on file extensions.
- Customize rules to define which file types should be moved to which folders.
- Simple configuration using a JSON file.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed on your system.
3. Install any required dependencies (none required for this basic version).

## Usage

1. Run the `icon_organizer.py` script.
2. Define your sorting rules by editing the `config.json` file or by using the `add_rule` method in the code.
3. Execute the script to organize your desktop files.

### Example Rules

You can specify rules directly in the script using `add_rule` method:

```python
organizer.add_rule('.txt', 'Text Files')
organizer.add_rule('.jpg', 'Images')
```

This will move all `.txt` files to a folder named "Text Files" and all `.jpg` files to a folder named "Images" on your desktop.

## Configuration

The program uses a `config.json` file to store and load your custom rules. If the file does not exist, it will be created automatically when you add your first rule.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgements

This project was inspired by the need to maintain a tidy and organized desktop environment.