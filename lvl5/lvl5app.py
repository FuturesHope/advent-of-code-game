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

ranges = []

for value in fresh_ids:
    start, end = map(int, value.split("-"))
    ranges.append((start, end))

ranges.sort()

total = 0
current_start, current_end = ranges[0]

for start, end in ranges[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        total += current_end - current_start + 1
        current_start, current_end = start, end

total += current_end - current_start + 1

print(f"total: {total}")


# # hash_fresh = hash(bytesfresh_ids)
# fresh_ids = [val for i , val in enumerate(fresh_ids) if fresh_ids.index(val) == i]
# ids_range0 = []
# ids_del = []
# ids_del_counter = []

# #remove ids range = 0
# # for i in fresh_ids:
# #     splited = i.split("-")
# #     id0 = int(splited[0])
# #     id1 = int(splited[1])
# #     if id0 == id1:
# #         # counter += 1
# #         ids_range0.append(i)

# # print(f"all {len(ids_range0)} range 0: ")
# # for i in ids_range0:
# #     print(f" {i}")
# # print(f"now all remaining len{len(fresh_ids)}:")
# # for i in [x for x in fresh_ids if not fresh_ids.__contains__(i)]:
# #     print(f"{i}:")
# #check whether in ids to remove are those that are within range of others
# # if not within , then add count +1 and remove it
# # fresh_ids_no0range = [x for x in fresh_ids if not ids_range0.__contains__(x)]
# # for i in range(len(ids_range0)):
# #     splited = ids_range0[i].split("-")
# #     id0 = int(splited[0])
# #     for j in fresh_ids_no0range:
# #         splis = j.split("-")
# #         ij0 = int(splis[0])
# #         ij1 = int(splis[1])
# #         if ij0 <= id0 <= ij1:
# #             print(f"OOOO , found an error")
# #             if fresh_ids.__contains__(ids_range0[i]):
# #                 ids_del.append(ids_range0[i])
# #                 # fresh_ids.remove(ids_to_remove[i])
# #             print(f"removing duplicate: {ids_range0[i]}")
# #         # else:
# #         #     if fresh_ids.__contains__(ids_range0[i]):
# #                 # ids_del_counter.append(ids_range0[i])
# #                 # fresh_ids.remove(ids_to_remove[i])
# #                 # counter += 1
# # for i in ids_del:
# #     if fresh_ids.__contains__(i):
# #         print(f"len: {len(fresh_ids)}")
# #         fresh_ids.remove(i)
# #         print(f"len: {len(fresh_ids)}")

# # for i in ids_del_counter:
# #     if fresh_ids.__contains__(i):
# #         print(f"len: {len(fresh_ids)}")
# #         fresh_ids.remove(i)
# #         print(f"len: {len(fresh_ids)}")
# #         counter += 1


# # print(f"len fresh id before cleaning range0: {len(fresh_ids)}")
# # for i in ids_to_remove:
# #     fresh_ids.remove(i)
# # print(f"len fresh id after cleaning range0: {len(fresh_ids)}")
# #recure
# # new_list = []
# # new_list.append(fresh_ids[0])
# # list_of_used = []
# # to_remove_list = []

# # def id_overlapers
# # def range_mutation
# # def remover of overlappers
# # returns the new id , the index where to update it, index what to remove
# def id_overlapers(given_list: list[str]):
#     range_return = ""
#     index_range_return:int 
#     removal_value:str
#     for i in range(len(given_list)):
#         splited = given_list[i].split("-")
#         id0 = int(splited[0])
#         id1 = int(splited[1])
#         for ij in range(len(given_list)):
#             if i == ij: continue
#             splitted = given_list[ij].split('-')
#             ij0 = int(splitted[0])
#             ij1 = int(splitted[1])
#             if ij0 <= id1 <= ij1:
#                 range_return = ""+str(id0) + "-" + str(ij1)
#                 index_range_return = i
#                 removal_value = given_list[ij]
#                 return range_return, index_range_return, removal_value
#             # one way cycle from i to ij
#             # base is still , try one way mutations
#             # base mutating -> the i , others removed in process if possible
#             # check whether need to simoky remove ranges within other ranges -> DUPLICATES
#             # ij has been detected within ameba space , ameba grows ij removed
#             if ij0 < id0 < ij1:
#                 range_return = ""+str(ij0) + "-" + str(id1)
#                 index_range_return = i
#                 removal_value = given_list[ij]
#                 return range_return, index_range_return, removal_value
#             #same number range
#             # if id0 == id1 and ij0 < id0 < ij1: # or ij0 == ij1
#             #     return "", 0 , given_list[i]
#             # if ij0 == ij1 and id0 < ij0 < id1: # or ij0 == ij1
#             #     return "", 0 , given_list[ij]
#             # duplicates catch for ij removal line, ameba grows from i center/ this catches the 'twins' as well
#             if id0 <= ij0 <= ij1 <= id1:
#                 return "", 0 , given_list[ij]




            
#     return None


# def range_mutation( given_list:list[str],new_val:str, index_update:int, removal_val:str):
#     if new_val != "":
#         given_list[index_update] = new_val
#     given_list.remove(removal_val)




# while(processed := id_overlapers(fresh_ids)) is not None:
#     print(f"len list before mutation: {len(fresh_ids)}")
#     range_mutation(fresh_ids, processed[0], processed[1], processed[2])
#     print(f"len list after mutation: {len(fresh_ids)}")





# # def recursive_range_concatenation(given_list: list[str]):
# #     for i in given_list:
# #         splited = i.split("-")
# #         id0 = int(splited[0])
# #         id1 = int(splited[1])
# #         for ij in given_list:
# #             if i == ij : continue
# #             splitted = ij.split('-')
# #             ij0 = int(splitted[0])
# #             ij1 = int(splitted[1])
# #             if id0 == ij0 and id1 == ij1:
# #                 continue
# #             if  ij0 <= id1 <= ij1 or id0 <= ij1 <= id1:
# #                 if ij0 <= id0 <= ij1:
# #                     i = ""+str(id0) + "-" + str(ij1)
# #                     print(f"picked for removal: {ij}")
# #                     print(f"new range = {i}")
# #                     if fresh_ids.__contains__(i):
# #                         fresh_ids.remove(ij)
# #                     recursive_range_concatenation(given_list)
# #                 if id0 <= ij1 <= id1:
# #                     i = ""+str(ij0) + "-" + str(id1)
# #                     print(f"picked for removal: {ij}")
# #                     print(f"new range = {i}")
# #                     if fresh_ids.__contains__(i):
# #                         fresh_ids.remove(ij)
# #                     recursive_range_concatenation(given_list)

# # recursive_range_concatenation(fresh_ids)

# # for i in range(len(fresh_ids)):
# #     splited = fresh_ids[i].split("-")
# #     id0 = int(splited[0])
# #     id1 = int(splited[1])
    
# #     for ij in range(len(fresh_ids)):
# #         total_extracted = 0
# #         splitted = fresh_ids[ij].split('-')
# #         ij0 = int(splitted[0])
# #         ij1 = int(splitted[1])
# #         if id0 == ij0 and id1 == ij1:
# #             continue
# #         if  ij0 <= id1 <= ij1 or id0 <= ij1 <= id1:
# #             print(f"AAA -> Found Interlapping ids")
# #             # if hash_fresh != hash(fresh_ids): print(f"OOO, the freshId-list is changing, checkout hashes: {hash_fresh} vs {hash(fresh_ids)}")
# #             if ij0 <= id1 <= ij1:
# #                 # fresh_ids[i] = ""+str(id0) + "-" + str(id1)
# #                 print(f"i at place: {fresh_ids[i]}")
# #                 print(f"fresh ij before {fresh_ids[ij]}")
# #                 if id0 == id1:
# #                     print(f"ERROR : how found range 0 {id0} vs {id1}")
# #                 else:
# #                     list_of_used.append(""+str(id0) + "-" + str(ij1))
# #                     total_extracted +=1
# #                 print(f"fresh ij after {fresh_ids[ij]}")

# #             if id0 <= ij1 <= id1:
# #                 # fresh_ids[ij] = ""+str(ij0) + "-" + str(ij1)
# #                 print(f"if at place: {fresh_ids[ij]}")
# #                 print(f"fresh i before {fresh_ids[i]}")
# #                 if ij0 == ij1 : 
# #                     print(f"ERROR : how found range 0 {ij0} vs {ij1}")
# #                 else:
# #                     list_of_used.append(""+str(ij0) + "-" + str(id1))
# #                     total_extracted += 1
# #                 print(f"fresh i after {fresh_ids[i]}")
# #             # ij = i 
# #         if total_extracted == 0:
# #             list_of_used.append()

# # pick up unique values
# print(f"len list before set: {len(fresh_ids)}")

# # fresh_ids_new = set(fresh_ids)
# fresh_fresh = list(dict.fromkeys(fresh_ids)) #list[str](fresh_ids_new)
# print(f"len list after set: {len(fresh_fresh)}")

# # repeating = [x for x in fresh_fresh if  fresh_ids.count(x) > 1] 
# # repeating = [val for i , val in enumerate(fresh_ids) if fresh_ids.index(val) != i] 
# # print(f"repeatin len: {len(repeating)}")
# # for x in repeating:
# #     y = fresh_fresh[fresh_fresh.index(x)]
    
# #     print(f"repeating nums check: {x} vs {y}")
# # print(f"len set: {len(fresh_fresh)}")

# for i in range(len(fresh_fresh)):
#     splited = fresh_fresh[i].split("-")
#     print(f"Counter: {counter}")
#     print(f"range : {fresh_fresh[i]}")
#     diff = int(splited[1]) - int(splited[0])
#     if diff == 0:
#         counter += 1
#         continue
#     print(f"adding: {(int(splited[1]) - int(splited[0]) + 1)}")
#     counter += (int(splited[1]) - int(splited[0]) + 1)
#     # print(f"at {i} from {len(fresh_fresh)}")
#     # for j in range(int(splitted[0]), int(splitted[1]) + 1):
#     #     counter += j
#     # for i in range(int(splited[0]), int(splited[1])+1):
#         # unique_ids.add(i)
# print(f"total: {counter}")
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