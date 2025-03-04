import os
import sys

def get_filenames_from_directory(directory_path):
    """
    Extract and sort filenames without extension from the given directory.
    """
    filenames = []
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            name, _ = os.path.splitext(filename)
            filenames.append(name)
    filenames.sort()  # Sort the filenames alphabetically
    return filenames

def write_to_file(file_path, content, overwrite=False):
    """
    Write content to a file. Ask for overwrite permission if required.
    """
    if os.path.exists(file_path) and not overwrite:
        response = input(f"{file_path} already exists. Overwrite? (y/n): ").strip().lower()
        if response != 'y':
            print("Operation cancelled.")
            return
    with open(file_path, 'w') as file:
        file.write(content)

def main(overwrite=False):
    base_path = "./game"
    sections = {
        "# Characters": "images/characters",
        "# NPCs": "images/npcs",
        "# Sound effects": "audio/soundeffects",
        "# Background music": "audio/bcgsound",
        "# Backgrounds": "images/locations",
    }

    content = ""
    for section, path in sections.items():
        full_path = os.path.join(base_path, path)
        filenames = get_filenames_from_directory(full_path)
        content += section + "\n" + "\n".join(filenames) + "\n\n"

    write_to_file("interface.conf", content, overwrite)

if __name__ == "__main__":
    overwrite_flag = '-O' in sys.argv
    main(overwrite=overwrite_flag)

