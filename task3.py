def backpack(items, max_weight):
    ok_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            ok_items.append(item)
            max_weight -= weight
    return ok_items

items = {'tent': 5, 'water': 3, 'food': 4, 'clothes': 2, 'dishes': 1}
max_weight = 10
print(backpack(items, max_weight)) 