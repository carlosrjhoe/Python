class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print(f"(Initializing {self.name})")
        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print("There are still {:d} robots working."
                  .format(Robot.population))

    def say_hi(self):
        """Greeting by the robot.
        Yeah, they can do that."""
        print(f"Greetings, my masters call me {self.name}.")

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print(f"We have {cls.population} robots.")


if __name__ == '__main__':
    droid1 = Robot("R2-D2")
    droid1.say_hi()
    Robot.how_many()
    droid2 = Robot("C-3PO")
    droid2.say_hi()
    Robot.how_many()
    print("Robots can do some work here.")
    print("Robots have finished their work. So lets destroy them.")
    droid1.die()
    droid2.die()
    Robot.how_many()
