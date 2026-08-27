

content = ""
row:int = 0
col:int = 0
cube_coord = [-1,0,1]
total_papers:int = 0
with open("papers.txt", "r") as file:
    content = file.read().splitlines()

line_length = len(content[0])
print(f"test existent row 0, index 0: 1{content[1][-1]}")
print(f"test unexistent row: -1{content[-1]}")

for l in range (0,len(content)):
    for ch in range (0, len(content[l])):
        print(f"line num {l}")

        if content[l][ch] == "@":
            papers_at_index = 1
            for i in cube_coord:
                for j in cube_coord:
                    if ((l + i) < 0 or 0 > (ch + j)) or (j == 0 and i == 0)  or (l + i) >= len(content) or (ch + j) >= len(content[l]):
                        continue
                    else:
                        if content[l+i][ch+j] == "@":
                            papers_at_index += 1
                            if papers_at_index > 4:break
            if papers_at_index  <= 4 : total_papers += 1

print(f"total papers: {total_papers}")