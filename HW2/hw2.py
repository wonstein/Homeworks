import random

class Portfolio(object):
	def __init__(self, name):
		self.name = name
		self.cash = 0
		self.stocks = []
		self.mutualfunds = []
		self.log = []
	
	def history(self):
		print "Transaction History:"
		for i in range(0, len(self.log)):
			print "\t%d. %s" % (i+1, self.log[i])
		
	def __str__(self):
		return "Portfolio Summary: \n\tCash: $%.2f \n\tStocks: %r \n\tMutual Funds: %r" % (self.cash, self.stocks, self.mutualfunds)
					
	def gatherAssets(self):
		for i in range(0, len(self.stocks)):
			if self.stocks[i][0] == 0:
				self.stocks.pop(i)
			for j in range(1, len(self.stocks)):
				if self.stocks[i][1] == self.stocks[j][1]:
					self.stocks[i][0] += self.stocks[j][0]
					self.stocks.pop(j)
			
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
	
	def buyAsset(self, quantity, asset):
		if quantity <= 0:
			print "Invalid transaction."
		elif isinstance(quantity, int) == False and isinstance(asset, Stock) == True:
			print "Invalid transaction. Stocks must be sold whole."
		else:
			self.cash -= asset.getPrice() * quantity
			if isinstance(asset, Stock) == True:
				asset_type = 'Stocks'
				self.stocks.append([quantity, asset.getSymbol()])
			elif isinstance(asset, MutualFund):
				asset_type = 'Mutual Fund'
				self.mutualfunds.append([quantity, asset.getSymbol()])
			if quantity == 1:
				multiple = ''
			else:
				multiple = 's'
			log_entry = "%s purchased: %r share%s of %s." % (asset_type, quantity, multiple, asset.getSymbol())
			self.log.append(log_entry)
			self.gatherAssets()
	
	def buyStock(self, quantity, asset):
		self.buyAsset(quantity, asset)
		
	def buyMutualFund(self, quantity, asset):
		self.buyAsset(quantity, asset)
				
	
	def sellStock(self, quantity, stock):
		if isinstance(quantity, int) == False or quantity <= 0:
			print "Invalid transaction. Stocks must be sold whole."
		else:
			# Check if client owns any shares of stock
			if not(stock.getSymbol() in zip(*self.stocks)[1]):
				print "Invalid transaction. No stock owned."
			
			# Check if client owns sufficient quantity of stock
			else:
				if self.stocks[zip(*self.stocks)[1].index(stock.getSymbol())][0] < quantity:
					print "Invalid transaction. Not enough stock owned."		
				else:
					# Generate random selling price 
					sellprice = stock.getPrice() * random.uniform(0.5, 1.5)
					self.cash += sellprice * quantity
					self.stocks[zip(*self.stocks)[1].index(stock.getSymbol())][0] -= quantity
					if quantity == 1:
						shares = 'share'
					else:
						shares = 'shares'
					log_entry = "Stock sold: %d %s of %s at $%.2f per share" % (quantity, shares, stock.getSymbol(), sellprice)
					self.log.append(log_entry)
		self.gatherAssets()
	
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

p = Portfolio('folio')
p.addCash(500000)
s = Stock(100, 'HAL')
m = MutualFund('MAR')
p.buyAsset(2, s)
print p
p.buyAsset(3.01029, m)
print p
p.history()