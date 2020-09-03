class Account:
	""" An account has a balance and a holder
	
	>>> a = Account('John')
	>>> a.holder
	'John'
	>>> a.deposit(100)
	100
	>>> a.withdraw(90)
	10
	>>> a.withdraw(90)
	'Insufficient funds'
	>>> a.balance
	10
	>>> a.interest
	0.02
	"""

	interest = 0.02 # A class attribute

	def __init__(self, account_holder):
		self.holder = account_holder;
		self.balance = 0;

	def deposit(self, amount):
		"""Add amount to balance. """
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self, amount):
		"""Substract amount from balance if funds are available."""
		if amount > self.balance:
			return 'Insufficient funds'
		self.balance = self.balance - amount
		return self.balance


class CheckingAccount(Account):
	"""A bank account that charges for withdrawals.
	这个肯定是继承这个类的意思

	>>> ch = CheckingAccount('Jack')
	>>> ch.balance = 20
	>>> ch.withdraw(5)
	14
	>>> ch.interest
	0.01
	"""

	withdraw_fee = 1
	interest = 0.01  # lixi

	def withdraw(self, amount):
		return Account.withdraw(self,amount + self.withdraw_fee)
		#Alternatively:
		return super().withdraw(amount + self.withdraw_fee)

class Bank:
	"""A bank has accounts and pays interest.
	
	>>> bank = Bank()
	>>> john = bank.open_account('John', 10)
	>>> jack = bank.open_account('Jack', 5, CheckingAccount)
	>>> jack.interest
	0.01
	>>> john.interest = 0.06
	>>> bank.pay_interest()
	>>> john.balance
	10.6
	>>> jack.balance
	5.05
	"""
	def __init__(self):
		self.accounts = []

	def open_account(self, holder, amount, account_type = Account):
		"""Open an account_type for holder and deposit amount."""
		account = account_type(holder)
		account.deposit(amount)
		self.accounts.append(account)
		return account

	def pay_interest(self):
		"""Pay interest to all accounts."""
		for account in self.accounts:
			account.deposit(account.balance * account.interest)

# Inheritance Excample

class A:
	z = -1
	def f(self, x):
		return B(x - 1)

class B(A)
	n = 4
	def __init__(self, y):
		if y:
			self.z = self.f(y)
		else:
			self.z = C(y+1)

class C(B):
	def f(self, x):
		return x

def WWPD():
	"""What would Python Display? . 的意思是这个对象属性指向的哪个变量名称。。

	>>> a = A()
	>>> b = B(1)
	>>> b.n = 5
	>>> C(2).n
	4
	>>> C(2).z
	2
	>>> a.z == C.z
	True
	>>> a.z == b.z
	False
	>>> b.z.z.z
	1
	"""

# Multiple Inheritance
## 多继承 这个还是第一次遇到
## 安排要做的事情。那就好好的完成。。
## 尽量努力一下。。多找找方法。。完成事情。。

class SavingsAccount(Account):
	"""A bank account that chares for deposits."""

	deposits_fee = 2

	def deposit(self, amount):
		return Account.deposit(self, amount - self.deposits_fee)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
	"""A bank account that charges for everything."""

	def __init__(self, account_holder):
		self.holder = account_holder
		self.balance = 1 # A free dollar!

supers = [c.__name__ for c in AsSeenOnTVAccount.mro()]