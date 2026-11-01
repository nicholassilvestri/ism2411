#Self-Assessment Questions
#1. Exercise 5 Debugging:
#The three bugs in the broken_sales.py file were an incorrect total calculation, a missing colon after the for loop, and a while loop that went out of range. I found these errors by examining/running the code and understanding. This helped me learn to check variables, syntax, and list indices. The first bug that I found was that total=sale was replacing the total each time through the for loop instead of adding each sale. The correct code is a small fix, total+=sale.
#2. apply_discount(price,tier):
#This function takes a price and discount tier as inputs, and applies a discount based on the tier(gold gets 15% off, silver gets 10%, bronze gets 5%, and other tiers get no discount) . The discounted price is returned, so another programmer could use it by passing in a price and a tier.
#3 AI Disclosure: 
#I did use ChatGPT to help understand/explain to me the debugging issues in Exercise 5. I learned from the explanations that it gave and used them to understand the corrections.
#---Exercise 1---:calculate_tax
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

#---Exercise 2---:apply_discount
def apply_discount(price, tier):
   if tier=="gold":
        discount=0.15
   elif tier=="silver":
        discount=0.10
   elif tier=="bronze":
        discount=0.05
   else:
        discount=0.0
   return price * (1 - discount)

print(f"gold: ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none: ${apply_discount(200, 'none'):.2f}")

#---Exercise 3---:Compose them
discounted_price=apply_discount(200, 'gold')
print(f"After gold discount: ${discounted_price:.2f}")
tax=calculate_tax(discounted_price, 0.07)  # Assuming a 7% tax rate
print(f"After tax: ${discounted_price + tax:.2f}")

def final_price(price, tier, tax_rate):
     discounted=apply_discount(price,tier)
     tax=calculate_tax(discounted, tax_rate)
     return discounted + tax

print(f'final_price(200,"gold",0.07) = '
      f'${final_price(200,"gold",0.07):.2f}')

#---Exercise 4---:Loop+function
orders=[
     (200,"gold"),
     (150,"silver"),
     (80,"bronze"),
     (500,"none")
]
for price, tier in orders: 
     total=final_price(price, tier, 0.07)  # Assuming a 7% tax rate
     print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

#---Exercise 5---:Debug First, Then Ask
sales=[120,80,250,175,90]
#Bug 1 fixed(add each sale to the running total)
total=0
for sale in sales:
    total += sale
print(f"Total: ${total}")
#Bug 2 fixed: added the missing colon after the for statement
count=0
for sale in sales:
    count += 1
print(f"Count: {count}")
#Bug 3 fixed(use<instead of <= to avoid indexing past the list)
i=0
while i < len(sales):
    print(sales[i])
    i += 1
#---Exercise 6---
x=100#global
def double_it():
     x=999#local
     return x*2
print(x)#Prints 100
print(double_it())#Prints 1998
print(x)#Prints 100 again

       
