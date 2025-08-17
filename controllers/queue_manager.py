import json
import os
import re

from controllers.queue import Queue

class QueueManager:
    queues: dict[str, Queue] = dict()
    name: str

    def __init__(self):
        self.set_name("Прога")

    def get_queue(self):
        return self.queues[self.name]

    def set_name(self, name):
        if not name in self.queues.keys():
            self.queues[name] = Queue([], 0)
        self.name = name

    def save_queue(self, name):
        queue = self.queues[name]
        with open(f"data/queue-{name}.json", "w") as file:
            json.dump(queue.__dict__, file) # type: ignore

    def save(self):
        for name in self.queues.keys():
            self.save_queue(name)

    def load(self):
        for file_name in os.listdir("data"):
            if re.match(r"queue-(.*)\.json", file_name):
                name = re.search(r"queue-(.*)\.json", file_name).group(1)
                with open(f"data/{file_name}", "r") as file:
                    res = json.loads(file.read())
                self.queues[name] = Queue(**res)

queue_manager = QueueManager()
