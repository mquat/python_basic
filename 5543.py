menu_list = [int(input()) for _ in range(5)]

burger= min(menu_list[:3])
beverage = min(menu_list[3:])

print(burger+beverage-50)