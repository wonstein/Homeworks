class Portfolio(object):
	def __init__(self, name):
		self.name = name
		self.cash = 0
		self.stocks = []
		self.mutualfunds = []
		self.log = []
		
	def addCash(self, amount):
		if isinstance(amount, float) == False and isinstance(amount, int) == False:
			print "Invalid value."
		else:
			self.cash += amount
			if amount >= 0:
				print "Cash deposited: $%.2f" % amount
			elif amount < 0:
				print "Cash withdrawn: $%.2f" % -amount
	
	def withdrawCash(self, amount):
		self.addCash(-amount)
		
	def getCash(self):
		return self.cash