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
		summary_stocks = ''
		summary_mutualfunds = ''
		for i in range(0,len(self.stocks)):
			summary_stocks += "%d shares of %s \n		" % (self.stocks[i][0], self.stocks[i][1])
		for i in range(0,len(self.mutualfunds)):
			summary_mutualfunds += "%d shares of %s \n		      " % (self.mutualfunds[i][0], self.mutualfunds[i][1])
		return "Portfolio Summary: \n\n\tCash: $%.2f \n\n\tStocks: %s \n\tMutual Funds: %s" % (self.cash, summary_stocks, summary_mutualfunds)
					
	def gatherAssets(self):
		removeStocks = []
		for i in range(0, len(self.stocks)):
			if self.stocks[i][0] == 0:
				self.stocks.pop(i)
			for j in range(i+1, len(self.stocks)):
				if self.stocks[i][1] == self.stocks[j][1]:
					self.stocks[i][0] += self.stocks[j][0]
					removeStocks.append(j)
		for k in removeStocks[::-1]:
			self.stocks.pop(k)
			
	def addCash(self, amount):
		if isinstance(amount, float) == False and isinstance(amount, int) == False:
			print "Invalid value."
		else:
			self.cash += amount
			if amount >= 0:
				log_entry = "Cash deposited: $%.2f" % amount
			elif amount < 0:
				log_entry = "Cash withdrawn: $%.2f" % -amount
			self.log.append(log_entry)
	
	def withdrawCash(self, amount):
		self.addCash(-amount)
		
	def getCash(self):
		return self.cash

	def buyAsset(self, quantity, asset):
		if quantity <= 0:
			print "Invalid transaction."
		elif isinstance(quantity, int) == False and isinstance(asset, Stock) == True:
			print "Invalid transaction. Stocks must be sold whole."
		elif self.cash < asset.getPrice() * quantity:
			print "Invalid transaction. Not enough cash."
		else:
			self.cash -= asset.getPrice() * quantity
			if isinstance(asset, Stock) == True:
				asset_type = 'Stocks'
				self.stocks.append([quantity, asset.getSymbol(), asset.getPrice()])
			elif isinstance(asset, MutualFund):
				asset_type = 'Mutual funds'
				self.mutualfunds.append([quantity, asset.getSymbol(), asset.getPrice()])
			log_entry = "%s purchased: %r share(s) of %s at $%.2f per share" % (asset_type, quantity, asset.getSymbol(), asset.getPrice())
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
			if not self.stocks:
				self.stocks.append([0, 'EMPTY'])
			if not self.mutualfunds:
				self.mutualfunds.append([0, 'EMPTY'])
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
				self.cash += sellprice * quantity
				if quantity == 1:
					multiple = ''
				else:
					multiple = 's'
				log_entry = "%s sold: %.1f share%s of %s at $%.2f per share" % (asset_type, quantity, multiple, asset.getSymbol(), sellprice)
				self.log.append(log_entry)
		self.gatherAssets()
		
	def sellStock(self, quantity, asset):
		if isinstance(asset, str) == True:
			if asset in zip(*self.stocks)[1]:
				self.sellAsset(quantity, Stock(zip(*self.stocks)[2][zip(*self.stocks)[1].index(asset)], asset))
			else: 
				print "Invalid transaction. %s is not a stock." % asset
		else:
			self.sellAsset(quantity, asset)
	
	def sellMutualFund(self, quantity, asset):
		if isinstance(asset, str) == True:
			if asset in zip(*self.mutualfunds)[1]:
				self.sellAsset(quantity, MutualFund(asset))
			else: 
				print "Invalid transaction. %s is not a mutual fund." % asset
		else:
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
p.addCash(50000)
s = Stock(100, 'HAL')
s2 = Stock(50, 'BAR')
m = MutualFund('MAR')
m2 = MutualFund('MOP')
p.buyAsset(2, s)
#print p
#p.buyAsset(15, s2)
#print p
#p.buyAsset(3, s)
#print p
#p.buyAsset(3, s2)
#print p
#p.gatherAssets()
#print p
p.buyAsset(3.1, m)
p.buyAsset(5.7, m2)
print p
p.sellMutualFund(4.1, 'HAL')
print p
p.history()