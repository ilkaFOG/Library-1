class App:
    def __int__(self):
        self.__event_loop = []

    def add_task(self, task):
        self.__event_loop.append(task)

    def remove_task(self, task):
        self.__event_loop.remove(task)

    def run(self):
        while True:
            for event in self.__event_loop:
                event()