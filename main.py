# from module_1 import add, test
# import module_1
# from module_1 import * #обращение ко всему, что есть
                        #нежелательно исползовать



# print(add(64, 78))
# print(test)

# print(module_1.add(64, 78))
# print(module_1.test)

# print(add(64, 78))
# print(test)


from my_packege import minus, add, test


from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

