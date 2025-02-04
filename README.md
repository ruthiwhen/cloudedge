# CloudEdge

CloudEdge is a simple Python application designed to customize your desktop wallpaper automatically at set intervals using a collection of user-defined images on Windows.

## Features

- Automatically cycles through wallpapers from a user-defined folder.
- Supports popular image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`.
- Allows for customizable intervals between wallpaper changes.
- Lightweight and easy to use.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Clone the repository or download the `cloudedge.py` file.
2. Ensure you have Python 3 installed on your system.
3. Install any dependencies using pip (if required).

## Usage

1. Set up a folder containing all your desired images for wallpapers.
2. Open the `cloudedge.py` file and update the `image_folder` variable with the path to your image folder.
3. Optionally, adjust the `interval_minutes` to change how often the wallpaper should change.
4. Run the script using the command:

   ```bash
   python cloudedge.py
   ```

## Customization

- **Image Folder**: Modify the `image_folder` variable in the script to point to the directory containing your images.
- **Interval**: Change the `interval_minutes` variable to set how often the wallpaper should change.

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute as needed.

## Disclaimer

This script is designed to work on Windows OS. Functionality on other operating systems is not guaranteed.