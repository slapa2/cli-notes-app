from entry import Entry
from datetime import datetime
from cli import Cli


class Prog:

    def __init__(self):
        self.cli = Cli()

    def add_entry(self):
        self.cli.clear()
        title = self.cli.get_line('Title\n')
        content = self.cli.get_multi_line_input('Content')
        entry = Entry(title=title, content=content, timestamp=datetime.now())
        entry.save()

    def show_entries(self):
        entries = Entry.get_entry_list()
        entries.extend(['back'])
        choice = self.cli.menu_choice(entries)
        if choice == 'back':
            return
        else:
            self.open_entry(choice)

    def open_entry(self, entry_name: str):
        entry = Entry.get_entry(entry_name)
        self.cli.print_msg(entry)

    def menu_loop(self):
        choice = None
        while choice != 'quit':
            choice = self.cli.menu_choice(['add entry', 'show entries', 'quit'])
            if choice == 'add entry':
                self.add_entry()
            elif choice == 'show entries':
                self.show_entries()