class ReplyHandler:
    def __init__(self):
        self.history = {}
        # The number of saved history per user
        self.max_history_per_user = 20

    def add_history(self, user, content):
        if user not in self.history:
            self.history[user] = []

        self.history[user].append(content)
        self.history[user] = self.history[user][-self.max_history_per_user:]

    def get_history(self, user):
        if user not in self.history:
            return None
        return self.history[user][-1]

    def replace_reply(self, content):
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('> '):
                user = line[len('> '):]
                history = self.get_history(user)
                if history:
                    lines[i] = '> '+"\n> ".join(history.split('\n'))
        return "\n".join(lines)

