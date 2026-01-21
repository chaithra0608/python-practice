class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_time,pin,balance):
    self.first_name=first_name
    self.last_name=last_name
    self.account_id=account_id
    self.account_time=account_time
    self.pin=pin
    self.balance=balance
  def deposit(self,account):
    self.balance+=account
    return self.balance
  def withdraw(self,account):
    self.balance-=account
    return self.balance
  def display_balance(self):
    return self.balance
account_1 = BankAccount('Alice','Smith',9191919,'Savings',1234,99000.01)
account_1.deposit(999)
account_1.withdraw(99)
print(account_1.display_balance())
