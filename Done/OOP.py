class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return "name is {} and age is {}".format(self.name, self.age)


class Men(Person):
    gender = "Male"
    nu_of_men = 0

    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice
        Men.nu_of_men += 1

    def display(self):
        return super().display() + f" and his voice is {self.voice} and his gander {Men.gender}"


class Women(Person):
    gender = "Female"
    nu_of_women = 0

    def __init__(self, name, age, voice, tall):
        super().__init__(name, age)
        self.voice = voice
        self.tall = tall
        Women.nu_of_women += 1

    def display(self):
        return super().display() + f"and her voice is {self.voice} and her gender is {Women.gender}"


man_1 = Men("Ahmed", 30, "Hard")
print(man_1.display())
woman_1 = Women("Abeer", 28, "soft", 170)
print(woman_1.display())
