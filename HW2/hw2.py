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
		
	def buyStock(self, quantity, stock):
		if isinstance(quantity, int) == False or quantity <= 0:
			print "Invalid transaction. Stocks must be sold whole."
		else:
			if stock.getPrice() * quantity > self.cash:
				print "Invalid transaction. Not enough cash."
			else:
				self.cash -= stock.getPrice() * quantity
				self.stocks.append([quantity, stock.getSymbol()])
				if quantity == 1:
					shares = 'share'
				else: 
					shares = 'shares'
				log_entry = "Stock purchased: %d %s of %s." % (quantity, shares, stock.getSymbol())
				self.log.append(log_entry)
				self.gatherAssets()
	
	def buyMutualFund(self, quantity, mutualfund):
		if quantity <= 0:
			print "Invalid transaction."
		else:
			if mutualfund.getPrice() * quantity > self.cash:
				print "Invalid transaction. Not enough cash."
			else:
				self.cash -= mutualfund.getPrice() * quantity
				self.mutualfunds.append([quantity, mutualfund.getSymbol()])
				if quantity == 1:
					shares = 'share'
				else: 
					shares = 'shares'
				log_entry = "Mutual funds purchased: %.1f %s of %s." % (quantity, shares, mutualfund.getSymbol())
				self.log.append(log_entry)
				self.gatherAssets()
				
	def gatherAssets(self):
		for i in range(0, len(self.stocks)):
			if self.stocks[i][0] == 0:
				self.stocks.pop(i)
			for j in range(1, len(self.stocks)):
				if self.stocks[i][1] == self.stocks[j][1]:
					self.stocks[i][0] += self.stocks[j][0]
					self.stocks.pop(j)
		
	def history(self):
		print "Transaction History:"
		for i in range(0, len(self.log)):
			print "\t%d. %s" % (i+1, self.log[i])
		
	def __str__(self):
		return "Portfolio Summary: \n\tCash: $%.2f \n\tStocks: %r \n\tMutual Funds: %r" % (self.cash, self.stocks, self.mutualfunds)
				
class Asset(object):
	def __init__(self, symbol):
		self.symbol = symbol
	
	def getSymbol(self):
		return self.symbol
		
	def getPrice(self):
		return self.price
		
class Stock(Asset):
	def __init__(self, price, symbol):
		self.symbol = symbol
		self.price = price
		
class MutualFund(Asset):
	def __init__(self, symbol):
		self.symbol = symbol
		self.price = 1
	