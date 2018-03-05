
start = 5000
money_spent_daily = 250
cash = start
money_earned = 500

for day in range(1,365):
	cash = cash + money_earned - money_spent_daily
	print("Day %s: %s" % (day, cash))
