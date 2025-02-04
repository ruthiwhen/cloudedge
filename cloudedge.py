import os
import ctypes
import time
from datetime import datetime, timedelta
from threading import Timer

class CloudEdge:
    def __init__(self, image_folder, interval_minutes=60):
        self.image_folder = image_folder
        self.interval = timedelta(minutes=interval_minutes)
        self.images = self._load_images()
        self.current_index = 0

    def _load_images(self):
        """Load images from the specified directory."""
        supported_formats = ('.jpg', '.jpeg', '.png', '.bmp')
        images = [os.path.join(self.image_folder, img) for img in os.listdir(self.image_folder) if img.lower().endswith(supported_formats)]
        if not images:
            raise ValueError(f"No supported image formats found in {self.image_folder}")
        return images

    def set_wallpaper(self, image_path):
        """Set the desktop wallpaper to the specified image."""
        print(f"Setting wallpaper to: {image_path}")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

    def _cycle_wallpaper(self):
        """Cycle through the images and update the wallpaper."""
        self.current_index = (self.current_index + 1) % len(self.images)
        self.set_wallpaper(self.images[self.current_index])
        next_cycle = datetime.now() + self.interval
        Timer((next_cycle - datetime.now()).total_seconds(), self._cycle_wallpaper).start()

    def start(self):
        """Start cycling the wallpapers."""
        if not self.images:
            print("No images to display.")
            return
        self.set_wallpaper(self.images[self.current_index])
        next_cycle = datetime.now() + self.interval
        Timer((next_cycle - datetime.now()).total_seconds(), self._cycle_wallpaper).start()

if __name__ == "__main__":
    image_folder = "path/to/your/image/folder"  # Replace with your image folder path
    interval_minutes = 60  # Set the interval in minutes
    cloud_edge = CloudEdge(image_folder, interval_minutes)
    cloud_edge.start()