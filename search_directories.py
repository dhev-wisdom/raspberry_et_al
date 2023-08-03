import os
from PIL import Image


# Pillow must be installed for this code solution to work
# Install Pillow with pip thus `pip install Pillow`
def find_image(dir):
    images_list = []

    for root, dirs, files in os.walk(dir):
        """
        os.walk generates a three element tuple - root, dirs and files
        """
        for file in files:
            """
            iterating through the files
            """
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                """
                first convert to lowercase to ensure consistency
                all possible image extensions
                """
                file_path = os.path.join(root, file)
                try:
                    """
                    attempt to open image file
                    """
                    with Image.open(file_path) as img:
                        width, height = img.size
                        """
                        if image opens, get width and height with .size and append img obj to image list
                        """
                        images_list.append({
                            'path': file_path,
                            'resolution': f'{width}x{height}'
                        })
                except (IOError, OSError, Image.DecompressionBombError):
                    """
                    saefely catch all errors
                    """
                    pass
    return images_list


if __name__ == '__main__':
    find_image(dir)
