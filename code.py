from itertools import combinations  

# Define items with their size and survival points  
gear_items = {  
    'r': (3, 25),  # Rifle  
    'p': (2, 15),  # Pistol  
    'a': (2, 15),  # Ammo  
    'm': (2, 20),  # Medkit  
    'i': (1, 5),   # Inhaler  
    'k': (1, 15),  # Knife  
    'x': (3, 20),  # Axe  
    't': (1, 25),  # Talisman  
    'f': (1, 15),  # Flasks  
    'd': (1, 10),  # Antidote  
    's': (2, 20),  # Food  
    'c': (2, 20)   # Crossbow  
}  

max_weight = 9  
base_survival_points = 15  
essential_items = ['i']  

optimal_combination = None  
highest_survival_points = float('-inf')  

# Iterate over all possible combinations of gear items  
for num_items in range(1, len(gear_items) + 1):  
    for combo in combinations(gear_items.keys(), num_items):  
        total_weight = sum(gear_items[item][0] for item in combo)  
        total_points = sum(gear_items[item][1] for item in combo)  

        # Check if the current combination is valid  
        if total_weight <= max_weight and all(item in combo for item in essential_items):  
            final_survival_points = base_survival_points + total_points  

            # Update the best combination found  
            if final_survival_points > highest_survival_points:  
                highest_survival_points = final_survival_points  
                optimal_combination = combo  

# Prepare to display the optimal inventory configuration  
if optimal_combination:  
    inventory_grid = [[' ' for _ in range(3)] for _ in range(3)]  
    for idx, item in enumerate(optimal_combination):  
        row, col = divmod(idx, 3)  
        inventory_grid[row][col] = item  

    # Print the inventory layout  
    for row in inventory_grid:  
        print(['[{}]'.format(item) for item in row])  

    print(f"Final survival points: {highest_survival_points}")
