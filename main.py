import random


class Student:
    group = "Shag"
    subject = "Python"

    def __init__(self, name):
        self.name=name
        self.hapiness = 50
        self.progress = 0
        self.alive = True

    def study(self):
        print("Time to study")
        self.progress += 0.1
        self.hapiness -= 3
    def sleep(self):
        print("Time to sleep")
        self.hapiness += 3
    def chill(self):
        print("Time to chill")
        self.progress -= 0.1
        self.hapiness += 5

    def end_of_the_day(self):
        print(f"Hapiness = {self.hapiness}")
        print(f"Progress = {self.progress}")

    def live(self, day):
        day = f"Day{day} of {self.name} life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.study()
        if live_cube == 2:
            self.sleep()
        if live_cube == 3:
            self.chill()
        self.end_of_the_day()
        self.is_alive()

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out ...')
            self.alive = False
        elif self.progress < 0:
            print('Depression!')
            self.alive = False
        elif self.progress < 0:
            print('Passed Externally')
            self.alive = False

nick = Student(name = "Nick")
for i in range(365):
    if nick.alive == False:
        break
    nick.live(i)







