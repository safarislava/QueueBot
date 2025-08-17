from controllers.user import user_controller

class Queue:
    value: list
    count: int

    def __init__(self, value, count):
        self.value = value
        self.count = count

    def exist(self, id: int) -> bool:
        return id in self.value

    def show(self) -> str:
        if len(self.value) == 0:
            return "Очередь пуста"

        users = [user_controller.get_user_by_int(i).name for i in self.value]

        text = ""
        for i in range(len(users)):
            text += f"{i + self.count}. {users[i]}\n"
        return text

    def append(self, id: int) -> None:
        if self.exist(id):
            self.value.remove(id)
        self.value.append(id)

    def swap(self, first_id: int, second_id: int) -> None:
        first_index = self.value.index(first_id)
        second_index = self.value.index(second_id)
        self.value[first_index], self.value[second_index] = self.value[second_index], self.value[first_index]
