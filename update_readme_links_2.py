import os
import re

ROOT_DIR = r"c:\Users\anand\OneDrive\Desktop\python projects"
OLD_REPO_PATTERN = re.compile(r'https://github\.com/tanmaycooks/PYTHON_PROJECTSSSS\.git', re.IGNORECASE)
NEW_REPO_URL = "https://github.com/tanmaycooks/projects.git"

print(f"Starting README link update in {ROOT_DIR}...")
modified_count = 0

for root, dirs, files in os.walk(ROOT_DIR):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'venv' and d != '__pycache__']
    
    for file in files:
        if file.lower() == 'readme.md':
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                continue
            
            if OLD_REPO_PATTERN.search(content):
                new_content = OLD_REPO_PATTERN.sub(NEW_REPO_URL, content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated links in: {filepath}")
                modified_count += 1
                
print(f"Complete. Modified {modified_count} README files.")
