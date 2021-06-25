class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.01, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

    def display_user_balance(self):
        reporte = ("-")*30 + "\n"
        reporte += "Nombre\t:" + self.name + "\n"
        reporte += "Saldo\t: $" + str(self.account.display_account_info())
        return reporte


class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrar una tarifa de $ 5")
            self.balance -= 5
        return self
	
    def display_account_info(self):
        #print(f"Saldo: ${self.balance}")
        return self.balance
	
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

usuario1 = User("Juan Perez","jperez@gmail.com")
usuario2 = User("Marcelo Soto","msoto@gmail.com")
usuario3 = User("Mauricio Abarca","mauricio@sektorweb.cl")

usuario1.make_deposit(1000)
usuario2.make_deposit(1000).transfer_money(usuario1, 1000)
usuario2.make_withdrawal(1000)
print(usuario1.display_user_balance())
print(usuario2.display_user_balance())