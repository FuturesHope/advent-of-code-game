from time import sleep

# as how I  see it now..1785878643.0657127
# given the range of ids, each Id number has to have % 2 = 0 length (even char length)
# in order to halfen and compare so that the ids are unique and not repeated

addup_invalid_ids: int = 0

#check whether the length of the first and second number of the range to be equal

def extract_id_range(id_range:str) -> tuple:
    #split the id_range into two parts using the '-' character as a delimiter
    start_id, end_id = id_range.split('-')
    return start_id, end_id

def check_id_length(id_value:str) -> bool:
    if len(id_value) % 2 == 0:
        return True
    else:
        return False


def is_id_invalid(id_value:str) -> bool:
    #split the id_value into two halves and compare the values
    half_length = len(id_value) // 2
    first_half = id_value[:half_length]
    second_half = id_value[half_length:]
    if first_half == second_half:
        return True
    else:
        return False


with open("ids.txt", "r", encoding="utf-8") as file:
    content = file.read()
    #set a list of given ranges for cycling
    id_ranges = list(str(content).strip("\n").split(","))
    # for i in range (0 , id_ranges.__len__()):
    #     first, second = extract_id_range(id_ranges[i])
    #     if len(first) != len(second):
    #         print(f"range {i}: {id_ranges[i]} has unequal length")
    #         print(f"range {i}: {id_ranges[i]}")
            
    for id_range in id_ranges:
        start_id, end_id = extract_id_range(id_range)
        if check_id_length(start_id) or check_id_length(end_id):
            for id_value in range(int(start_id), int(end_id) + 1):
                if is_id_invalid(str(id_value)):
                    addup_invalid_ids += id_value
                    # print(f"Invalid ID: {id_value}")
                    # sleep(0.5)
                # else:
                #     print(f"Valid ID: {id_value}")
        # else:
        #     print(f"ID range {id_range} has invalid length.")
    print(f" total invalid ids sum = {addup_invalid_ids}")