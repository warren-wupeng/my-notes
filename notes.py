import abc
import argparse
from dataclasses import dataclass
from datetime import datetime
from fileinput import filename

@dataclass
class Note:
    note_id: int
    title: str

    @classmethod
    def create(cls, title: str):
        result = cls(
            note_id=int(datetime.utcnow().timestamp()),
            title=title
        )
        return result

class LocalFileNoteRepo:

    def __init__(self) -> None:
        self.folder = './area/'

    def __setitem__(self, noteId: int, note: Note) -> None:
        filename = f"{noteId}-{note.title}"
        file_ext = '.md'
        with open(self.folder+filename+file_ext, "w") as f:
            f.write(f"# {filename}")


def create_handler(args):
    note = Note.create(title=args.title)
    repo = LocalFileNoteRepo()
    repo[note.note_id] = note

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help="create command help")
parser_create = subparsers.add_parser('create', help='create a new note')
parser_create.add_argument("--title", type=str)
parser_create.set_defaults(func=create_handler)

if __name__ == "__main__":
    print("Warren's notes system")
    args = parser.parse_args()
    args.func(args)