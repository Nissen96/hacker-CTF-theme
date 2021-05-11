from datetime import date
import pathlib
import templates


ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
year = str(date.today().year)
WRITEUP_DIR = ROOT_DIR / "_writeups" / year
ASSET_DIR = ROOT_DIR / "assets" / "CTFs" / year


def make_dir(path):
    dir_path = pathlib.Path(path)
    if not dir_path.exists():
        print(f'Creating directory: {dir_path.relative_to(ROOT_DIR)}')
        dir_path.mkdir(parents=True)


def create_ctf_index(ctf_name):
    ctf_path = ctf_name.replace(" ", "-")
    make_dir(ASSET_DIR / ctf_path)

    if pathlib.Path(WRITEUP_DIR / ctf_path).exists():
        print("Adding challenges to existing CTF")
        return

    make_dir(WRITEUP_DIR / ctf_path)
    
    index = templates.ctf_overview.format(ctf_name, date.today())
    with open(WRITEUP_DIR / ctf_path / "index.md", "w+") as fout:
        fout.write(index)


def create_chall(ctf_name, chall_name, points, solves, tags):
    tag_list = tags.replace(", ", ",").split(",")
    formatted_tags = "".join([f"\n    - {tag}" for tag in tag_list])
    
    ctf_path = ctf_name.replace(" ", "-")
    chall_path = chall_name.replace(" ", "-")
    writeup_file = WRITEUP_DIR / ctf_path / (chall_path + ".md")
    with open(writeup_file, "w+") as fout:
        fout.write(templates.ctf_writeup.format(
            chall_name,
            ctf_name,
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
