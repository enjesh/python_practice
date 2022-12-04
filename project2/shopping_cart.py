# Ask the user to provide the quantity of the shopping item
flowerpot = int(input('How many flowerpots? '))
flower_seeds = int(input('How many packs of flower seeds? '))
soil = int(input('How many bags of soil? '))
# print(flowerpot, flower_seeds, soil)

# Cost of each shopping item
flowerpot_price = 4.00
flower_seeds_price = 1.00
soil_price = 5.00

# Sales Tax Variable
tax_rate = 0.06

# calculate the cost of items
cost_of_items = (flowerpot * flowerpot_price) + (flower_seeds * flower_seeds_price) + (soil * soil_price)
print (cost_of_items)

# Calculate the cost of items plus tax
total_cost = (cost_of_items * tax_rate) + cost_of_items
print(total_cost)