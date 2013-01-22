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
			self.withdrawCash(asset.getPrice() * quantity)
			if isinstance(asset, Stock) == True:
				asset_type = 'Stocks'
				self.stocks.append([quantity, asset.getSymbol()])
			elif isinstance(asset, MutualFund):
				asset_type = 'Mutual funds'
				self.mutualfunds.append([quantity, asset.getSymbol()])
			if quantity == 1:
				multiple = ''
			else:
				multiple = 's'
			log_entry = "%s purchased: %.1f share%s of %s." % (asset_type, quantity, multiple, asset.getSymbol())
			self.log.append(log_entry)
			self.gatherAssets()
	
	def buyStock(self, quantity, asset):
		self.buyAsset(quantity, asset)
		
	def buyMutualFund(self, quantity, asset):
		self.buyAsset(quantity, asset)
				
	def sellAsset(self, quantity, asset):
		price_mod = 1
		if quantity <= 0:
			print "Invalid transaction."
		else: 
			# Check if client owns shares of asset
			if not(asset.getSymbol() in zip(*self.stocks)[1] or asset.getSymbol() in zip(*self.mutualfunds)[1]):
				print "Invalid transaction. No shares of %s owned." % asset.getSymbol()
			# Check if clients owns enough shares
			elif (isinstance(asset, Stock) == True and self.stocks[zip(*self.stocks)[1].index(asset.getSymbol())][0] < quantity) or (isinstance(asset, MutualFund) == True and self.mutualfunds[zip(*self.mutualfunds)[1].index(asset.getSymbol())][0] < quantity):
				print "Invalid transaction. Not enough shares of %s owned." % asset.getSymbol()
			else:
				if isinstance(asset, Stock) == True:
					asset_type = 'Stocks'
					if isinstance(quantity, int) == False:
						print "Invalid transaction. Stocks must be sold whole."
					else:		
						# Generate price modifier
						price_mod = random.uniform(0.5, 1.5)
						self.stocks[zip(*self.stocks)[1].index(asset.getSymbol())][0] -= quantity
				elif isinstance(asset, MutualFund) == True:
					asset_type = 'Mutual funds'	
					# Generate price modifier
					price_mod = random.uniform(0.9, 1.2)
					self.mutualfunds[zip(*self.mutualfunds)[1].index(asset.getSymbol())][0] -= quantity
				sellprice = asset.getPrice() * price_mod
				self.addCash(sellprice * quantity)
				if quantity == 1:
					multiple = ''
				else:
					multiple = 's'
				log_entry = "%s sold: %.1f share%s of %s at $%.2f per share" % (asset_type, quantity, multiple, asset.getSymbol(), sellprice)
				self.log.append(log_entry)
		self.gatherAssets()
		
	def sellStock(self, quantity, asset):
		self.sellAsset(quantity, asset)
	
	def sellMutualFund(self, quantity, asset):
		self.sellAsset(quantity, asset)
	
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
p.buyAsset(3.1, m)
print p
p.sellAsset(4, m)
print p