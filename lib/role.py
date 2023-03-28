from .audition import Audition

class Role:
    def __init__(self, character_name):
        self.character_name = character_name


    @property
    def auditions( self ):
        return [a for a in Audition.all if a.role ==self]
    

    @property
    def actors(self):
        return [a.actor for a in self.auditions]
    
    @property
    def locations(self):
        return [a.location for a in self.auditions]
    

    def hired(self):
        return [a.role for a in self.auditions if a.hired == True]

