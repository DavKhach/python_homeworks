"""Bad Example"""

# class Worker:
#     def work(self):
#         pass
#
#     def eat(self):
#         pass
#
# class HumanWorker(Worker):
#     def work(self):
#         print("Human working")
#
#     def eat(self):
#         print("Human eating")
#
# class Robot(Worker):
#     def work(self):
#         print("Robot working")
#
#     def eat(self):
#         pass
#
"""Robot class is forced to implement eat(), which is stupid because robots don't eat"""


"""Right Example"""

class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Workable):
    def work(self):
        print("Robot working")

human = Human()
robot = Robot()

human.work()
human.eat()
robot.work()


"""The Workable and Eatable interfaces are separated so that class only implements what it actually needs"""
