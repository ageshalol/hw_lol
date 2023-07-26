class Timer:
    def __init__(self, initial_time):
        self.initial_time = initial_time
        self.time = initial_time

    def get_time(self):
        return self.time

    def start(self):
        while self.time > 0:
            print(self.time)
            self.time -= 1

    def reset(self):
        self.time = self.initial_time
        

timer = Timer(10)
print(timer.get_time())
timer.start()
timer.reset()
# print(timer.get_time())
