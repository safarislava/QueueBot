from entity.user import User

class UserController:
    users = dict()

    def __init__(self):
        self.users[100] = User(100, "A")
        self.users[200] = User(200, "B")
        self.users[300] = User(300, "C")

    def add(self, user):
        if not user.id in self.users.keys():
            self.users[user.id] = user

    def get_user_by(self, id):
        return self.users.get(id)

user_controller = UserController()