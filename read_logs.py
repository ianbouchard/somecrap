# Look into importing Coinbase module
from sys import argv

script, read_file, tx_file = argv

# automate check pricing
# will need to learn how to use cron
# execute a buy

#print "What is the starting price"
#price_0 = float(raw_input(">>: "))

logs = open(read_file, 'r')
tx = open(tx_file, 'a')

agg_profit = 0.0
price_0 = float(logs.readline())
count_buy = 0
count_hold = 0

"""
def buy(price):
	price_0 = price
"""
	
for line in logs:
	price_n = float(line)
	if price_n >= price_0 * 1.02:
		# execute a SELL
		profit = price_n - (price_0 * 1.01)
		agg_profit += profit
		tx.write("buy no: %d \nprice_n was %f \nprice_0 was %f " % (count_buy, price_n, price_0))
		tx.write("Sold at %f. you made: %f agg profit is: %f \n" % (price_n, profit, agg_profit))
		count_buy += 1
		price_0 = price_n # buy at new price
	else:
		tx.write("held at %f \n" % (price_n,))
		count_hold += 1

# how do I round in file.write?

tx.write("no. buys: %d \nno. holds: %d \ntotal profit: %f \n" % (count_buy, count_hold, agg_profit))
tx.write("Final holding price: %f" % price_0)
logs.close()
tx.close()
	

#read prices and timestamps from logs/api 
#need a better way of doing the positioning for all of the lines
#need a function to check price and then sell or not sell

#compare old price to new price
#will need to check based on some time delay
#execute a sell depending on the result of the comparison
#write the results of each transaction in a new log file