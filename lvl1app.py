from pathlib import Path
from time import sleep

file_path = Path("moves.txt")
moves:list[str] = []
dial_circle = list(range(0,100))
steps:int = 0
direction:str = ""
dialValue:int = dial_circle[50]
hit_zero_counter:int = 0
print(dial_circle[50])

def process_moves(moves: list[str]) -> None:
    #global steps, direction, dialValue, hit_zero_counter
    for line in moves:
        direction = line[0]
        steps = int(line[1:].strip())
        if direction.lower() == 'r':

            for i in range(steps):
                for i in range(steps):
                    dialValue = dial_circle[(dial_circle.index(dialValue) + 1) % len(dial_circle)]
                    print(f'dialValue = {dialValue}')
                    sleep(0.5)  # Pause for 0.5 seconds between moves
                    if dialValue == 0:
                        hit_zero_counter += 1
            
        elif direction.lower() == 'l':
            for i in range(steps):              
                dialValue = dial_circle[(dial_circle.index(dialValue) - 1) % len(dial_circle)]
                print(f'dialValue = {dialValue}')
                sleep(0.5)  # Pause for 0.5 seconds between moves
                if dialValue == 0:
                    hit_zero_counter += 1
        else:
            print(f"Invalid direction '{direction}' in line: {line}")
            sleep(3)  # Pause for 3 seconds to allow the user to read the error message
            break

    print(f"Final zero counter value: {hit_zero_counter}")



with open(file_path, "r", encoding="utf-8") as file:
    moves = file.readlines()

process_moves(moves)