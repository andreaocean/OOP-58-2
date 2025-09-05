# Классы

# self - ссылка на обьект класса

# нотации
# HeroMag - верблюжая нотация
# hero_kirito - snakecase
class Hero:

    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибута класса
        self.name_1 = name
        self.lvl_1 = lvl
        self.hp_1 = hp

    # def __init__(kirito, name, lvl, hp):
    #     # Атрибута класса
    #     kirito.name_1 = name
    #     kirito.lvl_1 = lvl
    #     kirito.hp_1 = hp

    # Метод класса

    def action(self):
        print("Base action")

kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 100, 1000)

text_1 ="text1"
text_2 ="text2"

print(kirito.name_1)
print(asuna.name_1)
print(text_1)
print(text_1)



# print(kirito.hp_1)
# kirito.action()

# print(type("str"))
# print(type(123))
# print(type(12.12))
# print(type(True))
# print(type(kirito))

# test = str("sdsldkj")
# test = []
#
# kirito.action()


