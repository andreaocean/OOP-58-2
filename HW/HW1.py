class Object:
    def __init__(self, name, category, weight, maxspeed):
        self.name = name
        self.category = category
        self.weight = weight
        self.maxspeed = maxspeed

    def info(self):
        return (f"Name: {self.name}\n"
                f"Category: {self.category}\n"
                f"Weight: {self.weight}\n"
                f"Speed: {self.maxspeed}\n")

    def compare(self, other, attribute = "speed"):
        if attribute == "weight":
            object1 = self.weight
            object2 = other.weight
        if attribute == "speed":
            object1 = self.maxspeed
            object2 = other.maxspeed

        if object1 > object2:
            return f"{self.name} is better in {attribute}"
        elif object1 < object2:
            return f"{other.name} is better in {attribute}"
        else:
            return f"{self.name} and {other.name} are equal in {attribute}"


lion = Object("Lion", "Animal", 130, 80 )
ferrari = Object("Ferrari F80", "Car", 1525, 340)

print(lion.info())
print(ferrari.info())

print(ferrari.compare(lion, "weight"))
print(lion.compare(ferrari, "speed"))