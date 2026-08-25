
from time import sleep


code = ""
total_jolts = 0
dirty_battery_list: list[int]
with open("lvl3/batteries.txt", "r") as file:
    code = file.read()

# 1) identify the max val , while + remaining chars sum to min 12
# 2) from max val index towards end -> remove min vals 

for line in code.splitlines():
    string_form_joltage = ''
    index_controller = 11
    index_max_val = 0
    # print (f"Line Num: {code.splitlines().index(line)}")
    # print (line)

    dirty_battery_list = [int(char) for char in line ]
    processed_battery_list =  dirty_battery_list[:-12]
    remainder_batteries_list = dirty_battery_list[-12:]
    # maxval = max(dirty_battery_list)
    # topped_battery_list = 
    # string_form_joltage += str(maxval)
    # print(f"joltage formation: {string_form_joltage}")

        
    # print(f"total jolts= {total_jolts}")
    # print(f"# line length before : {len(line)}")
    # print(f" starting while loop")
    while len(string_form_joltage) != 12:
        # print(f"index controller val = {index_controller}")
        # print(f"Picked batteries: {processed_battery_list[index_max_val : ]}")
        # print(f"remained batteries untouched: {remainder_batteries_list}")
        processed_battery_list.append(remainder_batteries_list.pop(0))
        max_val = max(processed_battery_list[index_max_val :])
        # print(f"maxval = {max_val}")
        # print()
        # if coordinates_max_val1 < 0 : coordinates_max_val1 = 0
        index_max_val += processed_battery_list[index_max_val : ].index(max_val)
        index_max_val += 1
        # remaining_battery_list = dirty_battery_list[coordinates_max_val1 : -index_controller]
        # remaining_battery_list = dirty_battery_list[coordinates_max_val1 + 1 : -index_controller]
        # print(f"Coordinates max val = {index_max_val}")
        # max_val2 = max(dirty_battery_list[coordinates_max_val1 + 1:])
        # value_to_addup = int(str(max_val1) + str(max_val2))
        # if len(string_form_joltage) + len(dirty_battery_list[index_max_val:]) == 12:
        if index_max_val == len(processed_battery_list): #  len(string_form_joltage) + len(dirty_battery_list[index_max_val:]) == 12:
            # string_form_joltage += ''.add(char for char in dirty_battery_list[index_max_val  :])
            # print(f"OOOO : Check that the index is the last digit of processed list, adding the remainders")
            # returned the poped last digit
            remainder_batteries_list.insert(0, processed_battery_list.pop())
            # print(f"now OOOO, the remained batteries should include all the digits to fill the remaining spaces")
            for char in remainder_batteries_list: string_form_joltage += str(char)
            # print(f"Accelerated formation stringform : {string_form_joltage} , with length = {len(string_form_joltage)}")
        else:
            string_form_joltage += str(max_val)
        # print(f"string_form_joltage = {string_form_joltage}")

        # index_controller -= 1
        # if index_controller == 0 : print(f"index controller is 0 , the formed string is {string_form_joltage}")
        # if(index_controller < 0): 
        #     print(f"EROR: index controller < 0")
        #     sleep(20)
        # print(f" index controller val = {index_controller}")
        # print(f" - 1 while cycle")
    # print(f"jolts to add: {value_to_addup}")
    total_jolts += int(string_form_joltage)
    # print(f"total jolts = {total_jolts}")
print(f"Total jolts: {total_jolts}")

    # didn't work
    # test min val extraction: 
    # while len(dirty_battery_list) != 12:
    #     dirty_battery_list.pop(dirty_battery_list.index(min(dirty_battery_list))) #min(dirty_battery_list)
    #     # print(f"minval = {minval}")
    # print(dirty_battery_list)
    # for i in dirty_battery_list: 
    #     string_form_joltage += str(i) 

    # algo per line ideas
    # identify max digit and its index; if it's index is within last 11 digits, then search for next max digit within [:-11]
    #   next max digit & index identified -> then if it's index is the first digit of last 12 digits , the remaining remains unchanged
    #   if max digit is below last 12 digits > 
    #       pickit & this is the starting index for final joltage_to_add
    #       from remaining
    #       
    
    #digits would construct the final jolts_to_add