from getdone.Exceptions import InvalidTaskException


class Task:
    def __init__(self, title, deadline=''):
        self.title = title
        self.deadline = deadline

    def string_form(self) -> str:
        if self.deadline:
            representation = self.title + ' ==== ' + self.deadline
        else:
            representation = self.title
        return representation

    @staticmethod
    def parse_string(string):
        splits = string.split(' ==== ')
        if len(splits) == 1:
            Task(splits[0])
        elif len(splits) == 2:
            Task(splits[0], splits[1])
        else:
            raise InvalidTaskException(string)


