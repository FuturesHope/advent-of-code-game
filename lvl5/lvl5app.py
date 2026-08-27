#content: list[str]
fresh_ids_list: list[str]
ids_to_check_list: list [str]
counter:int = 0
with open( "ids.txt","r") as file:
    content = file.read()

both_sextions = content.split("\n\n")
print(f"section 1: {both_sextions[0]}")
fresh_ids = both_sextions[0].strip().split("\n")
given_ids = both_sextions[1].strip().split("\n")
print(f"fresh id range [0]: {fresh_ids[0]}")
print(f"given ids len[0]: {len(given_ids)}")
print(f"given ids [-1]: {given_ids[-1]}")
print(f"given ids [0]: {given_ids[0]}")

def check_validity( fresh_ids_list: list[str],  id_for_check: str) -> bool:
    global counter
    for fresh_range in fresh_ids_list:
        splited = fresh_range.split("-")
        if  int(splited[0]) <= int(id_for_check) <= int(splited[1]) :
            return True
            # counter += 1
            # print(f"found a fresh id: {id_for_check} within {int(splited[0])} and {int(splited[1])}")
    

for id in given_ids:
    if check_validity(fresh_ids, id) : counter+= 1

print(f"total fresh ids: {counter}")

# x = content.count([""])
# print(f" count '':{x}")
# content.count("")
# fresh_codes_list = content.)
# print(f"index of an empty string {fresh_codes_list}")

# for i in range(3):
#     print(f"line:{i}, value: {content[i].strip()}")
    # print(f"split type : {content[i].strip().split('-')[:]}")
# print(f"first 5 lines {content[0:5]}")
# print(f"first line type{(content[0].strip())}")
# print(f"index for empty space {content.index('')}")