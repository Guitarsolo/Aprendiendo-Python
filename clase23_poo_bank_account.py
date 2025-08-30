class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Su saldo actual es de {self.balance}")
        else:
            print('No se puede depositar. Cuenta inactiva.')

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Su saldo actual es {self.balance}")
            else:
                print('Su saldo es insuficiente.')
        else:
            print('No se puede extraer dinero. Cuenta inactiva.')
    
    def deactivate_account(self):
        self.is_active = False
        print('Se ha desactivado la cuenta.')

    def activate_account(self):
        self.is_active = True
        print('Se ha activado la cuenta.')

account1 = BankAccount('Mariano Diaz', 1000)
account2 = BankAccount('Maria Garay', 1000)

#Llamada a los metodos
account1.deposit(200)
account2.deposit(150)

account1.deactivate_account()
account1.deposit(100)

account1.activate_account()
account1.deposit(100)

account1.withdraw(700)



