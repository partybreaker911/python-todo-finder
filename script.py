import sys
import os
import re

TODO_REGEX = r"\bTODO\b(.*)"


def find_todos(file_path):
    todos = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            match = re.search(TODO_REGEX, line)
            if match:
                todo = match.group(1).strip()
                todos.append((file_path, i + 1, todo))
    return todos


def find_all_todos(root_dir):
    todos = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                todos += find_todos(file_path)
    return todos


def generate_readme(todos, readme_path):
    with open(readme_path, "w") as f:
        f.write("# TODO List\n\n")
        for todo in todos:
            f.write(f" - ` {todo[0]}` line {todo[1]}: {todo[2]}\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_directory> <output_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    todos = find_all_todos(root_dir)
    output_dir = sys.argv[2]
    readme_path = os.path.join(output_dir, "README.md")
    generate_readme(todos, readme_path)
