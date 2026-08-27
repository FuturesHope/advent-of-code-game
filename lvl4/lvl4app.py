

content : list[chr]

new_content = ""
row:int = 0
col:int = 0
cube_coord = [-1,0,1]
total_papers:int = 0
total_times_func_activated = 0
with open("papers.txt", "r") as file:
    content = [list(line.strip()) for line in file if line.strip()]  #list(file.read().splitlines())

copy_content = content
for j in range(3):
    print(f"line: {j} value: {content[j]}")
# line_length = len(content[0])
print(f"test existent row 0, index 0: 1{content[1][-1]}")
print(f"test unexistent row: -1{content[-1]}")

#return removed papers count
def process_papers(input_content) -> int:
    global total_papers
    global total_times_func_activated
    global content
    global copy_content

    total_removed = 0

    for l in range (0,len(input_content)):
        # print(f"line num {l}")
        for ch in range (0, len(input_content[l])):

            if input_content[l][ch] == "@":
                papers_at_index = 1
                for i in cube_coord:
                    for j in cube_coord:
                        if ((l + i) < 0 or 0 > (ch + j)) or (j == 0 and i == 0)  or (l + i) >= len(input_content) or (ch + j) >= len(input_content[l]):
                            continue
                        else:
                            if input_content[l+i][ch+j] == "@":
                                papers_at_index += 1
                                if papers_at_index > 4:break
                if papers_at_index  <= 4 :
                    total_removed += 1
                    # char_list = list(content[l])
                    # char_list[ch] = "."
                    # content[l] = "".join(char_list)
                    input_content[l][ch] = "."

    total_times_func_activated += 1

    copy_content = input_content
    print(f"total removed: {total_removed}")
    total_papers += total_removed
    return total_removed


while process_papers(copy_content) > 0:
    process_papers(copy_content)


# for i in range(3):
#     print(f"".join(content[i]))
print(f" total times func activated = {total_times_func_activated}")
print(f"total papers: {total_papers}")
print(copy_content)