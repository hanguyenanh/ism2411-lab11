# Question 1: I use bracket notation when a key must exist, like a customer ID or price in data I've already validated. If it's missing, something is broken, and I want the KeyError to stop the program instead of hiding the problem.
# I use .get() when a key might legitimately be missing, like an optional phone number or a tier not in a lookup table, because I can supply a safe default.
# My rule of thumb: required data gets brackets, optional data gets .get()

# Question 2: The summary dictionary reminds me of a PivotTable or SUMIF, where I total amounts grouped by a category like region.
# The Python version is more useful for large datasets because it makes one pass through the data, handles millions of rows without Excel's row limit or slowdowns, and is repeatable: I can rerun the same script on new data instead of rebuilding a pivot by hand.

print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

print("--- Exercise 2 ---")

customer['phone'] = '555-5555'
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer['email']
print(customer)

print("--- Exercise 3 ---")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print("KeyError caught: ", error)

print("--- Exercise 4 ---")

for key, value in customer.items():
    print(f"{key}: {value}")

# Looping over the dict without .items() gives only the keys, so I have to look up each value myself with customer[key].
# .items() hands me the key and value together as a pair, which is shorter and clearer.

for key in customer:
    print(key, customer[key])

print("--- Exercise 5 ---")

tier_discounts = {"bronze": 0, 
                  "silver": 0.05,
                  "gold": 0.1,
                  "platinum": 0.15}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")

print("--- Exercise 6 ---")

customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

print("--- Exercise 7 ---")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {details['stock']} left")

print("--- Exercise 8 ---")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")