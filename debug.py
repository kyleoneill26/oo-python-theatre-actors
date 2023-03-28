import ipdb
from lib import *

# Test your code below...

kyle = Actor("Kyle")
adam = Actor("Adam")


batman = Role("Batman")
spiderman = Role("SPiderman")

a1 = Audition("LA", True, batman, kyle)
a2 = Audition("Nashville", True, batman, adam)
a2 = Audition("NYC", False, spiderman, kyle)
a2 = Audition("Miami", True, spiderman, adam)



# the below line allows us to stop & try stuff!
ipdb.set_trace()