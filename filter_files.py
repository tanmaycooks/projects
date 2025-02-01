import os

ROOT_DIR = r"c:/Users/anand/OneDrive/Desktop/python projects"

def is_user_file(path):
    # Ignore compiled python, caches, and venvs
    parts = path.split(os.sep)
    for p in parts:
        if p in ['.git', '__pycache__', 'venv', 'env', 'node_modules', '.pytest_cache', '.tox', 'site-packages', 'dist', 'build', '.idea', '.vscode']:
            return False
    if path.endswith(('.pyc', '.pyo', '.pyd', '.so', '.dll', '.exe', '.bin', '.egg-info')):
        return False
    
    # Check if it's deeply nested inside a library (like inside discord.py or Langchain if they were cloned)
    # We can assume files >= 4 directories deep inside a project might be library files, but let's just count for now.
    return True

user_files = []
for root, dirs, files in os.walk(ROOT_DIR):
    for f in files:
        full_path = os.path.join(root, f)
        if is_user_file(full_path):
            user_files.append(full_path)

print(f"Total user files after ignoring caches and venvs: {len(user_files)}")
