class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Jeel", "Aman", "Rahul"])

print(len(team))