class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
      self._account_number = account_number
      self._account_holder_name = account_holder_name
      self._account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self._account_balance += amount
          return f"Deposited ${amount}. New balance: ${self._account_balance}"
      else:
          return "Invalid deposit amount."

  def withdraw(self, amount):
      if amount > 0 and amount <= self._account_balance:
          self._account_balance -= amount
          return f"Withdrew ${amount}. New balance: ${self._account_balance}"
      else:
          return "Invalid withdrawal amount or insufficient funds."

  def display_balance(self):
      return f"Account Balance for {self._account_holder_name} (Account #{self._account_number}): ${self._account_balance}"

# Test the BankAccount class
if __name__ == "__main__":
  account = BankAccount("12345", "John Doe", 1000.0)

  print(account.display_balance())  # Display initial balance

  print(account.deposit(500))  # Deposit $500
  print(account.display_balance())  # Display updated balance

  print(account.withdraw(200))  # Withdraw $200
  print(account.display_balance())  # Display updated balance

  print(account.withdraw(1500))  # Attempt to withdraw more than the balance

  print(account._account_balance)  # Accessing the balance directly (not recommended, but possible)
