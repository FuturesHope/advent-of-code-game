from time import sleep
import os
from typing import Tuple, List, Dict, Set

addup_invalid_ids: int = 0
factors: Dict[int, Set[int]] = {}
id_ranges: List[str] = []

print(f"start of processing...")
sleep(2)

def extract_id_range(id_range: str) -> Tuple[str, str]:
    start_id, end_id = id_range.split('-')
    return start_id.strip(), end_id.strip()

#intakes a range of ids to check for only all chars equal. this is for lengths where no factors deected
#need to detect the len of the range, and start with the min limit of the range to check for all numbers in the range if they are all equal
#returns the sum of all the invalid ids in the range
def check_all_nums_same(start_id: str, end_id: str) -> int:
    total = 0
    for id_value in range(int(start_id), int(end_id) + 1):
        if  str(id_value) == str(id_value)[0] * len(str(id_value)):  #len(set(str(id_value))) == 1:
            print(f"adding {id_value}")
            if len(str(id_value)) > 1:
                total += id_value
    return total



# this method neeeds adjustment , I should start from 2, 
# the algorithm: check for the whole number out of a sqrt(len(id_value)) and then check for the factors of the number and 
# then check if the sequence repeats itself
# feeding len for given range
def calculate_factors(n: int) -> Set[int]:
    factors_set: Set[int] = set()
    if n < 2:
        return set()
    tries = int(n ** 0.5)
    for i in range(2, tries + 1):
        if n % i == 0:
            rez = n // i
            factors_set.add(rez)
            factors_set.add(i)
    return factors_set


def extract_from_file(file_path: str) -> List[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        id_ranges = [r.strip() for r in content.strip().split(",") if r.strip()]
    return id_ranges

def extract_factors(id_ranges: List[str]) -> None:
    for id_range in id_ranges:
        for id_ in extract_id_range(id_range):
            length = len(id_)
            if factors.get(length) is None:
                factors[length] = calculate_factors(length)

def calculate_values_for_common_length_id_ranges(start_id: str, end_id: str) -> int:
    total = 0
    length = len(start_id)
    if(length  == 1): 
        return total
    list_of_factors = factors.get(length, set())
    ids_to_add_list : Set[int] = set()
    if list_of_factors:
        for factor in list_of_factors:
            if length % factor != 0:
                continue
            for i in range(int(start_id), int(end_id) + 1):
                s = str(i)
                sequence = s[:factor]
                if sequence * (len(s) // factor) == s:
                    if i not in ids_to_add_list: 
                        ids_to_add_list.add(i)
                        print(f"adding {i}")
                        total += i
                    else: 
                        print(f"{i} already found")
    else:
        total += check_all_nums_same(start_id, end_id)

    return total

#return the answer with sum of all invalid ids in the given ranges
def start_solution() -> None:
    global addup_invalid_ids
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "ids.txt")
    id_ranges = extract_from_file(file_path)
    print(id_ranges)
    extract_factors(id_ranges)
    for id_range in id_ranges:
        start_id, end_id = extract_id_range(id_range)

        print(f"processing range: {start_id, end_id}")
        if len(start_id) == len(end_id):
            addup_invalid_ids += calculate_values_for_common_length_id_ranges(start_id, end_id)
        else:
            list_of_ranges = []
            #check whether the id is less then length 2, then it is not fit for processing
            if len({len(item) for item in (start_id, end_id)}) <= 1:
                continue
            list_of_ranges.append((start_id, '9' * len(start_id)))
            list_of_ranges.append((str(10 ** len(start_id)), end_id))
            for s, e in list_of_ranges:
                addup_invalid_ids += calculate_values_for_common_length_id_ranges(s, e)


        print(f" addup_invalid_ids sum = {addup_invalid_ids}")
        # sleep(0.5)

    print(f"end of processing...")
    print(f" total invalid ids sum = {addup_invalid_ids}")


if __name__ == "__main__":
    start_solution()

            # method for factors
            #method for checking all numbers in the range if they are all equal
        # else:
        #     for id in (start_id, end_id):

        #     # method for handling different length id ranges
        #     pass

        # for id in (int(start_id), int(end_id) + 1):

        #     if factors.get(len(id)) != set({0}):
        #         list_of_factors = factors.get(len(id))
        #         #break the range by length if differentiate

        #         for factor in list_of_factors:
        #             if len(id) % factor == 0:
        #                 sequence = id[:factor]
        #                 if sequence * (len(id) // factor) == id:
        #                     addup_invalid_ids += int(id)
        #     else:
        #         addup_invalid_ids += check_all_nums_same(start_id, end_id)   

        


# def is_id_invalid(id_value:str) -> bool:
#     #split the id_value into two halves and compare the values
#     half_length = len(id_value) // 2
#     first_half = id_value[:half_length]
#     second_half = id_value[half_length:]
#     if first_half == second_half:
#         return True
#     else:
#         return False

# def check_id_length(id_value:str) -> bool:
#     if len(id_value) % 2 == 0:
#         return True
#     else:
#         return False


# with open("ids.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     #set a list of given ranges for cycling
#     id_ranges = list(str(content).strip("\n").split(","))
  
            
#     for id_range in id_ranges:
#         start_id, end_id = extract_id_range(id_range)
#         # if check_id_length(start_id) or check_id_length(end_id):
#         for id_value in range(int(start_id), int(end_id) + 1):
#             if is_id_invalid(str(id_value)):
#                 addup_invalid_ids += id_value
#                     # print(f"Invalid ID: {id_value}")
#                     # sleep(0.5)
#                 # else:
#                 #     print(f"Valid ID: {id_value}")
#         # else:
#         #     print(f"ID range {id_range} has invalid length.")

# # came up with this
# def is_id_invalid(id_value:str) -> bool:
#     #check if all the digits are the same using a set))
#     if len(set(id_value)) == 1:
#         return True
#     #check if any sequence repeats itself till the end of the length of the id number



#     # # revise this
#     # for i in range(2, len(id_value)):
#     #     if len(id_value) % i == 0:
#     #         sequence = id_value[:i]
#     #         if sequence * (len(id_value) // i) == id_value:
#     #             return True
#     # return False

#     # the idea for factor id-n. this would lower the number of cycles probably needs a different function
#     print(f" total invalid ids sum = {addup_invalid_ids}")