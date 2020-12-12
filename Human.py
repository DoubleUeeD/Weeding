class Human():
    def __init__(self, Name):
        self.name = Name

    def __str__(self):
        return ("Name: " + self.name + ".")


class Studen(Human):
    def __init__(self, Name, Skype):
        super().__init__(Name)
        self.nskype = Skype

    def __str__(self):
        return super().__str__() + "  Skype nickname: " + self.nskype


class Researcher(Human):
    def __init__(self, Name, Course):
        super().__init__(Name)
        self.course = Course

    def __str__(self):
        return super().__str__() + "  List of course:  " +self.course

Nick = Researcher("Nick Bateman","305172 and 305272")
jan = Studen("Jannie Kim","Jannie96")

print(jan)
print(Nick)
