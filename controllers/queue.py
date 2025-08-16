from controllers.user import user_controller

class Queue:
    value = []
    count = 0

    def __init__(self):
        self.append(100)
        self.append(300)

    def exist(self, id):
        return id in self.value

    def show(self):
        users = [user_controller.get_user_by_int(i).name for i in self.value]

        text = ""
        for i in range(len(users)):
            text += f"{i + self.count}. {users[i]}\n"
        return text

    def append(self, id):
        if self.exist(id):
            self.value.remove(id)
        self.value.append(id)

    def swap(self, first_id, second_id):
        first_index = self.value.index(first_id)
        second_index = self.value.index(second_id)
        self.value[first_index], self.value[second_index] = self.value[second_index], self.value[first_index]

queue = Queue()
