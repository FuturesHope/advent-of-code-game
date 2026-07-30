from pathlib import Path
from time import sleep

file_path = Path("moves.txt")
moves:list[str] = []
dial_circle = list(range(0,100))
steps:int = 0
direction:str = ""
dialValue:int = dial_circle[50]
hit_zero_counter:int = 0
print(f'dial_circle starting point = {dial_circle[50]}')

def process_moves(moves: list[str]) -> None:
    global steps, direction, dialValue, hit_zero_counter
    for line in moves:
        direction = line[0]
        steps = int(line[1:].strip())
        if direction.lower() == 'r':
            for i in range(steps):
                dialValue = dial_circle[(dial_circle.index(dialValue) + 1) % len(dial_circle)]
                # print(f'dialValue = {dialValue}')
                # sleep(0.05)  # Pause for 0.5 seconds between moves
                if dialValue == 0:
                    hit_zero_counter += 1
                    # print(f"Hit zero! Current zero counter: {hit_zero_counter}")
            # dialValue = dial_circle[(dial_circle.index(dialValue) + steps) % len(dial_circle)]
        elif direction.lower() == 'l':
            for i in range(steps):
                dialValue = dial_circle[(dial_circle.index(dialValue) - 1) % len(dial_circle)]
                # print(f'dialValue = {dialValue}')
                # sleep(0.05)  # Pause for 0.5 seconds between moves
                if dialValue == 0:
                    hit_zero_counter += 1
                    # print(f"Hit zero! Current zero counter: {hit_zero_counter}")
            # dialValue = dial_circle[(dial_circle.index(dialValue) - steps) % len(dial_circle)]
            #sleep(0.5)  # Pause for 0.5 seconds between moves
            #print(f'dialValue = {dialValue}')
        else:
            print(f"Invalid direction '{direction}' in line: {line}")
            break

        # if dialValue == 0:
        #     hit_zero_counter += 1
    print(f"Final zero counter value: {hit_zero_counter}")

with open(file_path, "r", encoding="utf-8") as file:
    moves = file.readlines()
    #count = len(file.readlines())
    #print(count)

process_moves(moves)

# for i in range(len(moves)):
#     line = moves[i]

#     print(line, end="")
#     sleep(0.5)  # Pause for 1 second between moves
#     print(f"direction = {line[0]}", f'moves = {line[1:].strip()}')

    # with open(file_path, "r", encoding="utf-8") as file:
#     for i in range(3):
#         line = file.readline()
#         print(line, end="")
#         sleep(0.5)  # Pause for 1 second between moves
#         print(f"direction = {line[0]}", f'moves = {line[1:].strip()}')
        # print(f"direction = {line[0]}", f'moves = {line[1:]}')
        # print(f"direction = {line[0]}", f'type = {type(line[1:])}')
        #print(len(file.readlines()))