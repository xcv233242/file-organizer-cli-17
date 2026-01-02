import os
import shutil
import argparse

def organize_files(directory):
    """Moves files into folders named after their extensions."""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Get extension and determine destination
        extension = filename.split('.')[-1].lower() if '.' in filename else 'no_extension'
        dest_folder = os.path.join(directory, extension)

        # Create folder if it doesn't exist
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Move the file
        try:
            shutil.move(filepath, os.path.join(dest_folder, filename))
            print(f"Moved: {filename} -> {extension}/")
        except Exception as e:
            print(f"Failed to move {filename}: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organize files in a directory by their file extension.')
    parser.add_argument('path', nargs='?', default='.', help='The path to the directory to organize (default: current directory)')
    args = parser.parse_args()
    
    print(f"Organizing files in: {os.path.abspath(args.path)}")
    organize_files(args.path)
    print("Done!")