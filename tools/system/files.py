import os
import shutil

def read_file(path):
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        return "Error: File not found."
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content):
    path = os.path.expanduser(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    return f"Success: Wrote to {path}"

def search_files(query, directory="."):
    directory = os.path.expanduser(directory)
    matches = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if query in file:
                matches.append(os.path.join(root, file))
    return matches

def list_dir(path="."):
    path = os.path.expanduser(path)
    return os.listdir(path)

def organize_dir(directory):
    """
    Organizes files in a directory into folders based on extensions.
    """
    directory = os.path.expanduser(directory)
    if not os.path.isdir(directory):
        return "Error: Path is not a directory."
    
    mapping = {
        "Documents": [".pdf", ".docx", ".txt", ".md", ".xlsx", ".csv"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Media": [".mp3", ".mp4", ".mov", ".wav"],
        "Code": [".py", ".js", ".html", ".css", ".go", ".c", ".cpp"],
        "Archives": [".zip", ".tar", ".gz", ".rar"]
    }
    
    count = 0
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            continue
            
        ext = os.path.splitext(filename)[1].lower()
        moved = False
        for folder, extensions in mapping.items():
            if ext in extensions:
                dest_dir = os.path.join(directory, folder)
                os.makedirs(dest_dir, exist_ok=True)
                shutil.move(filepath, os.path.join(dest_dir, filename))
                count += 1
                moved = True
                break
        
        if not moved and ext:
            dest_dir = os.path.join(directory, "Others")
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(filepath, os.path.join(dest_dir, filename))
            count += 1
            
    return f"Success: Organized {count} files in {directory}."
