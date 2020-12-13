class Fish:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def swim(self):
        print("swiming")

    def swim_backwards(self):
        print("swim backwards")


class Salmon(Fish):
    """
    """
    def __init__(self, first_name, last_name):
        super(Salmon, self).__init__(first_name, last_name)

    def swim_backwards(self):
        self.swim()


sal = Salmon(first_name="nemo", last_name="aab")
sal.swim_backwards()
