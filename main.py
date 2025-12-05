from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, initial_balance):
        self.balance = initial_balance

    @abstractmethod
    def add(self, amount):
        ...

    @abstractmethod
    def pay(self, amount):
        ...

    def transfer(self, accountTo, amount):
        if not self.pay(amount):
            return False
        if not accountTo.add(amount):
            self.add(amount)
            return False
        return True


class SimpleAccount(Account):
    def __init__(self, initial_balance):
        super().__init__(initial_balance)

    def add(self, amount):
        self.balance += amount
        return True

    def pay(self, amount):
        if self.balance - amount < 0:
            return False
        self.balance -= amount
        return True




class CreditAccount(Account):
    def __init__(self, credit_limit):
        super().__init__(0)
        self.credit_limit = credit_limit

    def add(self, amount):
        if self.balance + amount > 0:
            return False
        self.balance += amount
        return True

    def pay(self, amount):
        if self.balance - amount < - self.credit_limit:
            return False
        self.balance -= amount
        return True