import os

def list_folders(path):
    """List all folders inside the given path."""
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    return folders

def create_folders(base_path, num):
    """Create numbered folders inside the chosen folder."""
    exercise_num = input("Exercise #: ")
    for i in range(1, num + 1):
        folder_name = os.path.join(base_path, f"Exercise {exercise_num}-{i}")
        os.makedirs(folder_name, exist_ok=True)
        print(f"Created: {folder_name}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))

    folders = list_folders(script_dir)

    if not folders:
        print("No folders found in this directory.")
    else:
        print("\nAvailable folders:")
        for idx, folder in enumerate(folders, start=1):
            print(f"{idx}. {folder}")

        try:
            choice = int(input("\nSelect a folder by number: "))
            if 1 <= choice <= len(folders):
                target_folder = os.path.join(script_dir, folders[choice - 1])
                num = int(input("Enter number of subfolders to create: "))
                create_folders(target_folder, num)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

