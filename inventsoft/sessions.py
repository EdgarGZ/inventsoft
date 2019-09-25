SESSIONS = []

class Session:
    def __new__(cls, user):
        if len(SESSIONS) < 1:
            instance = super(Session, cls).__new__(cls)
            instance.__init__(user)
            SESSIONS.append(instance)
            return instance
        else:
            print('Only one session available')

    def __init__(self, user):
        self.user = user

    def getUser(self):
        return self.user

    def setUser(self, new_user):
        self.user = new_user

    def deleteSession(self, user):
        SESSIONS.remove(user)