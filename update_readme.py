import subprocess
from datetime import datetime

def run_tests():
    try:
        subprocess.check_call(["pytest", "-q"])
        return "Tests correctos"
    except subprocess.CalledProcessError:
        return " Tests fallidos"

def update_readme(status: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"- {status} {now}\n"

    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    inserted = False
    for line in lines:
        new_lines.append(line)
        if not inserted and line.strip() == "## Estado de los tests":
            new_lines.append(entry)
            inserted = True

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    status = run_tests()
    update_readme(status)
