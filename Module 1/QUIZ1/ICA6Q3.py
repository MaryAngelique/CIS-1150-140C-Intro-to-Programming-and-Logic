'''
Q3 75 points
You are a manufacturer of widgets.  Take in 2 numbers as input.
The first input is the number of widgets that you made.  This should be an non-negative integer.
The second input is the cost of manufacturing for a single widget. This should be a positive, non-zero float.

You sell to 3 middlemen.
Middleman A pays you a 30% premium on the manufacturing cost of your widgets.  He will buy up to 40 widgets.
Middleman B pays you a 25% premium on the manufacturing cost of your widgets.  He will buy up to 50 widgets.
Middleman C pays you a 20% premium on the manufacturing cost of your widgets.  He will buy up to 60 widgets.
Any leftover widgets must be sold on the open market, for only a 15% premium.

As an example, if it costs you $10 to manufacture a widget, Middleman A pays you $13 per widget.

You are trying to maximize your profit.  Given the input number of widgets, print:
How many widgets are sold to Middleman A, how much they paid for each widget, and how much money was made in total selling to A.
How many widgets are sold to Middleman B, how much they paid for each widget, and how much money was made in total selling to B.
How many widgets are sold to Middleman C, how much they paid for each widget, and how much money was made in total selling to C.
How many widgets are sold on the open market, how much was paid for each widget, and how much money was made in total selling to the open market.
How much money was made on sales to everyone in total.
Print your overall profit for all sales (money made on all sales minus manufacturing costs)
Also print out the profit margin (profit divided by total sales)
'''

widgets = int(input("Enter the number of widgets made: "))
cost = float(input("Enter the cost per widget: "))

premium_a = 0.30
premium_b = 0.25
premium_c = 0.20
premium_open = 0.15

midmanA = min(widgets, 40)
midmanB = min(widgets - midmanA, 50)
midmanC = min(widgets - midmanA - midmanB, 60)
openMarket = widgets - midmanA - midmanB - midmanC

salesA = midmanA * (cost * (1 + premium_a))
salesB = midmanB * (cost * (1 + premium_b))
salesC = midmanC * (cost * (1 + premium_c))
openMarketSales = openMarket * (cost * (1 + premium_open))

totalSales = salesA + salesB + salesC + openMarketSales
totalCost = widgets * cost
totalProfit = totalSales - totalCost
profitMargin = totalProfit / totalSales

print(f"You sold {midmanA} widgets to Middleman A at a price of ${salesA:.2f}")
print(f"You sold {midmanB} widgets to Middleman A at a price of ${salesB:.2f}")
print(f"You sold {midmanC} widgets to Middleman A at a price of ${salesC:.2f}")
print(f"You sold {openMarket} widgets to Middleman A at a price of ${salesA:.2f}")
print(f"{openMarket} widgets were sold on the open market for a total of ${openMarketSales:.2f}")
print(f"Your total sales were ${totalSales:.2f}")
print(f"Your overall profit is ${totalProfit:.2f}")
print(f"Your profit margin is {profitMargin:.2%}")