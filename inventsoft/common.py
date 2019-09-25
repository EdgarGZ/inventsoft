# Session
from inventsoft.sessions import Session

# Global variables
__session = None

# Create your views here.
def config(user):
    global __session

    if not __session:
        print('creando')
        __session = Session(user)

    return __session