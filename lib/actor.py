from .audition import Audition

class Actor:
    def __init__(self, name):
        self.name = name


    @property
    def auditions(self):
        return [a for a in Audition.all_auditions if a.actor == self ]
    

    @property
    def roles(self):
        return [a.role for a in self.auditions]
