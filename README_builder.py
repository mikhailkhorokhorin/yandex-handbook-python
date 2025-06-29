import os


def process_directory(path):
    readme_lines = []
    folder_name = os.path.basename(path.rstrip("/\\"))
    readme_lines.append(f"# {folder_name}\n")

    py_files = sorted(f for f in os.listdir(path) if f.endswith(".py"))

    for file_name in py_files:
        file_path = os.path.join(path, file_name)
        file_base = os.path.splitext(file_name)[0]

        readme_lines.append(f"### {file_base}")
        readme_lines.append("\n```python\n")

        with open(file_path, "r", encoding="utf-8") as f:
            readme_lines.extend(f.readlines())

        readme_lines.append("```\n")

    readme_path = os.path.join(path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(readme_lines)

    print(f"Added: {readme_path}")


def process_all_subfolders(root_dir="."):
    for current_dir, dirs, files in os.walk(root_dir):
        if any(part.startswith(".") for part in current_dir.split(os.sep)):
            continue
        process_directory(current_dir)


process_all_subfolders(root_dir="2. Базовые конструкции Python")
