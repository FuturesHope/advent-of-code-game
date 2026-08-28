#content: list[str]
fresh_ids_list: list[str]
ids_to_check_list: list [str]
counter:int = 0
ids_list:list[int] = list[int]
ids_list_stringformat:list[str] = []
unique_ids:set[int] = set()
with open( "ids.txt","r") as file:
    content = file.read()

both_sextions = content.split("\n\n")
# print(f"section 1: {both_sextions[0]}")
fresh_ids = both_sextions[0].strip().split("\n")
# hash_fresh = hash(bytesfresh_ids)


#recure
for i in range(len(fresh_ids)):
    splited = fresh_ids[i].split("-")
    id0 = int(splited[0])
    id1 = int(splited[1])
    for ij in range(len(fresh_ids)):
        splitted = fresh_ids[ij].split('-')
        ij0 = int(splitted[0])
        ij1 = int(splitted[1])
        if id0 == ij0 and id1 == ij1:
            continue
        if  ij0 <= id1 <= ij1 or id0 <= ij1 <= id1:
            print(f"AAA -> Found Interlapping ids")
            # if hash_fresh != hash(fresh_ids): print(f"OOO, the freshId-list is changing, checkout hashes: {hash_fresh} vs {hash(fresh_ids)}")
            if ij0 <= id1 <= ij1:
                # fresh_ids[i] = ""+str(id0) + "-" + str(id1)
                print(f"fresh ij before {fresh_ids[ij]}")
                fresh_ids[ij] = ""+str(id1+1) + "-" + str(ij1)
                print(f"fresh ij after {fresh_ids[ij]}")

            if id0 <= ij1 <= id1:
                # fresh_ids[ij] = ""+str(ij0) + "-" + str(ij1)
                print(f"fresh i before {fresh_ids[i]}")
                fresh_ids[i] = ""+str(ij1+1) + "-" + str(id1)
                print(f"fresh i after {fresh_ids[i]}")

# pick up unique values
fresh_ids_new = set(fresh_ids)
fresh_fresh = list[str](fresh_ids_new)

for i in range(len(fresh_fresh)):
    splited = fresh_ids[i].split("-")
    counter += int(splitted[1]) - int(splitted[0]) + 1
    # for i in range(int(splited[0]), int(splited[1])+1):
        # unique_ids.add(i)
print(f"total: {counter}")
# print(f"test uniq list: len{len(unique_ids)}, [0]:{unique_ids[0]}")
# ids_list = [int(id) for id in ids_list_stringformat]
# print(f"test transforming string ints list to list of ints, test len: {len(ids_list)}")
# print(f"test transforming string ints list to list of ints, test pos[0]: {(ids_list[0])}")

# maxid = max(ids_list)
# minid = min(ids_list)
# print(f"max: {maxid} min: {minid}")
# total = maxid - minid + 1 
# print(f"max - min + 1 = {total}")

# given_ids = both_sextions[1].strip().split("\n")
# print(f"fresh id range [0]: {fresh_ids[0]}")
# print(f"given ids len[0]: {len(given_ids)}")
# print(f"given ids [-1]: {given_ids[-1]}")
# print(f"given ids [0]: {given_ids[0]}")

# def check_validity( fresh_ids_list: list[str],  id_for_check: str) -> bool:
#     global counter
#     for fresh_range in fresh_ids_list:
#         splited = fresh_range.split("-")
#         if  int(splited[0]) <= int(id_for_check) <= int(splited[1]) :
#             return True
#             # counter += 1
#             # print(f"found a fresh id: {id_for_check} within {int(splited[0])} and {int(splited[1])}")
    

# for id in given_ids:
#     if check_validity(fresh_ids, id) : counter+= 1

# for r in fresh_ids:
#     splited = r.split("-")
#     counter += (int(splited[1]) - int(splited[0]) + 1)

# print(f"total fresh ids: {counter}")

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