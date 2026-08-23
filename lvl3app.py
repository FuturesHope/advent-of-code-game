
from time import sleep


code = ""
total_jolts = 0
dirty_battery_list: list[int]
with open("batteries.txt", "r") as file:
    code = file.read()


for line in code.splitlines():
    # print (line)
    dirty_battery_list = [int(char) for char in line ]
    max_val1 = max(dirty_battery_list[:-1])
    coordinates_max_val1 = dirty_battery_list.index(max_val1)
    max_val2 = max(dirty_battery_list[coordinates_max_val1 + 1:])
    value_to_addup = int(str(max_val1) + str(max_val2))
    total_jolts += value_to_addup
    # sleep(0.5)
    # print(f"jolts to add: {value_to_addup}")
    
print(f"Total jolts: {total_jolts}")

# print (len(code.splitlines()))