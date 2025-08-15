from controllers.user import user_controller

class Queue:
    value = []
    count = 0

    def __init__(self):
        self.append(100)
        self.append(200)
        self.append(300)

    def show(self):
        users = [user_controller.get_user_by(i).name for i in self.value]

        text = ""
        for i in range(len(users)):
            text += f"{i + self.count}. {users[i]}\n"

        return text

    def append(self, id):
        if self.value.count(id) > 0:
            self.value.remove(id)
        self.value.append(id)

queue = Queue()
