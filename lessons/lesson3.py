# Инкапсуляция



class BankAccount:

    def __init__(self, login, password, balance):
        self.login = login
        self.__password = password #приват
        self._balance = balance #защищен

    def check_balance(self, password):
        if password == self.__password:
            print(self._balance)
        else:
            print('Неправильный пароль!')

    def generate_pass(self):
        self.__pasword = 2344342

    def reset_pass(self, password):
        if password == self.__password:
            se

user_1 = BankAccount('Aizada', "12345", 1000)

print(user_1.__password)
print(user_1check_balance)