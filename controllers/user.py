from entity.user import User

class UserController:
    users = dict()

    def __init__(self):
        self.users[1076509512] = User(1076509512, "safarislava")
        self.users[7229159786] = User(7229159786, "Алёна")

    def add(self, user: User) -> None:
        if not user.id in self.users.keys():
            self.users[user.id] = user

    def get_user_by_int(self, id: int) -> User:
        return self.users.get(id)

    def get_user_by_str(self, name: str) -> User: # name should be unique
        for user in self.users.values():
            if user.name == name:
                return user

user_controller = UserController()