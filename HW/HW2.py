
class SpaceObject:

    def __init__(self, name, mass, size):
        self.name = name
        self.mass = mass
        self.size = size

    def info(self):
        return f"Сведения об объекте:\n1.Название: {self.name}\n2.Масса(кг):{self.mass}\n3.Размер(км):{self.size}"

    def shine(self):
        return f"{self.name} мерцает в космосе"

class Stars(SpaceObject):
    def __init__(self, name, mass, size, temperature):
        super().__init__(name, mass, size)
        self.temperature = temperature

    def info(self):
        return f"Сведения об объекте:\n1.Название: {self.name}\n2.Масса(кг): {self.mass}\n3.Размер(км): {self.size}\n4.Температура: {self.temperature}"

    def shine(self):
        return f"☀ {self.name} излучает яркий свет!"

sun = Stars('Солнце', 1989000000, '1.3927 млн', '5,772')
earth = SpaceObject('Земля', 59720000000, '6,378')

print(earth.info())
print(earth.shine())
print(sun.info())
print(sun.shine())

