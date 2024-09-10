import subprocess

def get_git_diff():
    """Run the git diff command and return its output."""
    result = subprocess.run(
        ['git', 'diff', '--name-status', 'origin/main...HEAD'],
        text=True,  # Return output as a string
        capture_output=True
    )
    return result.stdout

def main():
    git_diff_output = get_git_diff().strip().split('\n')
    new_files = []
    changed_files = []

    for line in git_diff_output:
        status, file_name = line.split(maxsplit=1)
        if status == 'A':
            new_files.append(file_name)
        elif status == 'M':
            changed_files.append(file_name)
    
    # Print new files
    print("New files added in the pull request:")
    for file in new_files:
        print(f"New file: {file}")

    # Print changed files
    print("Changed files in the pull request:")
    for file in changed_files:
        print(f"Changed file: {file}")

def get_git_diff_lines(file_path):
    """Run the git diff command for a specific file and return its output."""
    result = subprocess.run(
        ['git', 'diff', '--unified=0', 'origin/main...HEAD', '--', file_path],
        text=True,
        capture_output=True
    )
    return result.stdout

def parse_diff_lines(diff_output):
    """Parse the git diff output to extract lines added."""
    added_lines = []
    for line in diff_output.splitlines():
        if line.startswith('+') and not line.startswith('+++'):
            # This line is added content
            added_lines.append(line[1:])
    return added_lines


if __name__ == "__main__":
    main()
