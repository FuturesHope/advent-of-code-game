
from time import sleep


code = ""
total_jolts = 0
dirty_battery_list: list[int]
with open("batteries.txt", "r") as file:
    code = file.read()


for line in code.splitlines():
    string_form_joltage = ''
    index_controller = 12
    coordinates_max_val1 = 0
    print (line)
    print(f" line length before : {len(line)}")
    dirty_battery_list = [int(char) for char in line ]
    # remaining_battery_list  = dirty_battery_list
    print(f" starting while loop")
    while index_controller != 0:
        print(f"index controller val = {index_controller}")
        print(f"Picked batteries: {dirty_battery_list[coordinates_max_val1  : -index_controller]}")
        print(f"remained batteries untouched: {dirty_battery_list[-index_controller:]}")
        max_val = max(dirty_battery_list[coordinates_max_val1 : -index_controller])
        print(f"maxval = {max_val}")
        # print()
        # if coordinates_max_val1 < 0 : coordinates_max_val1 = 0
        coordinates_max_val1 += dirty_battery_list[coordinates_max_val1 : -index_controller].index(max_val)
        coordinates_max_val1 += 1
        # remaining_battery_list = dirty_battery_list[coordinates_max_val1 : -index_controller]
        # remaining_battery_list = dirty_battery_list[coordinates_max_val1 + 1 : -index_controller]
        print(f"Coordinates max val = {coordinates_max_val1}")
        # max_val2 = max(dirty_battery_list[coordinates_max_val1 + 1:])
        # value_to_addup = int(str(max_val1) + str(max_val2))
        string_form_joltage += str(max_val)
        print(f"string_form_joltage = {string_form_joltage}")

        index_controller -= 1
        # print(f" index controller val = {index_controller}")
        print(f" - 1 while cycle")
    # print(f"jolts to add: {value_to_addup}")
    total_jolts += int(string_form_joltage)
    print(f"total jolts = {total_jolts}")
print(f"Total jolts: {total_jolts}")

# print (len(code.splitlines()))