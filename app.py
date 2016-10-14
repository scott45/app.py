#  __author__ = 'Scott Businge'


import datetime
from Tools.Scripts.treesync import raw_input


class Journal(object):
    def __init__(self, journal_author=None):
        self.author = journal_author
        self.date_posted = str(datetime.datetime.now().date())
        self.journal_dict = {}

    def create_journal_entry(self):
        author = str(raw_input('Type your name: '))
        entry_name = str(raw_input('Type the title: '))
        post = str(raw_input('Type your thoughts:\n'))
        self.journal_dict.update({entry_name.upper(): {
            "author": author.upper(),
            "date": self.date_posted,
            "entry": post}})
        return self.journal_dict

    def delete_entry(self):
        entry = raw_input("input name of post to delete: ")
        self.journal_dict.pop(entry)
        return self.journal_dict

    def list_of_entries(self):
        entries = self.journal_dict.keys()
        for item in entries:
            print("NAME: {}\n".format(item))
            print("AUTHOR: {}\n".format(self.journal_dict[item]["author"]))
            print("DATE: {}\n".format(self.journal_dict[item]["date"]))
            print("{}\n".format(self.journal_dict[item]["entry"]))

    def view_one_journal_entry(self):
        name = raw_input("input name of post to view: ").upper()
        print("NAME: {}\n".format(name))
        print("DATE: {}".format(self.journal_dict[name]["date"]))
        print("{}\n".format(self.journal_dict[name]["entry"]))


journal = Journal()
stop = 'y'
while stop == 'y':
    create = int(raw_input(
        "To create input 1\nTo view posts input 2\nTo delete a post input 3\nTo view one post input 4\n"))
    if create == 1:
        print(journal.create_journal_entry())
        print("Entry posted successfully \n")
    if create == 2:
        journal.list_of_entries()
    if create == 3:
        journal.delete_entry()
    if create == 4:
        journal.view_one_journal_entry()
    stop = raw_input("Do you wish to continue?(y/n): ").lower()
