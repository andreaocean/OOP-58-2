# class Fly:
#     def fly(self):
#         print("Fly")
#
# class Swim:
#     def swim(self):
#         print("Swim")
#
#
# class Duck(Fly, Swim):
#     pass
#
# donald_duck = Duck()
#
# donald_duck.fly()
# donald_duck.swim()


# class Fly:
#     def action(self):
#         print("Fly")
#
# class Swim:
#     def action(self):
#         print("Swim")
#
#
# class Duck(Fly, Swim):
#     pass
#
# donald_duck = Duck()
#
# donald_duck.fly()
# donald_duck.swim()


class A:
    def action(self):
        print('A')


# class B(A):
#     def action(self):
#         print('B')

class B(A):
    def action(self):
        super().action()
        print('B')

class C(A):
    def action(self):
        print('C')


class D(B, C):
    pass
    # def action(self):
    #     print('D')

obj = D()

# obj.action()
print(D.__mro__)  #Method Resolution Order