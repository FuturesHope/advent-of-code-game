

content = ""
row:int = 0
col:int = 0
row_coord = [-1,0,1]
col_coord = [-1,0,1]
total_papers:int = 0
with open("papers.txt", "r") as file:
    content = file.read().splitlines()
    print(f"content at 0 {content[0]}")
    print(f"type {type(content)}")
    print(f"len {len(content)}")
    # print(f"splitlines {content.splitlines()[0]}")

for line in content:
    print(f"Line num: {content.index(line)}")
    for char in line:
        papers_at_index = 0
        if char == "@":
            for i in row_coord:
                for j in col_coord:
                    if i == 0 or j == 0: continue
                    if 



