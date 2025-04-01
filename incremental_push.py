import subprocess
import sys

def run_cmd(cmd):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

# Get all commit hashes in chronological order (oldest first)
result = subprocess.run(['git', 'log', '--reverse', '--format=%H'], capture_output=True, text=True)
commits = result.stdout.strip().split('\n')

if not commits or len(commits) == 1 and commits[0] == '':
    print("No commits found.")
    sys.exit(0)

# Push in batches of 50 to avoid RPC timeouts on large repos
batch_size = 50
for i in range(0, len(commits), batch_size):
    chunk = commits[i:i+batch_size]
    last_commit_in_chunk = chunk[-1]
    
    progress = min(i + batch_size, len(commits))
    print(f"\n--- Pushing batch: up to commit {last_commit_in_chunk} ({progress}/{len(commits)}) ---")
    
    try:
        # Push this specific commit to the remote 'main' branch
        run_cmd(['git', 'push', '-uf', 'origin', f'{last_commit_in_chunk}:refs/heads/main'])
    except subprocess.CalledProcessError as e:
        print(f"Error pushing batch ending at {last_commit_in_chunk}: {e}")
        sys.exit(1)

print("\n--- Finalizing push ---")
try:
    run_cmd(['git', 'push', '-uf', 'origin', 'main'])
    print("All commits pushed successfully in batches!")
except subprocess.CalledProcessError as e:
    print(f"Error finalizing push: {e}")
    sys.exit(1)
