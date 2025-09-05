# Наследование

# Родительский | Супер класс
class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):

        print("Base action")

# kirito = Hero("kirito", 100, 1000)


# Дочерний класс
# class HeroMage(Hero):
#
#     def cast_spell(self):
#         print(f"{self.name} fire!!!")
#
# kirito = HeroMage("kirito", 100, 1000)
#
#
#
# class HeroWar(HeroMage):
#     pass
#
# kirito =


# Полиморфизм
class BaseUser:

    def __init__(self, login, password, user_name):
        self.login = login
        self.password =password
        self.user_name =user_name

    def repost(self, text):
        print(f"{self.user_name} added a new repost \n {text}")

ardager = BaseUser("ardager", 12341, "mr.ardager")

class VipUser(BaseUser):

    def __init__(self, login, password, status: str, user_name: str = "john Doe", ):
        super().__init__(login, password, user_name)
        self.status = status


    def repost(self, text):
        print(f"{self.user_name} added a new repost  ☁︎ \n {text}")

    pass

# john = VipUser("john", 23456, "John Doe", "VIP")
john = VipUser(user_name = "John Doe", password = 134456,  )
ardager.repost("Alloha")
john.repost("I'm vip john")