
num_of_cities = int(input())
totalprofit = 0
combination = 0
city_dict = {}
for i in range(1, num_of_cities + 1):
    
    name_of_city = input()
    owner_money = float(input())
    owner_expenses = float(input())
    
    if i % 5 == 0 and i % 3 == 0:
        owner_money -= owner_money * 0.1
    elif i % 5 == 0:
        owner_money -= owner_money * 0.1
    if i % 3 == 0 and i % 5 != 0:
        owner_expenses += owner_expenses * 0.5
        
    city_dict.update({f"{name_of_city}":owner_money - owner_expenses})
final_str = ""
for value, key in city_dict.items():
    final_str += f"In {value} Burger Bus earned {float(key):.2f} leva.\n"
    totalprofit += key
print(f"{final_str}Burger Bus total profit: {totalprofit} leva.")
