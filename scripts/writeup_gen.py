from datetime import date
import pathlib
import templates
import urllib


ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
year = str(date.today().year)
WRITEUP_DIR = ROOT_DIR / "_writeups" / year
ASSET_DIR = ROOT_DIR / "assets" / "CTFs" / year


def make_dir(path):
    dir_path = pathlib.Path(path)
    if not dir_path.exists():
        print(f'Creating directory: {dir_path.relative_to(ROOT_DIR)}')
        dir_path.mkdir(parents=True)


def sanitize(path):
    return path.replace(" ", "-").replace("?", "").replace("/", "_")


def yaml_escape(str):
    for c in "{}[],&:*#?|-<>=!%@\\`":
        if c in str:
            return f">-\n    {str}"
    return str


def create_ctf_index(ctf_name):
    ctf_path = sanitize(ctf_name)
    make_dir(ASSET_DIR / ctf_path)

    if pathlib.Path(WRITEUP_DIR / ctf_path).exists():
        print("Adding challenges to existing CTF")
        return

    make_dir(WRITEUP_DIR / ctf_path)
    with open(WRITEUP_DIR / ctf_path / "index.md", "w+") as fout:
        fout.write(templates.ctf_overview.format(
            yaml_escape(ctf_name),
            date.today()
        ))


def create_chall(ctf_name, chall_name, points, solves, tags):
    tag_list = tags.replace(", ", ",").split(",")
    formatted_tags = "".join([f"\n    - {tag}" for tag in tag_list])
    
    ctf_path = sanitize(ctf_name)
    chall_path = sanitize(chall_name)
    writeup_file = WRITEUP_DIR / ctf_path / (chall_path + ".md")
    with open(writeup_file, "w+") as fout:
        fout.write(templates.ctf_writeup.format(
            yaml_escape(chall_name),
            yaml_escape(ctf_name),
            points,
            solves,
            formatted_tags,
            date.today()
        ))


def main():
    ctf_name = input('Enter CTF Name: ')
    create_ctf_index(ctf_name)
    
    while True:
        chall_name = input('Enter chall name: ')
        points = input('Enter points: ')
        solves = input('Enter no. of solves: ')
        tags = input('Enter chall tags (comma-separated): ')
        create_chall(ctf_name, chall_name, points, solves, tags)
        if input('Add another chall? (y/N): ') != 'y':
            break


if __name__ == '__main__':
    main()
